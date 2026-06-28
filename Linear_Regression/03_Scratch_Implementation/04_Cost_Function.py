import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/student_scores.csv")

X = df["Hours_Studied"]
y = df["Marks"]

w = 8
b = 30

ps = w*X +b

r = y-ps

# Residuals (Prediction Errors)
#
# Residual = Actual - Predicted
#
# Positive Residual  -> Model underestimated.
# Negative Residual  -> Model overestimated.
# Zero Residual      -> Perfect prediction.

r2 = r**2

# Squared Residuals
#
# Squaring removes negative signs and penalizes
# larger errors more heavily.

mse = np.mean(r2)

# Mean Squared Error (MSE)
#
#           1
# MSE = -------- Σ(y - ŷ)²
#          n
#
# Measures the average squared prediction error.
# Lower MSE indicates a better model.

print(f"Mean Squared Error (MSE): {mse:.2f}")

cost = mse/2

# Cost Function
#
#            1
# J(w,b) = ----- Σ(y - ŷ)²
#           2n
#
# The factor 1/2 simplifies differentiation during
# Gradient Descent.

print(f"Cost Function J(w,b): {cost:.2f}")

comp = pd.DataFrame({
    "Hours Studied": X,
    "Actual Marks": y,
    "Predicted Marks": ps,
    "Residual": r
})

print("\nComparison")
print(comp)