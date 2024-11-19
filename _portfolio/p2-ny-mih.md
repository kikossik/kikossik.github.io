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
This project focuses on analyzing housing affordability in New York City using detailed datasets on renter incomes, rental prices, and zoning policies. The goal is to evaluate how well current metrics, such as Area Median Income (AMI) affordability, reflect the real affordability challenges faced by renters in different community districts. By computing and comparing affordability metrics, we aim to identify discrepancies, understand spatial affordability patterns, and provide insights into the effectiveness of existing housing policies, including <a href="https://www.nyc.gov/site/planning/plans/mih/mandatory-inclusionary-housing.page" target="_blank">Mandatory Inclusionary Housing (MIH)</a> programs.

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
<p>
  This map visualizes the spatial patterns of  
  <span class="highlighted">property sales density</span>, 
  <span class="highlighted">Mandatory Inclusionary Housing (MIH) zones</span>, 
  and  
  <span class="highlighted">commercial zoning areas</span> in New York City.
</p>

<!-- SVG for the wavy highlight filter -->
<svg style="position: absolute; width: 0; height: 0;" xmlns="http://www.w3.org/2000/svg">
  <filter id="wavyHighlight" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" result="noise" seed="1" />
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="7" />
  </filter>
</svg>

<!-- CSS for the highlight effect -->
<style>
  .highlighted {
    position: relative;
    color: black; /* Text color */
  }

  .highlighted::before {
    content: '';
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background: hsla(0, 100%, 50%, 0.3); /* Red highlight */
    filter: url(#wavyHighlight);
    z-index: -1;
    transform: translate(-0.2em, -0.2em) skew(7deg, 0);
    border-radius: 4px; /* Rounded highlight */
  }

  .highlighted:nth-child(2)::before {
    background: hsla(240, 100%, 50%, 0.3); /* Blue highlight */
  }

  .highlighted:nth-child(3)::before {
    background: hsla(60, 100%, 50%, 0.3); /* Yellow highlight */
  }
</style>

<img src='/images/heatmap.png'>  
- The heatmap reveals that Manhattan is the epicenter of property sales. Peripheral areas in Brooklyn and Queens also show high activity, possibly due to spillover effects as people and businesses move out of Manhattan to relatively more affordable areas.  
- MIH zones often overlap with areas of high sales density, however, most of the MIH zones are designed in poor neighborhoods.  
- With commercial zones, it is evident that they are primarily prominent in areas with the highest Sales, such as Manhattan.  

**NYC Housing Affordability**

| Category          | Visualization           |
|------------------------------------|------------|
| **Rental Affordability at 80% AMI** | ![Rental Affordability](/images/rent_afford_80_ami.png) |
| **Median Income for Renters**      | ![Median Income](/images/median_income_rent.png)        |
| **Median Rent**                    | ![Median Rent](/images/median_rent.png)                |

- The maps highlight a clear spatial correlation: areas with higher median incomes (Map 2) also have higher median rents (Map 3). Manhattan and parts of Brooklyn dominate these categories, suggesting significant economic disparities between boroughs.  
- Rental affordability (Map 1) is low in high-income, high-rent areas, emphasizing the lack of affordable housing in wealthier districts. Conversely, outer boroughs like the Bronx and Staten Island, with lower incomes and rents, provide better affordability.  
- The maps collectively underscore economic segregation in NYC. Wealthier populations and high rents are clustered in central and gentrified areas, while more affordable rents and lower incomes are prevalent in peripheral districts.

Statistical Analysis
---
**Median Rent Price by Property Type**  
<img src='/images/box.png'>  
Before delving into the desired analysis, let's take a moment and look at this cool boxplot. This boxplot examines the distribution of median rent prices across various property types grouped into categories such as Residential, Condos & Co-ops, Commercial, Public & Cultural, and Other. It is obvious that Condos & Coops have the highest median rent prices on average than any other category. Residential properties have relatively consistent and moderate rent prices. We can observe a lot of variability in most of the property types.  

**Understanding drivers of Rent Prices**  
This analysis examines the relationship between median rent prices, median income for renters, and average sales price per census district (CD).  
<img src='/images/scat1.png'>  
Scatterplots reveal a strong positive correlation between renter income and rent prices, while the relationship between average sales price and rent prices is weaker but significant.
<img src='/images/reg1.png'>  
The regression model for predicting **Median Rent Price** is as follows:
\[
\text{MedianRentPrice} = 748.599 + (0.014 \times \text{MedianIncomeForRenters}) - (0.00001 \times \text{AverageSalesPriceCD})
\]
This model explains 91% of the variation in rent prices, showing that median income for renters has a significant positive effect on rent prices (\( \beta = 0.014 \), \( p < 0.01 \)). Interestingly, average sales price per CD negatively impacts rent prices (\( \beta = -0.00001 \), \( p < 0.01 \)).  

**Understand drivers of Sales Prices**  
This analysis investigates the factors influencing average sales prices per community district (CD) by examining their relationship with median homeowner income and median rent prices.  
<img src='/images/scat2.png'>  
Scatterplots reveal a positive correlation between median homeowner income and average sales prices, and average sales prices with median rent prices. However, the variation is definitely higher than in Rent price analysis.  
<img src='/images/reg2.png'>  
The regression model for predicting **Average Sales Price per CD** is as follows:
\[
\text{AverageSalesPriceCD} = -918,144.700 + (23.470 \times \text{MedianHomeownerIncome})
\]
The regression model explains 26% of the variation in average sales prices (\( R^2 = 0.260 \)). Median homeowner income has a significant positive effect (\( \beta = 23.470, p < 0.01 \)), suggesting that a $1,000 increase in homeowner income corresponds to an increase of $23,470 in average sales prices. The constant term, \( -918,144.700 \), represents the baseline sales price when all predictors are zero.





Important Conclusions
---
