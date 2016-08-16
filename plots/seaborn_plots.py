#!/usr/bin/env python3
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)


# Simple plot of linear, quadratic, and cubic curves
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend(loc="best")
plt.show()


# Histogram
x = np.random.normal(size=1000)
sns.distplot(x, bins=20, kde=True, rug=False, label="Histogram w/o Density")
sns.axlabel("Value", "Frequency")
plt.title("Histogram of a Random Sample from a Normal Distribution")
plt.legend()
plt.show()


# Scatter plot
mean, cov = [5, 10], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
data_frame = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=data_frame, kind="reg").set_axis_labels("x", "y")
plt.suptitle("Joint Plot of Two Variables with Bivariate and Univariate Graphs")
plt.show()


# Pairwise bivariate
#iris = sns.load_dataset("iris")
#sns.pairplot(iris)
#plt.show()


# Linear regression model
tips = sns.load_dataset("tips")
#sns.lmplot(x="total_bill", y="tip", data=tips)
sns.lmplot(x="size", y="tip", data=tips, x_jitter=.15, ci=None)
#sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean, ci=None)
plt.show()


# Box plots
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
#sns.factorplot(x="time", y="total_bill", hue="smoker",
#               col="day", data=tips, kind="box", size=4, aspect=.5)
plt.show()


# Bar plots
titanic = sns.load_dataset("titanic")
#sns.barplot(x="sex", y="survived", hue="class", data=titanic)
#sns.countplot(y="deck", hue="class", data=titanic, palette="Greens_d")
#plt.show()


# Non-linear regression model
anscombe = sns.load_dataset("anscombe")
# polynomial
#sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
#           order=2, ci=False, scatter_kws={"s": 80})
#plt.show()


# robust to outliers
#sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
#           robust=True, ci=False, scatter_kws={"s": 80})
#plt.show()


# logistic
#tips["big_tip"] = (tips.tip / tips.total_bill) > .15
#sns.lmplot(x="total_bill", y="big_tip", data=tips, logistic=True, y_jitter=.03).set_axis_labels("Total Bill", "Big Tip")
#plt.title("Logistic Regression of Big Tip vs. Total Bill")
#plt.show()


# lowess smoother
#sns.lmplot(x="total_bill", y="tip", data=tips, lowess=True)
#plt.show()


# Condition on other variables
#sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
#           markers=["o", "x"], palette="Set1")
#sns.lmplot(x="total_bill", y="tip", hue="smoker",
#           col="time", row="sex", data=tips)
#plt.show()


# Control shape and size of plot
#sns.lmplot(x="total_bill", y="tip", col="day", data=tips, col_wrap=2, size=3)
#sns.lmplot(x="total_bill", y="tip", col="day", data=tips, aspect=.5)
#plt.show()


# Plotting regression in other contexts
#sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
#sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
#             size=5, aspect=.8, kind="reg")
#sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
#             hue="smoker", size=5, aspect=.8, kind="reg")
#plt.show()
