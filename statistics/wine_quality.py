#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm


# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())

# Display descriptive statistics for all variables
print(wine.describe())

# Identify unique values
print(sorted(wine.quality.unique()))

# Calculate value frequencies
print(wine.quality.value_counts())

# Display descriptive statistics for quality by wine type
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

# Calculate correlation matrix for all variables
print(wine.corr())

# Look at relationship between pairs of variables
# Take a "small" sample of red and white wines for plotting
def take_sample(data_frame, replace=False, n=200):
	return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]	
reds = wine.loc[wine['type']=='red', :]
whites = wine.loc[wine['type']=='white', :]
reds_sample = take_sample(wine.loc[wine['type']=='red', :])
whites_sample = take_sample(wine.loc[wine['type']=='white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1.,0.)

reds_sample = reds.ix[np.random.choice(reds.index, 100)]
whites_sample = whites.ix[np.random.choice(whites.index, 100)]
wine_sample = pd.concat([reds_sample, whites_sample], ignore_index=True)

print(wine['in_sample'])
print(pd.crosstab(wine.in_sample, wine.type, margins=True))

sns.set_style("dark")
sns.set_style("darkgrid", {"legend.scatterpoints": 0})
pg = sns.PairGrid(wine_sample, hue="type", hue_order=["red", "white"], \
palette=dict(red="red", white="white"), hue_kws={"marker": ["o", "s"]}, vars=['quality', 'alcohol', 'residual_sugar'])
pg.x = wine_sample.ix[wine_sample['type']=='red', 'quality']
pg = pg.map_diag(plt.hist)
pg.x = wine_sample.ix[wine_sample['type']=='white', 'quality']
pg = pg.map_diag(plt.hist)
pg = pg.map_offdiag(plt.scatter, edgecolor="black", s=10, alpha=0.25)
#plt.show()

g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci": False, "x_jitter": 0.25, "y_jitter": 0.25}, \
hue='type', diag_kind='hist', diag_kws={"bins": 10, "alpha": 1.0}, palette=dict(red="red", white="white"), \
markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
sns.set_style({'legend.frameon': True,'legend.numpoints': 0,'legend.scatterpoints': 0})
wine_all_plot = sns.pairplot(wine, kind='reg', hue='type', palette=dict(red="red", white="white"), markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
wine_sample_plot = sns.pairplot(wine_sample, kind='reg', hue='type', palette=dict(red="red", white="white"), markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])

wine['ln_fixed_acidity'] = np.log(wine.ix[:, 'fixed_acidity'])
sns.distplot(wine.ix[:, 'fixed_acidity'])
sns.distplot(wine.ix[:, 'ln_fixed_acidity'])
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14, \
		horizontalalignment='center', verticalalignment='top',
		x=0.5, y=0.999)
#plt.show()

# Look at the distribution of quality by wine type
red_wine = wine.ix[wine['type']=='red', 'quality']
white_wine = wine.ix[wine['type']=='white', 'quality']

sns.set_style("dark")
print(sns.distplot(red_wine, \
		norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, \
		norm_hist=True, kde=False, color="white", label="White wine"))
sns.axlabel("Quality Score", "Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
#plt.show()

# Test whether mean quality is different between red and white wines
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f  pvalue: %.4f' % (tstat, pvalue))

# Fit a multivariate linear regression model
#wine_standardized = (wine - wine.mean()) / wine.std()
#formula_all = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
#formula_all = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
#formula = 'quality ~ residual_sugar + alcohol'
lm = ols(my_formula, data=wine).fit()
#lm = glm(my_formula, data=wine, family=sm.families.Gaussian()).fit()
#lm = smf.glm(formula_all, data=wine_standardized, family=sm.families.Gaussian()).fit()
print(lm.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficient Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))

# Fit a multivariate linear model with standardized independent variables
dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]
independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()
wine_standardized = pd.concat([dependent_variable, independent_variables_standardized], axis=1)
lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())

# Predict quality scores for "new" observations
new_observations = wine.ix[wine.index.isin(xrange(10)), independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)
