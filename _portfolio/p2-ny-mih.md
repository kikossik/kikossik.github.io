---
title: "New York City Rental Affordability Analysis"
excerpt: "<span>- Geospatial Analysis, Statistical Analysis, Data Visualization</span><br/>- R, ggplot2, sf, mapview, Regression Analysis<br/><br/>Conducted a comprehensive geospatial analysis of New York City rental affordability by comparing AMI-based metrics with localized affordability tailored to median renter incomes. Identified **29 districts (49%)** with discrepancies, revealing an **average affordability gap of $15,752.38**. Regression analysis achieved **R²: 0.910**, showing income as the primary driver of rent prices, while sales prices were influenced by broader factors (**R²: 0.260**). Developed interactive maps to visualize disparities, highlighting vulnerabilities in lower-income districts like the Bronx and Brooklyn.<br/><img src='/images/heatmap.png'>"
collection: portfolio
---

Key accomplishments:
---
- Compared Area Median Income (AMI)-based affordability metrics for <a href="https://www.nyc.gov/site/planning/plans/mih/mandatory-inclusionary-housing.page" target="_blank">Mandatory Inclusionary Housing (MIH)</a> with a custom, income-specific approach across all 59 Community Districts of NYC.
- Identified that **29** districts **(49%)** show affordability differences between metrics, with an average gap of **$15,752.38**, highlighting significant flaws of MIH policy.
- Demonstrated that Median Renter Income explains **91%** of rent price variation *(R²: 0.910)*, while sales prices are influenced by broader factors, with a weaker explanatory power *(R²: 0.260)*.
- Developed interactive maps and plots to highlight affordability misalignments, emphasizing differences in economically vulnerable regions like the Bronx and Brooklyn.
- Provided insights on the limitations of AMI-based policies, while suggesting a better approach of calculating affordability based on local median renter incomes tailored to the economic realities of individual Community Districts.

Key Goals and Project Description
---
This project focuses on analyzing housing affordability in New York City using detailed datasets on renter incomes, rental prices, and zoning policies. The goal is to evaluate how well current metrics, such as Area Median Income (AMI) affordability, reflect the real affordability challenges faced by renters in different community districts.  
By computing and comparing affordability metrics, we aim to identify discrepancies, understand spatial affordability patterns, and provide insights into the effectiveness of existing housing policies, including Mandatory Inclusionary Housing (MIH) programs.

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
- <a href="https://www.nyc.gov/site/finance/property/property-rolling-sales-data.page" target="_blank">**NYC Sales Data**</a>  
Contains records of property sales in NYC, including variables such as price, building category, and geographic coordinates.
- <a href="https://data.cityofnewyork.us/City-Government/New-York-Zones/8nxe-banu" target="_blank">**Commercial Zones**</a>  
Spatial polygons representing commercial zones in NYC.
- <a href="https://data.cityofnewyork.us/Housing-Development/Mandatory-Inclusionary-Housing-MIH-/bw8v-wzdr" target="_blank">**MIH Zones**</a>  
Inclusionary housing zones under Mandatory Inclusionary Housing (MIH) regulations.
- <a href="https://data.cityofnewyork.us/City-Government/Community-Districts/yfnk-k7r4" target="_blank">**Community Districts**</a>  
Community Districts shapefiles with demographic and economic attributes, such as rental affordability and median income for renters.

Visualizing the Data
---
**NYC Housing Dynamics**  

<p>This map visualizes the spatial patterns of <span class="highlight-red">property sales density</span>, <span class="highlight-blue">Mandatory Inclusionary Housing (MIH) zones</span>, and <span class="highlight-yellow">commercial zoning areas</span> in New York City.</p>

<svg style="position: absolute; width: 0; height: 0;" xmlns="http://www.w3.org/2000/svg">
  <filter id="wavyHighlight" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" result="noise" seed="1" />
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="7" />
  </filter>
</svg>

<style>
.highlight-red, .highlight-blue, .highlight-yellow {
  position: relative;
  display: inline-block;  /* Add this */
}

.highlight-red::before, .highlight-blue::before, .highlight-yellow::before {
  content: '';
  position: absolute;
  left: -0.2em;  /* Adjust padding */
  right: -0.2em;
  top: -0.2em;
  bottom: -0.2em;
  z-index: -1;
  filter: url(#wavyHighlight);
}

.highlight-red::before {
  background: hsla(0, 70%, 50%, 0.3);
}

.highlight-blue::before {
  background: hsla(240, 70%, 50%, 0.3);
}

.highlight-yellow::before {
  background: hsla(60, 70%, 50%, 0.3);
}
</style>

<img src='/images/heatmap.png'>  
- The heatmap reveals that Manhattan is the epicenter of property sales. Peripheral areas in Brooklyn and Queens also show high activity, possibly due to spillover effects as people and businesses move out of Manhattan to relatively more affordable areas.  
- MIH zones often overlap with areas of high sales density, however, most of the MIH zones are designed in poor neighborhoods.  
- With commercial zones, it is evident that they are prominent in areas with the highest sales, such as Manhattan.  

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
<code>**MedianRentPrice** = 0.014 × MedianIncomeForRenters - 0.00001 × AverageSalesPriceCD + 748.599</code>
The big picture emphasizes that Median Renter Income is the key driver of rent prices, directly influencing rental affordability, while Average Sales Prices per CD exhibit a more indirect impact. This highlights the importance of prioritizing income-focused housing policies to address affordability challenges effectively. For this project, we focused on minimizing predictors to identify the major factors driving rent prices, so this is definitely what we want to see.  

**Understanding drivers of Sales Prices**  
This analysis examines the relationship between Average Sales Price per Community District (CD) and its predictors: Median Homeowner Income and Median Rent Price.
<img src='/images/scat2.png'>  
- The scatterplots for the drivers of Sales Prices are weaker than for Rent Prices. 
- Still, the scatterplot shows a positive linear relationship between Median Homeowner Income and Average Sales Price per CD, and a weaker but still positive relationship is observed between Median Rent Price and Average Sales Price per CD as well.  

<img src='/images/reg2.PNG' style="display: block; margin: 0 auto;">  
<code>**AverageSalesPriceCD** = 23.470 × MedianHomeownerIncome - 918,144.700  </code>
The regression analysis highlights that Median Homeowner Income significantly predicts Average Sales Price per CD, indicating that higher homeowner incomes correspond to higher sales prices. However, the model's **R²** of *0.260* shows that only *26%* of the variability in sales prices is explained, suggesting sales prices are influenced by a broader set of factors beyond homeowner income.  

In contrast, the drivers of Median Rent Prices, such as Median Income for Renters, exhibit a much stronger relationship, with an **R²** of *0.910* in their model, indicating that renter incomes account for *91%* of the variability in rents. Additionally, the **standard error** of Median Homeowner Income in the sales regression (*0.166*) is nearly **8,000** times larger than the **standard error** of Median Income for Renters in the rent regression (*0.00002*), reflecting the tighter relationship between renter incomes and rent prices.  

While both models show significant predictors *(p < 0.01)*, the rent model's much higher R² and lower residual error suggest that rent prices are more directly and reliably determined by income levels compared to sales prices, which are influenced by a broader set of factors.

What We Have Been Waiting For
---
Before we continue, I want to remind you what the **goal** of this project was - understanding housing affordability in New York City by **comparing Mandatory Inclusionary Housing (MIH) standards**, which rely on fixed percentages of the Area Median Income (AMI), **with custom metrics tailored to district-specific renter incomes**.  
<img src='/images/diff.png'>  
This map visualizes differences in housing affordability across New York City's Community Districts by comparing affordability under the AMI-based metric and our custom metric - "one-third of income" per CD. Districts shaded red indicate areas where the two affordability measures diverge ("TRUE"), while blue districts show alignment between the metrics ("FALSE").  

- Concentration of Differences in Lower-Income Areas:  
The red areas are mostly found in lower-income neighborhoods, especially in outer boroughs like the Bronx and parts of Brooklyn. In these areas, there is often a big gap between affordability based on Area Median Income (AMI) and what renters can actually afford based on their incomes. This shows that AMI-based measures may overestimate affordability in these regions, as they don’t match the real financial situations of renters.
- Alignment in Higher-Income Areas:  
Blue areas, which show agreement between the metrics, are more common in higher-income neighborhoods, especially in Manhattan and wealthy parts of Queens. Here, AMI-based affordability aligns better with local economic conditions because income differences are smaller.
  
**Out of 59 Community Districts, 29 districts (49%) show differences between the AMI-based and custom affordability metrics.**  
**The average affordability gap is $15,752.38.**  

This analysis exposes the systematic flaws of standardized metrics like AMI, especially in lower-income neighborhoods targeted by MIH policy. By using a custom measure based on median renter income, the study discovers major gaps in how affordability is calculated. These findings highlight the need for more tailored, district-specific policies to better address affordability issues in NYC's most vulnerable areas.