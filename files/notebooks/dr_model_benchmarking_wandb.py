# libs = ['wandb','timm','seaborn']
# print("Please install these libraries before running the notebook (and obviously configure your own kaggle.json):")
# for lib in libs:
#     print(f"- {lib}")
# print('---')
# print('---')
# print('---')
import os
import torch
import torchmetrics
import torch.nn as nn
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
import wandb
from pytorch_lightning.loggers import WandbLogger
from sklearn.metrics import f1_score, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay
import timm
import timm.models
import time
import psutil
import numpy as np
from torch.cuda import max_memory_allocated
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# Define base directory
BASE_DIR = 'kaggle_data'
TRAIN_CSV = os.path.join(BASE_DIR, 'train.csv')
TEST_CSV = os.path.join(BASE_DIR, 'test.csv')
TRAIN_IMG_DIR = os.path.join(BASE_DIR, 'train_images')
# TEST_IMG_DIR = os.path.join(BASE_DIR, 'test_images') commented out since we don't need this

# GOAL - 1 - current goal of this project is to compare most used deep learning models in ophtalmology for diabetic retinopathy classification and see how they perform
# on NVIDEA L4. potentially we can extend and compare with other GPUs as well, but for now we focus on L40S provided from Lightning AI
# - 2 - after that we select two models, one with best performance, and one that is most efficient. then we will apply image preprocessing to our data
# and hyperparameter tuning to get both models as best scores as possible

# creating custom dataset for our files
# we have train_images and test_images folders. our logic is to create train/valid/test splits from train_images, since test_images 
# don't have labels (this is kaggle competition data)

# in torch, we can define our custom dataset by extending the Dataset class, where __init__, __len__, __getitem__ methods are required to be implemented
class DRDataset(Dataset):
    # __init__ method is used to initialize the dataset and is run once
    def __init__(self, csv_file, img_dir, transform=None):
        self.data = pd.read_csv(csv_file)
        self.img_dir = img_dir
        self.transform = transform # very basic image transformation will be applied later on

    # __len__ method is used to return the length of the dataset    
    def __len__(self):
        return len(self.data)
    
    # __getitem__ method is used to return the image and label for a given index
    def __getitem__(self, idx):
        img_name = self.data.iloc[idx]['id_code']
        if not img_name.endswith('.png'): # double checking for other formats
            img_name = f"{img_name}.png"
        img_path = os.path.join(self.img_dir, img_name)
        
        try:
            image = Image.open(img_path)
            if image.mode != 'RGB': # double checking for RGB
                image = image.convert('RGB')
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")
            image = Image.new('RGB', (224, 224))
            
        if self.transform:
            image = self.transform(image)
        
        label = self.data.iloc[idx]['diagnosis']
            
        return image, label

# defining our model
class DRClassifier(torch.nn.Module):
    # __init__ defines layers and other components for our models
    def __init__(self, model_name, num_classes=5):
        super().__init__()
        self.model_name = model_name
        use_pretrained = model_name not in ['efficientnet_b6', 'efficientnet_b7'] # efficientnet_b6 and b7 don't have pretrained weights from timm
        self.model = timm.create_model(model_name, pretrained=use_pretrained, num_classes=num_classes) # timm uses 'best' parameters for each model
        self.criterion = nn.CrossEntropyLoss()
        self.inference_times = []
        self.batch_times = []
        
        # Create metrics using torchmetrics
        metrics = torchmetrics.MetricCollection({
            'accuracy': torchmetrics.Accuracy(task='multiclass', num_classes=num_classes),
            'f1_score': torchmetrics.F1Score(task='multiclass', num_classes=num_classes),
            'auroc': torchmetrics.AUROC(task='multiclass', num_classes=num_classes),
            'precision': torchmetrics.Precision(task='multiclass', num_classes=num_classes),
            'recall': torchmetrics.Recall(task='multiclass', num_classes=num_classes)
        })
        
        self.train_metrics = metrics.clone(prefix='train_')
        self.val_metrics = metrics.clone(prefix='val_')
        self.test_metrics = metrics.clone(prefix='test_')
        
        # Store predictions and targets for confusion matrix
        self.test_predictions = []
        self.test_targets = []

    # computation is done here
    def forward(self, x):
        return self.model(x) # passes input through the model created in __init__ with timm.create_model
    
    # defining single step of training
    def training_step(self, batch, device):
        batch_start_time = time.time()
        images, labels = batch
        images, labels = images.to(device), labels.to(device)
        
        # Forward pass
        outputs = self(images)
        loss = self.criterion(outputs, labels)
        
        # Calculate probabilities and predictions
        probas = torch.softmax(outputs, dim=1)
        _, predicted = torch.max(outputs.data, 1)
        
        # Update metrics
        self.train_metrics.update(probas, labels)
        
        # Calculate batch time
        batch_time = time.time() - batch_start_time
        self.batch_times.append(batch_time)
        
        return {
            'loss': loss,
            'batch_time': batch_time,
            'predictions': predicted,
            'labels': labels,
            'probas': probas
        }
    
    # defining single step of validation
    def validation_step(self, batch, device):
        self.eval()
        with torch.no_grad():
            images, labels = batch
            images, labels = images.to(device), labels.to(device)
            
            # Start inference timer
            inference_start = time.time()
            
            # Forward pass
            outputs = self(images)
            loss = self.criterion(outputs, labels)
            
            # Calculate probabilities and predictions
            probas = torch.softmax(outputs, dim=1)
            _, predicted = torch.max(outputs.data, 1)
            
            # Update metrics
            self.val_metrics.update(probas, labels)
            
            # Calculate inference time
            inference_time = time.time() - inference_start
            self.inference_times.append(inference_time)
            
        self.train()
        return {
            'loss': loss,
            'inference_time': inference_time,
            'predictions': predicted,
            'labels': labels,
            'probas': probas
        }
    
    # defining single step of testing
    def test_step(self, batch, device):
        self.eval()
        with torch.no_grad():
            images, labels = batch
            images, labels = images.to(device), labels.to(device)
            
            # Start inference timer
            inference_start = time.time()
            
            # Forward pass
            outputs = self(images)
            loss = self.criterion(outputs, labels)
            
            # Calculate probabilities and predictions
            probas = torch.softmax(outputs, dim=1)
            _, predicted = torch.max(outputs.data, 1)
            
            # Update metrics
            self.test_metrics.update(probas, labels)
            
            # Store predictions and targets for confusion matrix
            self.test_predictions.extend(predicted.cpu().numpy())
            self.test_targets.extend(labels.cpu().numpy())
            
            # Calculate inference time
            inference_time = time.time() - inference_start
            self.inference_times.append(inference_time)
            
        return {
            'loss': loss,
            'inference_time': inference_time,
            'predictions': predicted,
            'labels': labels,
            'probas': probas
        }
    
    def get_metrics(self, mode='train'):
        if mode == 'train':
            metrics = self.train_metrics
        elif mode == 'val':
            metrics = self.val_metrics
        else:  # test
            metrics = self.test_metrics
            
        computed_metrics = metrics.compute()
        metrics.reset()
        return computed_metrics
    
# the simple transformation i talked about before
def get_transforms():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
    ])


def create_data_loaders(train_split=0.7, val_split=0.15, batch_size=32, random_state=42):
    transform = get_transforms()
    
    # Create full dataset from train_images
    full_dataset = DRDataset( 
        TRAIN_CSV, 
        TRAIN_IMG_DIR, 
        transform=transform
    )
    
    # Calculate split sizes
    total_size = len(full_dataset)
    train_size = int(total_size * train_split)
    val_size = int(total_size * val_split)
    test_size = total_size - train_size - val_size
    
    # Split dataset into train, validation, and test
    train_subset, val_subset, test_subset = torch.utils.data.random_split(
        full_dataset, 
        [train_size, val_size, test_size],
        generator=torch.Generator().manual_seed(random_state)
    )
    
    # Create dataloaders
    train_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=True, num_workers=4) # num_workers speeds up loading with parallel data loading
    val_loader = DataLoader(val_subset, batch_size=batch_size, shuffle=False, num_workers=4)
    test_loader = DataLoader(test_subset, batch_size=batch_size, shuffle=False, num_workers=4) 
    
    return train_loader, val_loader, test_loader

# training models
def train_model(model, train_loader, val_loader, device, model_name, model_family, num_epochs=10, patience=4):
    wandb.init(
        project='wandb-dr-final',
        name=f"{model_name}_{time.strftime('%Y%m%d_%H%M%S')}",
        group=model_family,
        config={
            'model_name': model_name,
            'model_family': model_family,
            'learning_rate': 1e-4,
            'batch_size': train_loader.batch_size,
            'epochs': num_epochs,
            'optimizer': 'Adam',
            'scheduler': 'ReduceLROnPlateau',
            'architecture': model_name,
            'dataset': 'Diabetic Retinopathy',
            'total_params': sum(p.numel() for p in model.parameters()),
            'trainable_params': sum(p.numel() for p in model.parameters() if p.requires_grad)
        }
    )
    
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=3, factor=0.1)
    
    best_val_loss = float('inf')
    patience_counter = 0
    best_model_state = None
    training_history = []
    
    # Track GPU memory
    if torch.cuda.is_available():
        initial_memory = torch.cuda.memory_allocated(device) / 1024**2  # MB
    
    for epoch in range(num_epochs):
        model.train()
        epoch_start_time = time.time()
        
        # Training phase
        batch_times = []
        train_losses = []
        
        for batch in tqdm(train_loader, desc=f'Epoch {epoch+1}/{num_epochs} - Training'):
            # Training step
            train_output = model.training_step(batch, device)
            loss = train_output['loss']
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            train_losses.append(loss.item())
            batch_times.append(train_output['batch_time'])
        
        # Validation phase
        model.eval()
        val_losses = []
        inference_times = []
        
        with torch.no_grad():
            for batch in tqdm(val_loader, desc='Validation'):
                val_output = model.validation_step(batch, device)
                val_losses.append(val_output['loss'].item())
                inference_times.append(val_output['inference_time'])
        
        # Calculate epoch metrics
        train_metrics = model.get_metrics(mode='train')
        val_metrics = model.get_metrics(mode='val')
        epoch_train_loss = np.mean(train_losses)
        epoch_val_loss = np.mean(val_losses)
        epoch_time = time.time() - epoch_start_time
        
        # GPU memory tracking
        if torch.cuda.is_available():
            current_memory = torch.cuda.memory_allocated(device) / 1024**2
            memory_diff = current_memory - initial_memory
        else:
            memory_diff = 0
        
        # Update learning rate scheduler
        scheduler.step(epoch_val_loss)
        current_lr = optimizer.param_groups[0]['lr']
        
        # Log metrics to wandb
        wandb.log({
            'epoch': epoch + 1,
            'train_loss': epoch_train_loss,
            'val_loss': epoch_val_loss,
            'learning_rate': current_lr,
            'epoch_time': epoch_time,
            'avg_batch_time': np.mean(batch_times),
            'avg_inference_time': np.mean(inference_times),
            'gpu_memory_usage': memory_diff,
            'gpu_memory_total': current_memory if torch.cuda.is_available() else 0,
            **train_metrics,
            **val_metrics
        })
        
        # Store epoch results
        epoch_results = {
            'epoch': epoch + 1,
            'train_loss': epoch_train_loss,
            'val_loss': epoch_val_loss,
            'train_metrics': train_metrics,
            'val_metrics': val_metrics,
            'lr': current_lr,
            'epoch_time': epoch_time,
            'avg_batch_time': np.mean(batch_times),
            'avg_inference_time': np.mean(inference_times)
        }
        training_history.append(epoch_results)
        
        # Print epoch results
        print(f"\nEpoch {epoch+1}/{num_epochs}:")
        print(f"Train Loss: {epoch_train_loss:.4f}")
        print(f"Val Loss: {epoch_val_loss:.4f}")
        print(f"Train Metrics:", {k: f"{v:.4f}" for k, v in train_metrics.items()})
        print(f"Val Metrics:", {k: f"{v:.4f}" for k, v in val_metrics.items()})
        print(f"Learning Rate: {current_lr:.6f}")
        print(f"Avg Batch Time: {np.mean(batch_times):.4f}s")
        print(f"Avg Inference Time: {np.mean(inference_times):.4f}s")
        print(f"Epoch Time: {epoch_time:.2f}s")
        print(f"GPU Memory Usage: {memory_diff:.2f} MB")
        
        # Early stopping check
        if epoch_val_loss < best_val_loss:
            best_val_loss = epoch_val_loss
            best_model_state = model.state_dict()
            patience_counter = 0
        else:
            patience_counter += 1
            
        if patience_counter >= patience:
            print(f"\nEarly stopping triggered after {epoch+1} epochs")
            break
    
    # Restore best model
    if best_model_state is not None:
        model.load_state_dict(best_model_state)
    
    #wandb.finish()
    return model, training_history

def evaluate_model(model, test_loader, device, model_name, wandb_run):
    print(wandb_run)
    model = model.to(device)
    test_losses = []
    inference_times = []
    start_time = time.time()
    
    # Track GPU memory
    if torch.cuda.is_available():
        initial_memory = torch.cuda.memory_allocated(device) / 1024**2  # MB
    
    # Test phase
    model.eval()
    with torch.no_grad():
        for batch in tqdm(test_loader, desc='Testing'):
            # Test step
            test_output = model.test_step(batch, device)
            test_losses.append(test_output['loss'].item())
            inference_times.append(test_output['inference_time'])
    
    # Calculate test metrics
    test_metrics = model.get_metrics(mode='test')
    test_loss = np.mean(test_losses)
    avg_inference_time = np.mean(inference_times)
    total_test_time = time.time() - start_time
    
    # GPU memory tracking
    if torch.cuda.is_available():
        current_memory = torch.cuda.memory_allocated(device) / 1024**2
        memory_diff = current_memory - initial_memory
    else:
        memory_diff = 0
    
    # Log results to W&B
    wandb_run.log({
        'test_loss': test_loss,
        'avg_inference_time': avg_inference_time,
        'total_test_time': total_test_time,
        'gpu_memory_usage': memory_diff,
        'gpu_memory_total': current_memory if torch.cuda.is_available() else 0,
        **{f'test_{k}': v.item() for k, v in test_metrics.items()}
    })
    
    # Print results
    print(f"\nTest Results for {model_name}:")
    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test Metrics:", {k: f"{v:.4f}" for k, v in test_metrics.items()})
    print(f"Avg Inference Time: {avg_inference_time:.4f}s")
    print(f"Total Test Time: {total_test_time:.2f}s")
    print(f"GPU Memory Usage: {memory_diff:.2f} MB")
    
    # Create confusion matrix
    cm = confusion_matrix(model.test_targets, model.test_predictions)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix - {model_name}')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    
    wandb.log({
        'confusion_matrix': wandb.Image(plt),
        'confusion_matrix_values': cm
    })
    
    wandb.finish()
    plt.close()
    
    return {
        'test_loss': test_loss,
        'avg_inference_time': avg_inference_time,
        **{f'test_{k}': v.item() for k, v in test_metrics.items()}
    }, cm


def main():
    models = {
        'vgg': ['vgg11', 'vgg13', 'vgg16', 'vgg19'],
        'resnet': ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152'],
        'densenet': ['densenet121', 'densenet169', 'densenet201'],
        'inception': ['inception_v3', 'inception_v4', 'inception_resnet_v2'],
        'mobilenet': ['mobilenetv2_100', 'mobilenetv3_large_100', 'mobilenetv3_small_100'],
        'efficientnet': ['efficientnet_b0', 'efficientnet_b1', 'efficientnet_b2', 
                        'efficientnet_b3', 'efficientnet_b4', 'efficientnet_b5', 
                        'efficientnet_b6', 'efficientnet_b7'],
        'xception': ['xception', 'xception41', 'xception65', 'xception71']
    }
    # Set device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    # Create data loaders
    train_loader, val_loader, test_loader = create_data_loaders()
    
    # Initialize wandb
    wandb.login()
    
    # Train and evaluate each model
    for family, model_list in models.items():
        print(f"\nTraining models from {family} family:")
        family_results = {}
        
        for model_name in model_list:
            print(f"\nTraining {model_name}...")
            try:
                # Initialize wandb run with group
                wandbrun = wandb.init(
                    project="wandb-dr-final",
                    name=model_name,
                    group=family,
                    job_type="training"
                )
                
                # Initialize model
                model = DRClassifier(model_name)
                
                # Train model
                trained_model, history = train_model(
                    model, 
                    train_loader, 
                    val_loader, 
                    device,
                    model_name,
                    family
                )
                
                # Evaluate model
                test_results, confusion_mat = evaluate_model(
                    trained_model, 
                    test_loader, 
                    device,
                    model_name,
                    wandbrun
                )

                wandbrun.finish()
                
            except Exception as e:
                print(f"Error training {model_name}: {str(e)}")
                wandb.finish()  # Ensure the wandb run is finished even on exception
                continue
        
if __name__ == "__main__":
    main()
