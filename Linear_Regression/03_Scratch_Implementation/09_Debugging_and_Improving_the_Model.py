import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


class LinearRegression:

    def __init__(self, lr=0.01, it=1000):

        self.lr = lr
        self.it = it

        self.w = 0
        self.b = 0

    def fit(self, X, y):

        n = len(X)

        for _ in range(self.it):

            pred = self.w * X + self.b

            residuals = y - pred

            dw = (-2 / n) * np.sum(X * residuals)
            db = (-2 / n) * np.sum(residuals)

            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X):

        return self.w * X + self.b


# Load Dataset
df = pd.read_csv("../data/student_scores.csv")

X = df["Hours_Studied"]
y = df["Marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------------------------------
# Experiment 1 : Good Learning Rate
#
# lr = 0.01
#
# • Stable convergence
# • Cost decreases smoothly
# • Produces a good model
# ----------------------------------------------------

model = LinearRegression(lr=0.01, it=1000)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Good Learning Rate")
print(pred)

# ----------------------------------------------------
# Experiment 2 : Learning Rate Too Small
#
# lr = 0.00001
#
# • Very slow learning
# • Requires many iterations
# • May not converge within the given iterations
# ----------------------------------------------------

model = LinearRegression(lr=0.00001, it=1000)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nSmall Learning Rate")
print(pred)

# ----------------------------------------------------
# Experiment 3 : Learning Rate Too Large
#
# lr = 1
#
# • Large parameter updates
# • May overshoot the minimum
# • Can diverge instead of converging
# ----------------------------------------------------

model = LinearRegression(lr=1, it=1000)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nLarge Learning Rate")
print(pred)

# ----------------------------------------------------
# Experiment 4 : Too Few Iterations
#
# it = 10
#
# • Model stops learning too early
# • Parameters remain far from optimal
# ----------------------------------------------------

model = LinearRegression(lr=0.01, it=10)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nFew Iterations")
print(pred)

# ----------------------------------------------------
# Common Problems in Gradient Descent
# ----------------------------------------------------

# 1. Learning Rate Too Small

# • Slow convergence
# • Requires many iterations
# • Training takes longer

# ----------------------------------------------------

# 2. Learning Rate Too Large

# • Overshoots the minimum
# • Cost may increase
# • Training becomes unstable

# ----------------------------------------------------

# 3. Too Few Iterations

# • Model under-trains
# • Parameters remain inaccurate
# • Predictions are poor

# ----------------------------------------------------

# 4. Too Many Iterations

# • Usually harmless for Linear Regression
# • Increases computation time
# • Stop when the Cost stabilizes

# ----------------------------------------------------

# How to Improve the Model

# ✓ Choose an appropriate learning rate.

# ✓ Increase iterations if the Cost is still decreasing.

# ✓ Normalize or standardize features for faster convergence.

# ✓ Check the data for outliers.

# ✓ Always evaluate on the test set.