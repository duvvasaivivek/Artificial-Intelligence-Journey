import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/student_scores.csv")

X = df["Hours_Studied"]
y = df["Marks"]

# Hyperparameters
#
# learning_rate : Controls the step size during
# parameter updates.
#
# iterations : Number of times the model updates
# its parameters.

lr = 0.01
it = 1000

# Initialize Parameters
#
# The model starts without any knowledge.
# Weight and bias are initialized to zero and will
# gradually improve through Gradient Descent.

w = 0
b = 0

# Gradient Descent
#
# Every iteration consists of:
#
# 1. Generate Predictions
# 2. Compute Gradients
# 3. Update Parameters
#
# The goal is to minimize the Cost Function.

n = len(X)
ch = []

for _ in range(it):
    # Hypothesis Function (ŷ = wx + b)
    ps = w*X + b

    # Cost Function
    r = y-ps
    cost = np.mean(r**2)/2
    ch.append(cost)

    # Compute Gradients
    #
    # dw = ∂J/∂w
    # db = ∂J/∂b

    dw = (-2/n)*np.sum(X*r)
    db = (-2/n)*np.sum(r)

    # Update Parameters
    #
    # Move opposite to the gradient.

    w -= lr*dw
    b -= lr*db

predictions = w*X + b

print(f"Weight : {w:.4f}")
print(f"Bias   : {b:.4f}")

comparison = pd.DataFrame({
    "Actual": y,
    "Predicted": np.round(predictions, 2)
})

print(comparison)


# Best Fit Line
plt.figure(figsize=(10,5))
plt.scatter(X,y)
plt.plot(X,predictions)
plt.title("Linear Regression using Gradient Descent")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()

# Cost Reduction
plt.figure(figsize=(10, 5))
plt.plot(ch)
plt.title("Cost vs Iterations")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.grid(True)
plt.show()