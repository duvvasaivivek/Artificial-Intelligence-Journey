import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# Gradient Descent Visualization
#
# Purpose
# -------
# Visualize how the Cost Function decreases as
# Gradient Descent updates the model parameters.
#
# Graph:
#
# X-axis -> Iterations
# Y-axis -> Cost
#
# A smooth decreasing curve indicates successful
# convergence.
# ----------------------------------------------------

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("../data/Salary_dataset.csv")

X = df["YearsExperience"].values
y = df["Salary"].values

# ----------------------------------------------------
# Hyperparameters
# ----------------------------------------------------

lr = 0.01
it = 1000

# ----------------------------------------------------
# Initialize Parameters
# ----------------------------------------------------

w = 0
b = 0

n = len(X)

# ----------------------------------------------------
# Store Cost History
#
# Stores the Cost after every iteration so that
# we can visualize the learning process.
# ----------------------------------------------------

cost_history = []

# ----------------------------------------------------
# Gradient Descent
# ----------------------------------------------------

for _ in range(it):

    # -------------------------
    # Prediction
    #
    # ŷ = wx + b
    # -------------------------

    pred = w * X + b

    # -------------------------
    # Residuals
    #
    # y - ŷ
    # -------------------------

    residuals = y - pred

    # -------------------------
    # Cost Function
    #
    #             1
    # J = --------------- Σ(y-ŷ)²
    #         2n
    #
    # Lower Cost
    # ↓
    # Better Model
    # -------------------------

    cost = (1 / (2 * n)) * np.sum(residuals ** 2)

    cost_history.append(cost)

    # -------------------------
    # Compute Gradients
    # -------------------------

    dw = (-2 / n) * np.sum(X * residuals)

    db = (-2 / n) * np.sum(residuals)

    # -------------------------
    # Update Parameters
    #
    # w = w - lr × dw
    #
    # b = b - lr × db
    # -------------------------

    w -= lr * dw
    b -= lr * db

# ----------------------------------------------------
# Plot Cost vs Iterations
# ----------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    range(1, it + 1),
    cost_history,
    color="blue",
    linewidth=2
)

plt.title("Gradient Descent Convergence")

plt.xlabel("Iterations")

plt.ylabel("Cost")

plt.grid(True)

plt.show()

# ----------------------------------------------------
# Final Parameters
# ----------------------------------------------------

print("Final Parameters")

print(f"Weight : {w:.2f}")

print(f"Bias   : {b:.2f}")

print(f"Final Cost : {cost_history[-1]:.2f}")
