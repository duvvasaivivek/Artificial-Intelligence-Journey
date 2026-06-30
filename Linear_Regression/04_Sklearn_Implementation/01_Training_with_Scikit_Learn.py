import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load Dataset
df = pd.read_csv("../data/Salary_dataset.csv")

# Features and Target
X = df[["YearsExperience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Linear Regression Model
#
# Scikit-Learn internally performs all the mathematical
# computations required to learn the optimal parameters.

model = LinearRegression()

# Train Model
#
# fit() learns the optimal slope and intercept from
# the training data.

model.fit(X_train, y_train)

# Predict Test Data
#
# predict() uses the learned equation
#
# ŷ = wx + b
#
# to generate predictions.

pred = model.predict(X_test)

comparison = pd.DataFrame({
    "YearsExperience": X_test["YearsExperience"],
    "Actual Salary": y_test,
    "Predicted Salary": np.round(pred, 2)
})

print(comparison)