# ----------------------------------------------------
# Model Evaluation Metrics
#
# Model evaluation measures how close the predicted
# values are to the actual values.
#
# Lower Error  -> Better Model
# Higher R²    -> Better Model
# ----------------------------------------------------

# ----------------------------------------------------
# Mean Absolute Error (MAE)
#
#          1
# MAE = ------- Σ |y - ŷ|
#         n
#
# • Average absolute prediction error.
# • Treats all errors equally.
# • Measured in the original unit.
# • Lower MAE is better.
# ----------------------------------------------------

#mae = np.mean(np.abs(y_test - pred))

# ----------------------------------------------------
# Mean Squared Error (MSE)
#
#          1
# MSE = ------- Σ (y - ŷ)²
#         n
#
# • Squares every error.
# • Penalizes large errors heavily.
# • Used in Linear Regression optimization.
# • Lower MSE is better.
# ----------------------------------------------------

#mse = np.mean((y_test - pred) ** 2)

# ----------------------------------------------------
# Root Mean Squared Error (RMSE)
#
# RMSE = √MSE
#
# • Square root of MSE.
# • Converts error back to original units.
# • Easier to interpret than MSE.
# • Lower RMSE is better.
# ----------------------------------------------------

#rmse = np.sqrt(mse)

# ----------------------------------------------------
# R² Score (Coefficient of Determination)
#
#                 SS_res
# R² = 1 - ----------------
#              SS_tot
#
# where
#
# SS_res = Σ(y - ŷ)²
# SS_tot = Σ(y - ȳ)²
#
# • Measures how well the model explains the
#   variation in the target variable.
#
# Interpretation
#
# R² = 1   -> Perfect Model
# R² ≈ 0.9 -> Excellent Fit
# R² ≈ 0.8 -> Good Fit
# R² = 0   -> Same as predicting the mean
# R² < 0   -> Worse than predicting the mean
#
# Higher R² is better.
# ----------------------------------------------------

# ss_res = np.sum((y_test - pred) ** 2)
# ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)

# r2 = 1 - (ss_res / ss_tot)

# ----------------------------------------------------
# Display Evaluation Metrics
# ----------------------------------------------------

# print(f"MAE  : {mae:.4f}")
# print(f"MSE  : {mse:.4f}")
# print(f"RMSE : {rmse:.4f}")
# print(f"R²   : {r2:.4f}")



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

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# ----------------------------------------------------
# Evaluation Metrics
# ----------------------------------------------------

# Mean Absolute Error (MAE)
mae = np.mean(np.abs(y_test - pred))

# Mean Squared Error (MSE)
mse = np.mean((y_test - pred) ** 2)

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)

# R² Score
ss_res = np.sum((y_test - pred) ** 2)
ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)

r2 = 1 - (ss_res / ss_tot)

# Display Results
print(f"MAE  : {mae:.4f}")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")