import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ----------------------------------------------------
# Data & Best Fit Line Visualization
#
# Purpose
# -------
# 1. Understand the relationship between the feature
#    and the target variable.
#
# 2. Train a Linear Regression model.
#
# 3. Visualize the learned Best Fit Line.
#
# Interpretation
# --------------
# • Blue Points  -> Training Data
# • Green Points -> Test Data
# • Red Line     -> Learned Regression Line
#
# If the line passes close to most data points,
# the model has learned the relationship well.
# ----------------------------------------------------

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("../data/Salary_dataset.csv")

print("First 5 Rows")
print(df.head())

# ----------------------------------------------------
# Features and Target
# ----------------------------------------------------

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
# Train Linear Regression Model
# ----------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ----------------------------------------------------
# Best Fit Line
#
# The regression equation is
#
# ŷ = wx + b
#
# where
#
# w -> Slope
# b -> Intercept
# ----------------------------------------------------

w = model.coef_[0]
b = model.intercept_

print("\nLearned Equation")
print(f"Salary = {w:.2f} × YearsExperience + {b:.2f}")

# ----------------------------------------------------
# Generate Line Points
# ----------------------------------------------------

x_line = np.linspace(
    X["YearsExperience"].min(),
    X["YearsExperience"].max(),
    100
).reshape(-1, 1)

y_line = model.predict(x_line)

# ----------------------------------------------------
# Visualization
# ----------------------------------------------------

plt.figure(figsize=(10, 6))

# Training Data
plt.scatter(
    X_train,
    y_train,
    color="blue",
    label="Training Data"
)

# Test Data
plt.scatter(
    X_test,
    y_test,
    color="green",
    label="Test Data"
)

# Best Fit Line
plt.plot(
    x_line,
    y_line,
    color="red",
    linewidth=2.5,
    label="Best Fit Line"
)

plt.title("Linear Regression - Data & Best Fit Line")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.legend()

plt.grid(True)

plt.show()