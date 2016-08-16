#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in \
churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
print(churn.head())
print(churn.describe())


# Calculate descriptive statistics for grouped data
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge', 'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))

# Specify different statistics for different variables
print(churn.groupby(['churn']).agg({'day_charge' : ['mean', 'std'], 
				'eve_charge' : ['mean', 'std'],
				'night_charge' : ['mean', 'std'],
				'intl_charge' : ['mean', 'std'],
				'account_length' : ['count', 'min', 'max'],
				'custserv_calls' : ['count', 'min', 'max']}))

# Create total_charges, split it into 5 groups, and
# calculate statistics for each of the groups
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + \
						 churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2)
def get_stats(group):
	return {'min' : group.min(), 'max' : group.max(),
			'count' : group.count(), 'mean' : group.mean(),
			'std' : group.std()}
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())

# Split account_length into quantiles and
# calculate statistics for each of the quantiles
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack())

# Create binary/dummy indicator variables for intl_plan and vmail_plan
# and join them with the churn column in a new DataFrame
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
print(churn_with_dummies.head())

# Split total_charges into quartiles, create binary indicator variables
# for each of the quartiles, and add them to the churn DataFrame
qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
churn_with_dummies = churn.join(dummies)
print(churn_with_dummies.head())

# Create pivot tables
print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], \
						aggfunc='mean', fill_value='NaN', margins=True))

# Fit a logistic regression model
dependent_variable = churn['churn01']
independent_variables = churn[['account_length', 'custserv_calls', 'total_charges']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()
#logit_model = smf.glm(output_variable, input_variables, family=sm.families.Binomial()).fit()
print(logit_model.summary())
print("\nQuantities you can extract from the result:\n%s" % dir(logit_model))
print("\nCoefficients:\n%s" % logit_model.params)
print("\nCoefficient Std Errors:\n%s" % logit_model.bse)
#logit_marginal_effects = logit_model.get_margeff(method='dydx', at='overall')
#print(logit_marginal_effects.summary())

print("\ninvlogit(-7.2205 + 0.0012*mean(account_length) + 0.4443*mean(custserv_calls) + 0.0729*mean(total_charges))")

def inverse_logit(model_formula):
	from math import exp
	return (1.0 / (1.0 + exp(-model_formula)))*100.0

at_means = float(logit_model.params[0]) + \
	float(logit_model.params[1])*float(churn['account_length'].mean()) + \
	float(logit_model.params[2])*float(churn['custserv_calls'].mean()) + \
	float(logit_model.params[3])*float(churn['total_charges'].mean())

print(churn['account_length'].mean())
print(churn['custserv_calls'].mean())
print(churn['total_charges'].mean())
print(at_means)
print("Probability of churn when independent variables are at their mean values: %.2f" % inverse_logit(at_means))

cust_serv_mean = float(logit_model.params[0]) + \
	float(logit_model.params[1])*float(churn['account_length'].mean()) + \
	float(logit_model.params[2])*float(churn['custserv_calls'].mean()) + \
	float(logit_model.params[3])*float(churn['total_charges'].mean())
		
cust_serv_mean_minus_one = float(logit_model.params[0]) + \
		float(logit_model.params[1])*float(churn['account_length'].mean()) + \
		float(logit_model.params[2])*float(churn['custserv_calls'].mean()-1.0) + \
		float(logit_model.params[3])*float(churn['total_charges'].mean())

print(cust_serv_mean)
print(churn['custserv_calls'].mean()-1.0)
print(cust_serv_mean_minus_one)
print("Probability of churn when account length changes by 1: %.2f" % (inverse_logit(cust_serv_mean) - inverse_logit(cust_serv_mean_minus_one)))

# Predict churn for "new" observations
new_observations = churn.ix[churn.index.isin(xrange(10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

# Fit a logistic regression model
output_variable = churn['churn01']
vars_to_keep = churn[['account_length', 'custserv_calls', 'total_charges']]
inputs_standardized = (vars_to_keep - vars_to_keep.mean()) / vars_to_keep.std()
input_variables = sm.add_constant(inputs_standardized, prepend=False)
logit_model = sm.Logit(output_variable, input_variables).fit()
#logit_model = smf.glm(output_variable, input_variables, family=sm.families.Binomial()).fit()
print(logit_model.summary())
print(logit_model.params)
print(logit_model.bse)
#logit_marginal_effects = logit_model.get_margeff(method='dydx', at='overall')
#print(logit_marginal_effects.summary())

# Predict output value for a new observation based on its mean standardized input values
input_variables = [0., 0., 0., 1.]
predicted_value = logit_model.predict(input_variables)
print("Predicted value: %.5f") % predicted_value