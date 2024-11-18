---
title: "New York City Rental Affordability Analysis"
excerpt: "<span>- Distributed Database Management System, Data Scraping, Custom Hash Partitioning</span><br/>- Python, Django, MySQL, Selenium WebDriver, BeautifulSoup<br/><br/>Developed a Django-based Distributed Database Management System for job postings from scratch, utilizing a custom hash function to partition data across 3 MySQL databases. The dataset was obtained by scraping LinkedIn Jobs using Selenium WebDriver for automated navigation and BeautifulSoup for HTML parsing.<br/><img src='/images/mihnyc.PNG'>"
collection: portfolio
---

Key accomplishments:
---
- nlah nlah
- more blah blah

Initial Hypotheses
---
Started our research assuming that Residential Sales prices are higher when nearby areas are commercially zoned.  
  
Also hypothesized that real estate sales with a high volume of nearby sales would be at a higher price, indicating that the market is extremely attractive.  
  
Additionally, hypothesized that housing price would be higher per unit for single family homes than multi-family homes.  

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
The heatmap reveals that Manhattan is the epicenter of property sales. Peripheral areas in Brooklyn and Queens also show high activity, possibly due to spillover effects as people and businesses move out of Manhattan to relatively more affordable areas.  
MIH zones often overlap with areas of high sales density, however, most of the MIH zones are designed in poor neighborhoods.  
With commercial zones, it is evident that they are primarily prominent in areas with the highest Sales, such as Manhattan.  

**NYC Housing Affordability**  
- **Rental Affordability at 80% AMI**  
<img src='/images/rent_afford_80_ami.png'>  

- **Median Income for Renters**  
<img src='/images/median_income_rent.png'> 

- **Median Rent**  
<img src='/images/median_rent.png'> 

**Takeaway**  
The maps highlight a clear spatial correlation: areas with higher median incomes (Map 2) also have higher median rents (Map 3). Manhattan and parts of Brooklyn dominate these categories, suggesting significant economic disparities between boroughs.  
Rental affordability (Map 1) is low in high-income, high-rent areas, emphasizing the lack of affordable housing in wealthier districts. Conversely, outer boroughs like the Bronx and Staten Island, with lower incomes and rents, provide better affordability.  
The maps collectively underscore economic segregation in NYC. Wealthier populations and high rents are clustered in central and gentrified areas, while more affordable rents and lower incomes are prevalent in peripheral districts.