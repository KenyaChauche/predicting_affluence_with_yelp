# Predicting Neighborhood Affluence with Yelp Ratings
​
## Problem Statement 
​
Income and home value are simple and relatively static ways to measure a neighborhood's affluence. This project aims to identify a new way of measuring affluence in a community, called "active affluence," and focuses on Seattle, specifically. In this way we use Yelp data to determine the number of businesses of various price tiers present, and investigated a possible relationship between more typical measures of affluence (home value, income, rent rate) and the proportion of businesses present within each Yelp price tier.  
​
## Data Gathering
​
We gathered our housing, rental, and income data from the Seattle City Data Portal. This portal, blessedly, had an API that would allow us to gather our data with minimal webscraping. This data was able to be split into neigborhoods, and the Seattle neighborhood delineations matched the delineations Yelp uses for its site. We gathered Yelp restaurant price ratings from Yelp.com with their API as well.
​
## Methods
​
In order to take as local an approach as possible, we attempted to correlate Yelp restaurant pricing with Seattle neighborhoods, which are significantly smaller areas than zip code or the city as a whole. We were able to find median home values, median rental rates, and median income for each neighborhood. After obtaining our Yelp data, we created a dataframe that contained nearly 1,000 random points throughout the city with their latitude and longitude, and then the proportion of restaurants with 1, 2, 3, and 4 price-point ratings by Yelp within both a half mile radius and a mile radius. We then looked for correlations with neighborhood data.
​
To attempt to get better scores, we attempted a second method which included using points randomly generated throughout the city, and running the Yelp API on the latitude and longitude of those points. The hope here is to get more restaurants, since we initially only got 960 out of roughly 3350 for the city. We then looked at both the number and proportion of restaurants with 1, 2, 3, and 4 price-point ratings by Yelp within a .5 and 1 mile radius. We did get more restaurants by doing this, and our model performance metrics improved somewhat.

## Modeling
​
We ran models with the input being proportion of Yelp restaurant 1, 2, 3, and 4 price-tiers within a half-mile and a mile radius. The inputs were run three times, once against neighborhood median home values, once against neighborhood median rental rates, and finally against neighborhood median income. For median home values and median rental rates, we utililzed Linear Regression, Adaboost, LASSO, KNN, and Decision Tree models. For the median income of neighborhoods we utilized the same models plus Ridge and Bagged Decision Tree models.
​
## Results
​
Ultimately, most of the models were overfit.  There were some instances that returned R-squared scores in the upper 40s and low 50s percentage that weren't overfit, however this range is still not satisfactory for correlating Yelp price ratings to neighborhood affluence. These results indicated to us that there is not a significant or strong correlation between Yelp restaurant price tier distribution of a neighborhood and neighborhood median home value, income or rent. 
​
## Conclusion
​
We were not able to find significant correlations between neighborhood affluence and Yelp restaurant price ratings. This does not rule out Yelp data as a new measure of neigborhood affluence. While home value, rent, and income represent static forms of affluence, the businesses present in a community and the average cost of frequenting them can still be a good measure of a community's active affluence. While home value can be a good indicator of what it costs to move into a certain neighborhood, the distribution of restaurant price tier can be a good indicator of what it costs to be an active member of the social community. 

The result of this project opens up new questions: is the lack of correlation an indication of the inefficacy of Yelp data metrics in predicting affluence? Are the static measures of affluence not accurate reflections of the neighborhoods' communities? Are Yelp metrics not accurate reflections of the neighborhoods' communities? Are these metrics both still effective, but convey very different things? 

Some challenges encountered in this project was the limited availability of information with Yelp's API. Of the 3350 restaurants in Seattle, on our initial usage of the API we only got 960. This was well below what we preferred for accurate results in this project. Additionally, the neighborhood data we obtained only had median home value, income, and rental rates for the entire neighborhood. We recognize that there are vast fluctuations of each of these within each neighborhood, and being able to see where these fluctuations converge within each neighborhood would allow for a more accurate representation of a neighborhood's affluence distribution. We recognize the possibility of this is limited, for data management, ethical, and privacy related reasons.

### Data Sources
​
Housing, Rental, and Income data was gathered with the [City of Seattle's Open Data Portal] (https://data.seattle.gov/) 

Yelp data metrics were gathered with [Yelp's API] (https://www.yelp.com/developers/documentation/v3/get_started)

## Credits
This project was a collaboration between myself, [Richard Samuelson] (https://github.com/samuelsonric), and [Stephen Schott] (https://github.com/stephenschott). 
​
## Data Dictionary
​
|Feature|Type|Dataset|Description|
|----|----|----|----|
|index|int|df|numbered index of the rows| 
|latitude|float|df|the latitude of the point|
|longitude|float|df|the longitude of the point| 
|neighborhood|object|df|the neighborhood in which the point sits|
|.5mi 1 dollar|float|df|percentage of 1 tier price rating within .5 mile radius of point|
|1.0mi 1 dollar|float|df|percentage of 1 tier price rating within 1 mile radius of point|
|0.5mi 2 dollar|float|df|percentage of 2 tier price rating within .5 mile radius of point|
|1.0mi 2 dollar|float|df|percentage of 2 tier price rating within 1 mile radius of point|
|0.5mi 3 dollar|float|df|percentage of 3 tier price rating within .5 mile radius of point|
|1.0mi 3 dollar|float|df|percentage of 3 tier price rating within 1 mile radius of point|
|0.5mi 4 dollar|float|df|percentage of 4 tier price rating within .5 mile radius of point|
|1.0mi 4 dollar|float|df|percentage of 4 tier price rating within 1 mile radius of point|
|median income|int|df|median income of neighborhood in which the point sits|
|median rent|int|df|median rent cost of neighborhood in which the point sits|
|median home value|int|df|median home value of neighborhood in which the point sits|
|Unnamed: 0|int|df2|old index|
|Unnamed: 0.1|int|df2|old index|
|Unnamed: 0.1.1|float|df2|longitude of the point|
|Unnamed: 1|float|df2|latitude of the point|
|1|int|df2|count of 1 price point restaurants in the 1 mile radius of the point|
|2|int|df2|count of 2 price point restaurants in the 1 mile radius of the point|
|3|int|df2|count of 3 price point restaurants in the 1 mile radius of the point|
|4|int|df2|count of 4 price point restaurants in the 1 mile radius of the point|
|GEN_ALIAS|obj|df2|neighborhood that the point falls in|
|1p|float|df2|proportion of 1 price point restuarants in the 1 mile radius of the point|
|2p|float|df2|proportion of 2 price point restuarants in the 1 mile radius of the point|
|3p|float|df2|proportion of 3 price point restuarants in the 1 mile radius of the point|
|4p|float|df2|proportion of 4 price point restuarants in the 1 mile radius of the point|
|MEDIAN_GROSS_RENT|int|df2|median gross rent of the neighborhood in which the point lies|
|HU_VALUE_MEDIAN_DOLLARS|int|df2|median home value of the neighborhood in which the point lies|
|MEDIAN_HH_INC_PAST_12MO_DOLLAR|int|df2|median household income of the neighborhood in which the point lies|
|median_rent|obj|seattle_rent|median rent price for neighborhood|
|median_home_value|int|seattle_rent|median home value for neighborhood|
|median_income|int|seattle_rent|median income for neighborhood|
|1 dollar|int|seattle_rent|proportion of 1 price point restuarants in the neighborhood|
|2 dollar|float|seattle_rent|proportion of 2 price point restuarants in the neighborhood|
|3 dollar|float|seattle_rent|proportion of 3 price point restuarants in the neighborhood|
|4 dollar|float|seattle_rent|proportion of 4 price point restuarants in the neighborhood|
||||
 