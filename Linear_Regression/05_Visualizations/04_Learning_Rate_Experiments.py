import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# Learning Rate Experiments
#
# Purpose
# -------
# Compare how different learning rates affect
# Gradient Descent convergence.
#
# Learning Rates
#
# 0.0001 -> Slow Learning
# 0.01   -> Good Learning
# 1.0    -> Divergence
#
# Graph
#
# X-axis -> Iterations
# Y-axis -> Cost
# ----------------------------------------------------

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("../data/Salary_dataset.csv")

X = df["YearsExperience"].values
y = df["Salary"].values

n = len(X)
it = 100

# ----------------------------------------------------
# Gradient Descent Function
# ----------------------------------------------------

def gradient_descent(lr):

    w = 0
    b = 0

    cost_history = []

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
        # Residual = y - ŷ
        # -------------------------

        residuals = y - pred

        # -------------------------
        # Cost Function
        #
        #             1
        # J = --------------- Σ(y-ŷ)²
        #         2n
        # -------------------------

        cost = (1 / (2 * n)) * np.sum(residuals ** 2)

        cost_history.append(cost)

        # -------------------------
        # Gradients
        # -------------------------

        dw = (-2 / n) * np.sum(X * residuals)
        db = (-2 / n) * np.sum(residuals)

        # -------------------------
        # Parameter Update
        # -------------------------

        w -= lr * dw
        b -= lr * db

    return cost_history

# ----------------------------------------------------
# Train with Different Learning Rates
# ----------------------------------------------------

cost_lr_small = gradient_descent(0.0001)

cost_lr_good = gradient_descent(0.01)

cost_lr_large = gradient_descent(1)

# ----------------------------------------------------
# Visualization
# ----------------------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    cost_lr_small,
    label="lr = 0.0001"
)

plt.plot(
    cost_lr_good,
    label="lr = 0.01"
)

plt.plot(
    cost_lr_large,
    label="lr = 1.0"
)

plt.title("Learning Rate Comparison")

plt.xlabel("Iterations")

plt.ylabel("Cost")

plt.legend()

plt.grid(True)

plt.show()

# ----------------------------------------------------
# Interpretation
# ----------------------------------------------------

print("\nLearning Rate Analysis")

print("lr = 0.0001")
print("- Learns very slowly.")
print("- Cost decreases gradually.")
print("- Requires many iterations.\n")

print("lr = 0.01")
print("- Smooth convergence.")
print("- Efficient learning.")
print("- Recommended learning rate.\n")

print("lr = 1.0")
print("- Updates are too large.")
print("- Cost may increase.")
print("- Model can diverge instead of converging.")