---
title: "Job Posting Distributed Database Management System"
excerpt: "<span>- Distributed Database Management System, Data Scraping, Custom Hash Partitioning</span><br/>- Python, Django, MySQL, Selenium WebDriver, BeautifulSoup<br/><br/>Developed a Django-based Distributed Database Management System for job postings from scratch, utilizing a custom hash function to partition data across 3 MySQL databases. The dataset was obtained by scraping LinkedIn Jobs using Selenium WebDriver for automated navigation and BeautifulSoup for HTML parsing.<br/><img src='/images/django.PNG'>"
collection: portfolio
---

Key accomplishments:
---
- Designed and implemented a Django-based Distributed Database Management System from scratch, optimizing data handling for job postings through efficient, custom data partitioning across three MySQL databases.
- The hash function for partitioning was calculated by adding up the ASCII values of all characters in the title, then applying a modulo operation by 3 (to match the number of databases) to determine the target database . This approach distributes data evenly and reduces retrieval time by ensuring balanced database loads.
- Data scraping from LinkedIn Jobs using Selenium WebDriver for navigation and BeautifulSoup for HTML parsing, simulating a robust and comprehensive job postings dataset.

Cool Features
---
- **Hash Function**  
The hash function implementation is to distribute data across three databases. A hash function, as described <a href="https://pages.cs.wisc.edu/~siff/CS367/Notes/hash.html" target="_blank">here</a>, maps input data (in this case, the length of job titles) to a numerical value within a fixed range. This function calculates the length of the job title, applies the modulo operator (%) with the number of databases (3), and assigns the data to one of the three databases based on the result. This hashing approach is needed to evenly distribute data across the databases, preventing overcrowding in a single database and ensuring efficient storage and retrieval of information.  
```
def hash_by_title_length(self, title):
    # Initialize the hash value
    hashVal = 0
    # Accumulate the ASCII values of each character in the title
    for char in title:
        hashVal += ord(char)
    # Mod by 3 since we have 3 databases
    return hashVal % 3
```
- **Bulk Import**  
Custom command is implemented to import job listings from a CSV file (acquired from our scraping) and distribute them across three databases based on the hash of the job title length. The command reads each row from the CSV file, processes the job data (including parsing dates and other features), and determines the target database using the *get_db_for_job* method, which employs a hash function. Finally, jobs are bulk imported into their respective databases using Django's *bulk_create* method, optimizing database operations and ensuring efficient data storage.  
---> View the <a href="https://github.com/kikossik/Job-Posting-Distributed-Database-Management-System/blob/main/django_project/blog/management/commands/import_jobs.py" target="_blank">bulk import here</a>  
- **Bulk Removal**  
Custom command is implemented to efficiently remove job listings within a specified date range from one or multiple databases. The command accepts the database name (*first_db*, *second_db*, *third_db*, or *all*) and the date range as arguments. Based on the selected database(s), the command uses Django's ORM to query jobs within the specified range. The matched jobs are then removed using the *delete* method, and the number of deleted jobs is tracked and displayed for each database. If all databases are selected, the total number of removed jobs is summarized at the end.  
---> View the <a href="https://github.com/kikossik/Job-Posting-Distributed-Database-Management-System/blob/main/django_project/blog/management/commands/remove_jobs.py" target="_blank">bulk removal here</a>  
- **Scraper**
Scraper to gather job postings from LinkedIn using a combination of Selenium for navigating dynamic web pages and BeautifulSoup for parsing HTML content. The function automates job searches by inputting a job title, location, and optional page count, iteratively scrolling through job listings and extracting details like job title, company, location, description, salary, and more. The collected data is cleaned and saved into a structured CSV file using pandas.  
---> View the <a href="https://github.com/kikossik/Job-Posting-Distributed-Database-Management-System/blob/main/linkedin_scrape.py" target="_blank">scraper here</a>  


You can find the full project on <a href="https://github.com/kikossik/Job-Posting-Distributed-Database-Management-System" target="_blank">GitHub</a>, where you can fork or set it up on your local machine. Comprehensive documentation for the setup is provided there.