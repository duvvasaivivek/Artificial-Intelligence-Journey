import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# ----------------------------------------------------
# Scratch Implementation
# ----------------------------------------------------

class LinearRegressionScratch:

    def __init__(self, lr=0.01, it=1000):

        self.lr = lr
        self.it = it

        self.w = 0
        self.b = 0

    def fit(self, X, y):

        n = len(X)

        X = X.values.flatten()
        y = y.values

        for _ in range(self.it):

            pred = self.w * X + self.b

            residuals = y - pred

            dw = (-2 / n) * np.sum(X * residuals)
            db = (-2 / n) * np.sum(residuals)

            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X):

        X = X.values.flatten()

        return self.w * X + self.b


# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("../data/Salary_dataset.csv")

X = df[["YearsExperience"]]
y = df["Salary"]

# ----------------------------------------------------
# Train-Test Split
# ----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------------------------------
# Scratch Model
# ----------------------------------------------------

scratch = LinearRegressionScratch()

scratch.fit(X_train, y_train)

scratch_pred = scratch.predict(X_test)

# ----------------------------------------------------
# Scikit-Learn Model
# ----------------------------------------------------

sklearn_model = LinearRegression()

sklearn_model.fit(X_train, y_train)

sklearn_pred = sklearn_model.predict(X_test)

# ----------------------------------------------------
# Comparison
# ----------------------------------------------------

comparison = pd.DataFrame({

    "Actual Salary": y_test.values,

    "Scratch Prediction": np.round(scratch_pred, 2),

    "Scikit-Learn Prediction": np.round(sklearn_pred, 2)

})

print(comparison)

# ----------------------------------------------------
# Learned Parameters
# ----------------------------------------------------

print("\nScratch Model")

print(f"Weight : {scratch.w:.2f}")
print(f"Bias   : {scratch.b:.2f}")

print("\nScikit-Learn Model")

print(f"Weight : {sklearn_model.coef_[0]:.2f}")
print(f"Bias   : {sklearn_model.intercept_:.2f}")

# ----------------------------------------------------
# Scratch vs Scikit-Learn
#
# Scratch Implementation
#
# • Implemented manually.
# • Gradient Descent used for optimization.
# • Every mathematical step is visible.
#
# Scikit-Learn
#
# • Optimized library implementation.
# • Faster and more reliable.
# • Internals are hidden.
#
# Both aim to learn the same equation:
#
# ŷ = wx + b
# ----------------------------------------------------

# ----------------------------------------------------
# Why compare both models?
#
# If the learned parameters and predictions are
# nearly identical, it validates that our scratch
# implementation is correct.
#
# Small numerical differences may occur because
# Scikit-Learn uses highly optimized algorithms.
# ----------------------------------------------------