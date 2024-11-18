---
title: "New York City Rental Affordability Analysis"
excerpt: "<span>- Distributed Database Management System, Data Scraping, Custom Hash Partitioning</span><br/>- Python, Django, MySQL, Selenium WebDriver, BeautifulSoup<br/><br/>Developed a Django-based Distributed Database Management System for job postings from scratch, utilizing a custom hash function to partition data across 3 MySQL databases. The dataset was obtained by scraping LinkedIn Jobs using Selenium WebDriver for automated navigation and BeautifulSoup for HTML parsing.<br/><img src='/images/mihnyc.PNG'>"
collection: portfolio
---

Key accomplishments:
---
- nlah nlah
- more blah blah

Key Goals and Project Description
---
This project focuses on analyzing housing affordability in New York City using detailed datasets on renter incomes, rental prices, and zoning policies. The goal is to evaluate how well current metrics, such as Area Median Income (AMI) affordability, reflect the real affordability challenges faced by renters in different community districts. By computing and comparing affordability metrics, we aim to identify discrepancies, understand spatial affordability patterns, and provide insights into the effectiveness of existing housing policies, including Mandatory Inclusionary Housing (MIH) programs.

Brief Preliminaries to The Problem
---
**MIH Affordability**  
Mandatory Inclusionary Housing (MIH) is a zoning tool aimed at addressing housing affordability in New York City by requiring developers to include affordable units in new residential projects. However, affordability under MIH is calculated using fixed percentages of the Area Median Income (AMI), which may not accurately reflect the financial realities of local residents. This disconnect raises concerns about whether MIH truly meets the affordability needs of low- and middle-income households in high-demand areas.  
**Affordability Analysis**  
Housing affordability is traditionally assessed using benchmarks like AMI, but these standardized measures often fail to capture district-specific income variations. This project explores both AMI-based and custom metrics, where affordability is tailored to the median renter income in each community district. By comparing these approaches, we aim to identify gaps in affordability metrics and understand how well current models align with actual economic conditions.  
**Why Calculate Affordability This Way?**  
Using the widely accepted "one-third of income" rule to define affordability provides a practical lens to assess housing burdens. However, AMI-based thresholds can overgeneralize affordability, particularly in diverse cities like NYC where income levels vary significantly across districts. A district-specific metric, based on local renter incomes, offers a more accurate depiction of affordability challenges.

Data
---
- **NYC Sales Data**  
Contains records of property sales in NYC, including variables such as price, building category, and geographic coordinates.
- **Commercial Zones Shapefiles**  
Spatial polygons representing commercial zones in NYC.
- **MIH Zones**  
Inclusionary housing zones under Mandatory Inclusionary Housing (MIH) regulations.
- **Community Districts**  
Community Districts shapefiles with demographic and economic attributes, such as rental affordability and median income for renters.

Visualizing the Data
---
**NYC Housing Dynamics**  
This map visualizes the spatial patterns of property sales density, Mandatory Inclusionary Housing (MIH) zones, and commercial zoning areas in New York City.  
<img src='/images/heatmap.png'>  
- The heatmap reveals that Manhattan is the epicenter of property sales. Peripheral areas in Brooklyn and Queens also show high activity, possibly due to spillover effects as people and businesses move out of Manhattan to relatively more affordable areas.  
- MIH zones often overlap with areas of high sales density, however, most of the MIH zones are designed in poor neighborhoods.  
- With commercial zones, it is evident that they are primarily prominent in areas with the highest Sales, such as Manhattan.  

**NYC Housing Affordability**

<div style="display: flex; flex-direction: column; align-items: center;">

- **Rental Affordability at 80% AMI**  
  <img src="./images/rent_afford_80_ami.png" width="500">  

- **Median Income for Renters**  
  <img src="./images/median_income_rent.png" width="500">  

- **Median Rent**  
  <img src="./images/median_rent.png" width="500">  

</div>


**Takeaway**  
-The maps highlight a clear spatial correlation: areas with higher median incomes (Map 2) also have higher median rents (Map 3). Manhattan and parts of Brooklyn dominate these categories, suggesting significant economic disparities between boroughs.  
-Rental affordability (Map 1) is low in high-income, high-rent areas, emphasizing the lack of affordable housing in wealthier districts. Conversely, outer boroughs like the Bronx and Staten Island, with lower incomes and rents, provide better affordability.  
-The maps collectively underscore economic segregation in NYC. Wealthier populations and high rents are clustered in central and gentrified areas, while more affordable rents and lower incomes are prevalent in peripheral districts.