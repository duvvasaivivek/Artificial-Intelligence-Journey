import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# Experiment: Effect of Learning Rate
#
# Objective
# ---------
# Observe how different learning rates affect
# Gradient Descent.
#
# Learning Rates Tested
#
# • 0.0001 -> Very Small
# • 0.01   -> Good
# • 1.0    -> Very Large
#
# Observation
#
# • Final Cost
# • Learned Parameters
# • Convergence Speed
# ----------------------------------------------------

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("../data/Salary_dataset.csv")

X = df["YearsExperience"].values
y = df["Salary"].values

n = len(X)
it = 100


def gd(lr):
    w = 0
    b = 0
    ch = []

    for _ in range(it):

        pred = w*X + b
        residuals = y - pred
        cost = (1/(2*n))*np.sum(residuals**2)

        ch.append(cost)

        dw = (-2/n)*np.sum(X*residuals)
        db = (-2/n)*np.sum(residuals)

        w -= lr*dw
        b -= lr*db
    
    return w, b, ch


learning_rates = [0.0001, 0.01, 1.0]

plt.figure(figsize=(10,6))

for lr in learning_rates:

    w, b, cost_history = gd(lr)

    print(f"\nLearning Rate : {lr}")

    print(f"Weight : {w:.2f}")

    print(f"Bias : {b:.2f}")

    print(f"Final Cost : {cost_history[-1]:.2f}")

"""
Small Learning Rate (0.0001)
----------------------------
• Slow convergence
• Stable learning
• Requires many iterations

Good Learning Rate (0.01)
--------------------------
• Fast convergence
• Stable optimization
• Recommended

Large Learning Rate (1.0)
-------------------------
• Overshoots the minimum
• Cost increases
• Model may diverge
"""