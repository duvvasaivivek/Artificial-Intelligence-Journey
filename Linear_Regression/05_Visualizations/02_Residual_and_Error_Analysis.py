import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ----------------------------------------------------
# Residual & Error Analysis
#
# Purpose
# -------
# Analyze how well the model predicts unseen data.
#
# This file visualizes:
#
# 1. Actual vs Predicted Values
# 2. Residual Plot
#
# Interpretation
# --------------
#
# Actual vs Predicted Plot
# • Points near the diagonal line -> Good predictions
# • Points far from the line      -> Large prediction errors
#
# Residual Plot
# • Residuals randomly scattered around zero -> Good model
# • Patterns or curves -> Linear Regression may not be suitable
# ----------------------------------------------------

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
# Train Model
# ----------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ----------------------------------------------------
# Generate Predictions
# ----------------------------------------------------

pred = model.predict(X_test)

# ----------------------------------------------------
# Calculate Residuals
#
# Residual = Actual - Predicted
#
# Positive Residual
# ↓
# Model underestimated.
#
# Negative Residual
# ↓
# Model overestimated.
# ----------------------------------------------------

residuals = y_test - pred

# ----------------------------------------------------
# Actual vs Predicted Plot
# ----------------------------------------------------

plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    pred,
    color="blue"
)

# Perfect Prediction Line
plt.plot(
    [y.min(), y.max()],
    [y.min(), y.max()],
    color="red",
    linewidth=2,
    linestyle="--",
    label="Perfect Prediction"
)

plt.title("Actual vs Predicted Salary")

plt.xlabel("Actual Salary")

plt.ylabel("Predicted Salary")

plt.legend()

plt.grid(True)

plt.show()

# ----------------------------------------------------
# Residual Plot
# ----------------------------------------------------

plt.figure(figsize=(8,6))

plt.scatter(
    pred,
    residuals,
    color="purple"
)

# Zero Error Line
plt.axhline(
    y=0,
    color="red",
    linestyle="--",
    linewidth=2
)

plt.title("Residual Plot")

plt.xlabel("Predicted Salary")

plt.ylabel("Residual (Actual - Predicted)")

plt.grid(True)

plt.show()

# ----------------------------------------------------
# Residual Analysis
# ----------------------------------------------------

print("\nResidual Analysis")

print(f"Mean Residual : {np.mean(residuals):.2f}")

print(f"Maximum Residual : {np.max(residuals):.2f}")

print(f"Minimum Residual : {np.min(residuals):.2f}")
