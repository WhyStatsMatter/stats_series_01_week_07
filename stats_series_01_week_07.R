# Snippet 1: Introduction to Linear Regression
X <- c(1, 2, 3, 4)
y <- c(3, 6, 9, 12)
model <- lm(y ~ X)

# Snippet 2: Multiple Linear Regression
X_multi <- data.frame(X1 = c(1, 2, 3, 4), X2 = c(2, 4, 6, 8))
model_multi <- lm(y ~ X1 + X2, data = X_multi)

# Snippet 3: Assumptions and Diagnostics
residuals <- resid(model)
plot(predict(model), residuals)
abline(h = 0, col = "red")

# Snippet 4: Interpretation and Applications (Using the previous models)
slope <- coef(model)['X']
intercept <- coef(model)['(Intercept)']
