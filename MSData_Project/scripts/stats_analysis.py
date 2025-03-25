import pandas as pd
from sklearn import linear_model
import statsmodels.formula.api as smf
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from itertools import combinations

#1. Analyze walking speed:
   #- Multiple regression with education and age
   #- Account for repeated measures
   #- Test for significant trends

df = pd.read_csv("ms_data.csv")

education_coded = {'High School': 1, 'Some College':2, 'Bachelors':3, 'Graduate':4} #encode education level into numeric values
df['education_level_coded'] = df['education_level'].map(education_coded) #new column with numeric values

#mixed effects model analyzing walking speed with education level and age category
model = smf.mixedlm(
    "walking_speed ~ education_level_coded + age_category",
    df,
    groups = df['patient_id'] #handles repeated measures
)

result = model.fit()

print(result.summary())

#middle aged people are walking 0.751 m/s faster than old people (p <0.001)
#young adults walk 1.070 m/s faster on average than old adults (p < 0.0001
#as education level increases, so does walking speed (p < 0.0001)

#2. Analyze costs:
   #- Simple analysis of insurance type effect
   #- Box plots and basic statistics
   #- Calculate effect sizes
sns.boxplot(x='insurance_type', y='visit_cost', data=df) #boxplots of visit costs
sns.set_theme(style = 'whitegrid')
plt.savefig('boxplot.png')

plt.hist('visit_cost', data=df, bins=30) #normal distribution of visit costs across insurance types
plt.savefig('visit_cost_hist.png')

#basic stats
grouped_data = df.groupby('insurance_type')['visit_cost']
summary_stats = grouped_data.agg(['mean', 'median', 'std']) #summary stats of choice

#One way ANOVA test to test effect of insurance type on visit costs - compares means between categorical groups
anova_test = f_oneway(*[group for _, group in grouped_data])
print(f"ANOVA test: F = {anova_test.statistic:.2f}, p = {anova_test.pvalue:.4f}") #p-val of 0.000 shows significant differences in the means of vists costs across insurance types

#effect sizes using cohens_d calculations
def cohen_d(x, y):
    diff_mean = np.mean(x) - np.mean(y) #difference in means 
    pooled_sd = np.sqrt(((len(x) - 1) * np.var(x) + (len(y) - 1) * np.var(y)) / (len(x) + len(y) - 2)) #pooled sd calculations
    return diff_mean / pooled_sd

insurance_types = df['insurance_type'].unique()
pairs = list(combinations(insurance_types, 2)) #all combinations of different pairs of insurance types


effect_sizes = {}
for pair in pairs: #store pairwise comparisons between insurance types in a dictionary
    group1 = df[df['insurance_type'] == pair[0]]['visit_cost']
    group2 = df[df['insurance_type'] == pair[1]]['visit_cost']
    effect_sizes[f"{pair[0]} vs {pair[1]}"] = cohen_d(group1, group2)

print("\nEffect Sizes:")
for comparison, es in effect_sizes.items():
    print(f"{comparison}: {es:.2f}") #effect sizes are very large, which makes sense given that costs are highly different between plans (~50 vs ~100 vs ~150)

#3. Advanced analysis:
   #- Education age interaction effects on walking speed
   #- Control for relevant confounders
   #- Report key statistics and p-values

df['education_level_coded'] = df['education_level'].astype('category').cat.codes #encoding education level numerically
df['age_category_coded'] = df['age_category'].astype('category').cat.codes #encoding age categories numerically

age_dict = dict(zip(df['age_category'], df['age_category_coded'])) #shows that elderly = 0, middle aged = 1, young adult = 2

model = smf.mixedlm(
    formula = "walking_speed ~ education_level_coded * age_category_coded + visit_cost + insurance_type",
    data = df,
    groups = 'patient_id'
)

result = model.fit()
print(result.summary())

#walking speed for reference group is 3.977 m/s (significant (p < 0.001))
#compared to basic insurance, platinum or premium insurance does NOT significantly change walking speed (p = 0.814 and p = 0.728)
#as education increases, walking speed decreases by 0.245 m/s (p < 0.001)
#as age category value increases (people get younger), walking speed increases by 0.390 m/s (p < 0.001)
#effect of education level on walking speed doesn't significantly differ by age category (p = 0.531)
#visit cost does not significantly affect walking speed (p = 0.774)
#there is random variance of individual patient id on walking speed (coeff = 0.216)
