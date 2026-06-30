import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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
# Create & Train Model
# ----------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ----------------------------------------------------
# Model Parameters
#
# Learned Equation
#
# ŷ = wx + b
#
# coef_      -> Weight (Slope)
# intercept_ -> Bias (Intercept)
# ----------------------------------------------------

w = model.coef_[0]
b = model.intercept_

print(f"Weight (Slope) : {w:.2f}")
print(f"Bias (Intercept): {b:.2f}")

# ----------------------------------------------------
# Final Regression Equation
# ----------------------------------------------------

print(f"\nRegression Equation:")
print(f"Salary = {w:.2f} × YearsExperience + {b:.2f}")

# ----------------------------------------------------
# Model Parameters
#
# Scikit-Learn learns the equation
#
# ŷ = wx + b
#
# where
#
# w -> Weight / Slope
# b -> Bias / Intercept
#
# These are exactly the same parameters we learned
# manually using Gradient Descent.
# ----------------------------------------------------

# ----------------------------------------------------
# coef_
#
# Returns the learned weight(s).
#
# In Simple Linear Regression,
# only one feature exists.
#
# Therefore,
#
# coef_[0]
#
# gives the slope of the regression line.
# ----------------------------------------------------

# ----------------------------------------------------
# intercept_
#
# Returns the learned bias.
#
# It represents the predicted value when
# the feature value is zero.
# ----------------------------------------------------