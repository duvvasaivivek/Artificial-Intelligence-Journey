import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# ----------------------------------------------------
# Experiment: Feature Scaling
#
# Objective
# ---------
# Observe how Feature Scaling changes the feature
# values while preserving their relative order.
#
# Note
# ----
# For Simple Linear Regression, Feature Scaling
# does not significantly change the final model.
#
# However, it greatly improves the convergence
# speed of Gradient Descent and becomes essential
# for many Machine Learning algorithms.
# ----------------------------------------------------

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("../data/Salary_dataset.csv")

X = df[["YearsExperience"]]
y = df["Salary"]

# ----------------------------------------------------
# Original Model
# ----------------------------------------------------

original_model = LinearRegression()

original_model.fit(X, y)

# ----------------------------------------------------
# Standard Scaling
#
# Formula
#
#            x - μ
# z = ----------------
#          σ
#
# μ -> Mean
# σ -> Standard Deviation
#
# After Scaling
#
# Mean ≈ 0
# Standard Deviation ≈ 1
# ----------------------------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ----------------------------------------------------
# Model After Scaling
# ----------------------------------------------------

scaled_model = LinearRegression()

scaled_model.fit(X_scaled, y)

# ----------------------------------------------------
# Display Comparison
# ----------------------------------------------------

comparison = pd.DataFrame({

    "Original Feature": X["YearsExperience"],

    "Scaled Feature": X_scaled.flatten()

})

print(comparison)

# ----------------------------------------------------
# Plot Comparison
# ----------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    X["YearsExperience"],
    label="Original Feature",
    linewidth=2
)

plt.plot(
    X_scaled,
    label="Scaled Feature",
    linewidth=2
)

plt.title("Original vs Standardized Feature")

plt.xlabel("Sample Index")

plt.ylabel("Feature Value")

plt.legend()

plt.grid(True)

plt.show()

# ----------------------------------------------------
# Learned Parameters
# ----------------------------------------------------

print("\nOriginal Model")

print(f"Weight : {original_model.coef_[0]:.2f}")

print(f"Bias : {original_model.intercept_:.2f}")

print("\nScaled Model")

print(f"Weight : {scaled_model.coef_[0]:.2f}")

print(f"Bias : {scaled_model.intercept_:.2f}")

# ----------------------------------------------------
# Observations
# ----------------------------------------------------
"""
Feature Scaling changes the numerical values of the feature.
The relative ordering of samples remains unchanged.
Gradient Descent usually converges faster after scaling.
Scaling is essential for algorithms that depend on distance or gradients.
Scikit-Learn's LinearRegression solves the optimization analytically, so scaling has little effect on the final predictions.")
"""