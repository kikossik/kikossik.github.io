---
title: "New York City Rental Affordability Analysis"
excerpt: "<span>- Geospatial Analysis, Statistical Analysis, Data Visualization</span><br/>- R, ggplot2, sf, mapview, Regression Analysis<br/><br/>Conducted a comprehensive geospatial analysis of New York City rental affordability by comparing AMI-based metrics with localized affordability tailored to median renter incomes. Identified 29 districts (49%) with discrepancies, revealing an average affordability gap of $15,752.38. Income is the primary driver of rent prices, while sales prices were influenced by broader factors. Developed interactive maps to visualize disparities, highlighting vulnerabilities in lower-income districts like the Bronx and Brooklyn.<br/><br/><img src='/images/heatmap.png'>"
collection: portfolio
---

Key accomplishments:
---
- Compared Area Median Income (AMI)-based affordability metrics for <a href="https://www.nyc.gov/site/planning/plans/mih/mandatory-inclusionary-housing.page" target="_blank">Mandatory Inclusionary Housing (MIH)</a> with a custom, income-specific approach across all 59 Community Districts of NYC.
- Identified that **29** districts **(49%)** show affordability differences between metrics, with an average gap of **$15,752.38**, highlighting significant flaws of MIH policy.
- Demonstrated that Median Renter Income explains **91%** of rent price variation, while sales prices are influenced by broader factors, with a weaker explanatory power.
- Developed interactive maps and plots to highlight affordability misalignments, emphasizing differences in economically vulnerable regions like the Bronx and Brooklyn.
- Suggested a better approach for calculating affordability based on local median renter incomes tailored to the economic realities of individual Community Districts.  

---> R Notebook - <a href="https://nbviewer.org/github/kikossik/kikossik.github.io/blob/master/files/notebooks/nyc_affordability.html" target="_blank">NBViewer</a>

Key Goals and Project Description
---
This project analyzes housing affordability in NYC using data on renter incomes, rental prices, and zoning policies. It evaluates how well AMI-based metrics reflect renters' challenges and compares metrics to identify discrepancies, spatial patterns, and the effectiveness of policies like MIH.

Brief Preliminaries to The Problem
---
**MIH Affordability**   
Mandatory Inclusionary Housing (MIH) is a zoning tool in NYC requiring developers to include affordable units in residential projects. However, affordability is based on fixed percentages of the Area Median Income (AMI), which often doesn't reflect local residents' financial realities.  
**Custom Affordability Metric**  
This project compares AMI-based metrics with those tailored to median renter incomes in community districts, highlighting gaps and evaluating alignment with actual economic conditions. Formulas are attached at the end of the project.   
**Why Calculate Affordability This Way?**  
The "one-third of income" rule is a practical benchmark for housing affordability, but AMI-based thresholds can overgeneralize in diverse areas like NYC. District-specific metrics, reflecting local renter incomes, provide a clearer picture of affordability challenges.  

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
  background: hsla(178, 60%, 55%, 0.3);
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
```
MedianRentPrice = 0.014 × MedianIncomeForRenters - 0.00001 × AverageSalesPriceCD + 748.599
```
Median Renter Income directly drives rent prices and influences affordability, while Average Sales Prices per CD have a more indirect effect. This underscores the need for income-focused housing policies to tackle affordability challenges effectively. By minimizing predictors, the goal was to identiy the key factors shaping rent prices.  

**Understanding drivers of Sales Prices**  
This analysis examines the relationship between Average Sales Price per Community District (CD) and its predictors: Median Homeowner Income and Median Rent Price.

<img src='/images/scat2.png'>  
- The scatterplots for the drivers of Sales Prices are weaker than for Rent Prices. 
- Still, the scatterplot shows a positive linear relationship between Median Homeowner Income and Average Sales Price per CD, and a weaker but still positive relationship is observed between Median Rent Price and Average Sales Price per CD as well.  

<img src='/images/reg2.PNG' style="display: block; margin: 0 auto;">  
```
AverageSalesPriceCD = 23.470 × MedianHomeownerIncome - 918,144.700
```

Interpreting Regression Results
---
- **Sales Reg:** **Median Homeowner Income** significantly predicts **Average Sales Price per CD**, with higher homeowner incomes correlating to higher sales prices.
  - **R²: 0.260** → Only 26% of the variability in sales prices is explained, indicating that sales prices depend on a broader range of factors.
- **Rent Reg:** **Median Renter Income** shows a much stronger relationship with **Median Rent Prices**:
  - **R²: 0.910** → 91% of rent price variability is explained by renter incomes.
  - The **standard error** for **Median Homeowner Income** in the sales model (0.166) is nearly **8,000** times larger than the **standard error** for **Median Renter Income** in the rent model (0.00002), highlighting the tighter link between renter incomes and rents.
- Both models show significant predictors (*p < 0.01*), but the **Rent Reg** model’s higher R² and lower residual error indicate that rent prices are more directly and reliably determined by incomes compared to **Sales Reg** sales prices, which are influenced by multiple factors. 

Affordability Analysis
---
Before we continue, I want to remind you what the **goal** of this project was - understanding housing affordability in New York City by **comparing Mandatory Inclusionary Housing (MIH) standards**, which rely on fixed percentages of the Area Median Income (AMI), **with custom metrics tailored to district-specific renter incomes**.  

**- MIH Affordability:**  
<br/>
<div style="text-align: center; font-size: 80%;">
<img src="https://latex.codecogs.com/svg.latex?\Large\text{AMI\ Affordability}=\frac{\text{AMI}}{3}" title="\Large \text{AMI Affordability}=\frac{\text{AMI}}{3}" />
</div>  
<br/>
MIH uses the Area Median Income (AMI) to determine the maximum affordable annual rent.

**- Custom Affordability (Our Approach):**  
<br/>
<div style="text-align: center; font-size: 80%;">
<img src="https://latex.codecogs.com/svg.latex?\Large\text{Our\ Affordability}=\frac{\text{Median\ Income\ for\ Renters\ per\ CD}}{3}" title="\Large \text{Our Affordability}=\frac{\text{Median Income for Renters per CD}}{3}" />
</div>  
<br/>
This method uses the district-specific median income of renters instead of AMI.

**- Annualized Rent:**  
<br/>
<div style="text-align: center; font-size: 80%;">
<img src="https://latex.codecogs.com/svg.latex?\Large\text{Median\ Annual\ Rent}=\text{Median\ Rent\ Price}\times12" title="\Large \text{Median Annual Rent}=\text{Median Rent Price}\times12" />
</div>  
<br/>
This converts monthly rent prices to annual values to compare with the affordability thresholds.

**- Binary Affordability Dummy Variables:**  

<br/>
<div style="text-align: center; font-size: 80%;">
<img src="https://latex.codecogs.com/svg.latex?\Large\text{AMIDum}=\begin{cases}1&\text{if}\ \text{AMI\ Affordability}\geq\text{Median\ Annual\ Rent}\\0&\text{otherwise}\end{cases}" title="\Large \text{AMIDum}=\begin{cases}1&\text{if}\ \text{AMI Affordability}\geq\text{Median Annual Rent}\\0&\text{otherwise}\end{cases}" />
</div>
<br/>

<br/>
<div style="text-align: center; font-size: 80%;">
<img src="https://latex.codecogs.com/svg.latex?\Large\text{OurAMIDum}=\begin{cases}1&\text{if}\ \text{Our\ Affordability}\geq\text{Median\ Annual\ Rent}\\0&\text{otherwise}\end{cases}" title="\Large \text{OurAMIDum}=\begin{cases}1&\text{if}\ \text{Our Affordability}\geq\text{Median Annual Rent}\\0&\text{otherwise}\end{cases}" />
</div>
<br/>

Now let's take a look if the housing is actually affordable.  

<img src='/images/diff.png'>  

This map compares NYC Community Districts' housing affordability using AMI-based and the custom metrics. Red districts show divergence between the measures, while blue indicates alignment.

- **Concentration of Differences in Lower-Income Areas:**  
Red areas, mostly in the Bronx and Brooklyn, highlight gaps between AMI-based and renter-based affordability, showing AMI often overestimates affordability.
- **Alignment in Higher-Income Areas:**  
Blue areas, common in Manhattan and affluent parts of Queens, show better alignment as income differences are smaller.
  
**Out of 59 Community Districts, 29 districts (49%) show differences between the AMI-based and custom affordability metrics.**  
**The average affordability gap is $15,752.38.**  

This analysis exposes the systematic flaws of standardized metrics like AMI, especially in lower-income neighborhoods targeted by MIH policy. By using a custom measure based on median renter income, the study discovers major gaps in how affordability is calculated. These findings highlight the need for more tailored, district-specific policies to better address affordability issues in NYC's most vulnerable areas.  

---> R Notebook - <a href="https://nbviewer.org/github/kikossik/kikossik.github.io/blob/master/files/notebooks/nyc_affordability.html" target="_blank">NBViewer</a>
