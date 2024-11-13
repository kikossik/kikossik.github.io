---
title: "Does Climate Change Affect Oil & Gas Infrastructure?"
excerpt: "<em>Interactive Visualization, Data Processing, Conference Speaking</em><br/>d3.js, Python<br/><br/>This project is the result of some cool research I did at Stony Brook University, guided by Dr. Halada (Materials Science) and Dr. Montgomery (Economics). I even got to mix it up with Dr. Mueller's Data Visualization class in Computer Science, so it became a mashup of everything I love about data science—bringing together different fields to tell a story with data!<br/><img src='/images/oil_gas_pic.PNG'>"
collection: portfolio
---
## Key accomplishments:
- Created an interactive dashboard showcasing high-risk geographical areas where *hazardous liquid pipelines* are prone to damage, helping material scientists focus on these areas to develop anti-crack and corrosion-resistant coatings for the pipelines.
- Presented research at the SBU Economics Conference and showcased a poster for the <a href="https://www.stonybrook.edu/commcms/vertically-integrated-projects/teams/_team_page/team_page.php?team=Engineering%20Adaptation%20to%20Climate%20Change%20(EACC)" target="_blank">EACC VIP</a> team with Prof. Halada at the URECA Symposium.

---
## 1 - Data Cleaning  
I got the data from <a href="https://www.phmsa.dot.gov/data-and-statistics/pipeline/data-and-statistics-overview" target="_blank">*Federal Pipeline and Hazardous Materials Safety Administration (PHMSA)*</a>. Since it spans from 1986 to 2022, the format was inconsistent across three different Excel files, each with unique formatting. About 80% of my work involved data cleaning and preprocessing. I’ve attached my Jupyter Notebook file for anyone interested in exploring it further. *Side note*: I also merged data on Temperature and Extreme Storm Events from 1986 to 2022 (sourced from [NOAA.gov](NOAA.gov)), as these factors are also susceptible to change due to climate change. Ultimately, this was not used in the visualization, but it's good I kept it since you can see more work inside the Notebook!  
Jupyter Notebook - <a href="https://github.com/kikossik/kikossik.github.io/blob/master/files/notebooks/oil_gas_spill.ipynb" target="_blank">GitHub</a> <a href="https://nbviewer.org/github/kikossik/kikossik.github.io/blob/master/files/notebooks/oil_gas_spill.ipynb" target="_blank">NBViewer</a>

---
## 2 - Interactive Dashboard  
I had the opportunity to integrate my research with **CSE 332 - Introduction to Scientific Visualization** class taught by Prof. Mueller, where I created this interactive dashboard. It was an awesome learning experience, especially since I had to learn **D3.js** and code everything from scratch – from the axes to the visuals and animations. One thing I noticed, though, is that having too many categories in the bar plot made it tough to see things clearly. Looking back, it would’ve been better to keep fewer categories or maybe even just stick to the map as it’s the key element for identifying high-risk areas prone to pipeline damage. Overall, I learned a ton about keeping things clear and knowing what to focus on when building a solid graph or dashboard.  
View the <a href="https://kikossik.pythonanywhere.com/" target="_blank">full dasbhoard here</a>

---
## 3 - SBU Economics Conference and URECA
I got to present my research at the **SBU Economics Conference**, which was a cool way to share my work with others. I also put together a poster for **URECA** as part of the <a href="https://www.stonybrook.edu/commcms/vertically-integrated-projects/teams/_team_page/team_page.php?team=Engineering%20Adaptation%20to%20Climate%20Change%20(EACC)" target="_blank">**EACC VIP**</a> team with Prof. Halada, and it was a great experience getting our project out there for more people to see.  
<img src='/images/poster.PNG'>



