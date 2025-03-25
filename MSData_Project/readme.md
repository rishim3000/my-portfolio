# Multiple Sclerosis Analysis - Rishi Mukundan

## Part 1: Data Preparation with Command-Line Tools

File name: `prepare.sh`

1. Insurance types labeled as 'Basic', 'Premium', and 'Platinum'
2. 15408 rows in the processed csv file: ms_data.csv

## Part 2: Data Analysis with Python

File name: `analyze_visits.py`

1. Visit cost set based on insurance type (Basic = 150, Premium = 100, Platinum = 50)
2. Anyone under 25 classified as young adult, anyone between 25 and 50 is middle aged, and anyone above 50 is classified as elderly.
3. Summary statistics
    -Mean walking speed by education level:
        -Bachelors: 4.0866
        -Graduate: 4.422
        -High School: 3.277
        -Some College: 3.644

    -Mean costs by insurance type:
        -Basic: $149.93
        -Premium: $100.07
        -Platinum: $50.05
        
    -Age effects on walking speed:
        -Young adult: 4.74
        -Middle aged: 4.26
        -Elderly: 3.44    

## Part 3: Statistical Analysis

File name: `stats_analysis.py`

1. Mixed effects model analyzing walking speed with education level and age category
    -Middle aged people are walking 0.751 m/s faster than old people (p <0.001)
    -Young adults walk 1.070 m/s faster on average than old adults (p < 0.0001)
    -As education level increases, so does walking speed (p < 0.0001)

2. Analyze costs: Simple analysis of insurance type effect, box plots and basic statistics, and effect sizes
    -Boxplot and histogram show normal distribution of insurance, across all 3 types
    -One way ANOVA test shows p-val of 0.000, indicating significant differences in the means of vists costs across insurance types
    -Effect sizes are very large, which makes sense given that costs are highly different between plans (~50 vs ~100 vs ~150)

3. Advanced analysis: Mixed linear model analyzing education-age interaction effects on walking speed
    -Walking speed for reference group is 3.977 m/s (p < 0.001)
    -Compared to basic insurance, platinum or premium insurance does NOT significantly change walking speed (p = 0.814 and p = 0.728)
    -As education increases, walking speed decreases by 0.245 m/s (p < 0.001)   
    -As age category value increases (people get younger), walking speed increases by 0.390 m/s (p < 0.001)
    -Effect of education level on walking speed doesn't significantly differ by age category (p = 0.531)
    -Visit cost does not significantly affect walking speed (p = 0.774)
    -There is random variance of individual patient id on walking speed (coeff = 0.216)

## Part 4: Data Visualization

File name: `visualize.ipynb`

Scatter plot: ![alt text](Images/Age_vs_WS_scatter.png)

Boxplot: ![alt text](Images/WS_by_Edu_Boxplot.png)

Education-age interaction: ![alt text](Images/Edu_Age_catplot.png)

Bar plot of mean costs by insurance type: ![alt text](Images/Mean_Cost_Insurance.png)

Box plot of cost distribution: ![alt text](Images/Visit_Cost_Insurance_boxplot.png)

Pairplot of Key Variables: ![alt text](Images/pairplot.png)

Faceted plots by education level: ![alt text](Images/Facet_Edu.png)

Faceted plots by insurance type: ![alt text](Images/Insurance_Facet.png)

Time trend data: ![alt text](Images/WS_Edu_Time.png)