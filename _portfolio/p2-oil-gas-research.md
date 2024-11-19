---
title: "Does Climate Change Affect Oil & Gas Infrastructure?"
excerpt: "<span>- Interactive Visualization, Data Processing, Conference Speaking</span><br/>- Python, d3.js<br/><br/>This project stems from research I conducted at Stony Brook University under the guidance of Dr. Halada (Materials Science) and Dr. Montgomery (Economics). I had the chance to merge this work with Prof. Mueller’s Data Visualization class, which led to creating an interactive dashboard. This project captures what data science is all about - the intersection of multiple disciplines coming together to tell a meaningful story.<br/><br/><img src='/images/oil_gas_pic.PNG'>"
collection: portfolio
---

Key accomplishments:
---
- Created an interactive dashboard showcasing high-risk geographical areas where *hazardous liquid pipelines* are prone to damage, helping material scientists focus on these areas to develop anti-crack and corrosion-resistant coatings for the pipelines.
- Presented research at the SBU Economics Conference and showcased a poster for the <a href="https://www.stonybrook.edu/commcms/vertically-integrated-projects/teams/_team_page/team_page.php?team=Engineering%20Adaptation%20to%20Climate%20Change%20(EACC)" target="_blank">EACC VIP</a> team with Prof. Halada at the URECA Symposium.

Brief Preliminaries to The Problem
---
**Climate Change and Pipeline Infrastructure**   
The oil and gas industry forms a critical component of the global energy supply chain, yet it is increasingly vulnerable to the impacts of climate change. Rising temperatures, sea-level rise, and extreme weather events have introduced new challenges, particularly in regions like the Gulf of Mexico, where environmental conditions and aging infrastructure intersect. Pipeline systems, vital for the transportation of hazardous liquids and gases, face heightened risks of accidents and failures due to shifting soil conditions, flooding, and structural corrosion.  
**Scope of Study**  
This project focuses on understanding the interplay between climate change and pipeline failures in the United States. By utilizing incident heat maps, predictive modeling of sea-level rise, and case studies of damaged infrastructure, the study aims to highlight the geographic and operational vulnerabilities of hazardous liquid and gas transmission pipelines. 

Data Cleaning
---
I got the data from <a href="https://www.phmsa.dot.gov/data-and-statistics/pipeline/data-and-statistics-overview" target="_blank">*Federal Pipeline and Hazardous Materials Safety Administration (PHMSA)*</a>. Since it spans from 1986 to 2022, the format was inconsistent across three different Excel files, each with unique formatting. About 80% of my work involved data cleaning and preprocessing. I’ve attached my Jupyter Notebook file for anyone interested in exploring it further. *Side note*: I also merged data on Temperature and Extreme Storm Events from 1986 to 2022 (sourced from <a href="https://www.noaa.gov/" target="_blank">*NOAA.gov*</a>), as these factors are also susceptible to change due to climate change. Ultimately, this was not used in the visualization, but it's good I kept it since you can see more work inside the Notebook!  
---> Jupyter Notebook - <a href="https://github.com/kikossik/kikossik.github.io/blob/master/files/notebooks/oil_gas_spill.ipynb" target="_blank">GitHub</a> | <a href="https://nbviewer.org/github/kikossik/kikossik.github.io/blob/master/files/notebooks/oil_gas_spill.ipynb" target="_blank">NBViewer</a>

Interactive Dashboard
---
I had the opportunity to integrate my research with **CSE 332 - Introduction to Scientific Visualization** class taught by Prof. Mueller, where I created this interactive dashboard. It was a great learning experience, especially since I had to learn **D3.js** and code everything from scratch. One thing I noticed, though, is that having too many categories in the bar plot made it tough to see things clearly. Looking back, it would’ve been better to keep fewer categories or maybe even just stick to the map as it is the key element for identifying high-risk areas prone to pipeline damage.  
---> View the <a href="https://kikossik.pythonanywhere.com/" target="_blank">full dasbhoard here</a>

SBU Economics Conference and URECA
---
I got to present my research at the **SBU Economics Conference**, and I also put together a poster for **URECA** as part of the <a href="https://www.stonybrook.edu/commcms/vertically-integrated-projects/teams/_team_page/team_page.php?team=Engineering%20Adaptation%20to%20Climate%20Change%20(EACC)" target="_blank">**EACC VIP**</a> team with Prof. Halada. It was a great experience getting our project out there for more people to see. I have attached my poster below, where you can see my work in researching about the topic and creating more visualizations to help capture the story better.  

<img src='/images/poster.PNG'>



