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

Data Description
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
  <span class="highlighted">property sales density</span>, Mandatory Inclusionary 
  <span class="highlighted">Housing (MIH) zones</span>, 
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
Before investigating the drivers for rent and sales prices, let's take a moment and look at this cool boxplot. This boxplot examines the distribution of median rent prices across various property types grouped into categories such as Residential, Condos & Co-ops, Commercial, Public & Cultural, and Other. I am not going to emphasize on this part too much, but some quick observations:  
- This plot illustrates the significant variation in rental affordability across different property types.  
- While residential properties are generally more affordable, the variability in condos and commercial properties highlights the diversity of NYC's rental market.  
- These results emphasize the importance of considering property types when assessing affordability or policy impacts, as broad averages can obscure critical disparities between groups.  

**Understanding drivers of Rent Prices**  
This analysis examines the relationship between median rent prices, median income for renters, and average sales price per community district (CD).  
<img src='/images/scat1.png'>  
- The scatterplot shows a very strong positive correlation between Median Rent Price and Median Income for Renters.
- It also reveals a weaker and more dispersed relationship between Median Rent Price and Average Sales Price per CD. While there is a general upward trend, the variability in rent prices suggests that other factors may contribute to rental pricing beyond sales trends at the district level.  

<img src="/images/reg1.PNG" style="display: block; margin: 0 auto;"> 
The big picture emphasizes that Median Renter Income is the key driver of rent prices, directly influencing rental affordability, while Average Sales Prices per CD exhibit a more indirect impact. This highlights the importance of prioritizing income-focused housing policies to address affordability challenges effectively. For this project, we focused on minimizing predictors to identify the major factors driving rent prices, so this is definitely what we want to see.  

**Understanding drivers of Sales Prices**  
This analysis examines the relationship between Average Sales Price per Community District (CD) and its predictors: Median Homeowner Income and Median Rent Price.
<img src='/images/scat2.png'>  
- The scatterplots for the drivers of Sales Prices are weaker than for Rent Prices. 
- Still, the scatterplot shows a positive linear relationship between Median Homeowner Income and Average Sales Price per CD, and a weaker but still positive relationship is observed between Median Rent Price and Average Sales Price per CD as well.  

<img src='/images/reg2.PNG'>  
The regression analysis highlights that Median Homeowner Income significantly predicts Average Sales Price per CD, indicating that higher homeowner incomes correspond to higher sales prices. However, the model's R² of 0.260 shows that only 26% of the variability in sales prices is explained, suggesting sales prices are influenced by a broader set of factors beyond homeowner income.  
In contrast, the drivers of Median Rent Prices, such as Median Income for Renters, exhibit a much stronger relationship, with an R² of 0.910 in their model, indicating that renter incomes account for 91% of the variability in rents. Additionally, the standard error of Median Homeowner Income in the sales regression (0.166) is nearly 8,000 times larger than the standard error of Median Income for Renters in the rent regression (0.00002), reflecting the tighter relationship between renter incomes and rent prices.  
While both models show significant predictors (p < 0.01), the rent model's much higher R² and lower residual error suggest that rent prices are more directly and reliably determined by income levels compared to sales prices, which are influenced by a broader set of factors.

What We Have Been Waiting For
---
