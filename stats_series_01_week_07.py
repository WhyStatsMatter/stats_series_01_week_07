# Snippet 1: Introduction to Linear Regression
from sklearn.linear_model import LinearRegression

X, y = [[1], [2], [3], [4]], [3, 6, 9, 12] # Simple example
model = LinearRegression().fit(X, y)

# Snippet 2: Multiple Linear Regression
X_multi = [[1, 2], [2, 4], [3, 6], [4, 8]]
model_multi = LinearRegression().fit(X_multi, y)

# Snippet 3: Assumptions and Diagnostics
import statsmodels.api as sm
import matplotlib.pyplot as plt

X = sm.add_constant(X) # Adding intercept
model_stats = sm.OLS(y, X).fit()
residuals = model_stats.resid
plt.scatter(model_stats.predict(), residuals)
plt.hlines(0, min(model_stats.predict()), max(model_stats.predict()), colors='r')
plt.show()

# Snippet 4: Interpretation and Applications (Using the previous models)
slope = model.coef_
intercept = model.intercept_
