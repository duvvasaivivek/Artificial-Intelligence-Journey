import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split


class LinearRegression:

    def __init__(self, lr=0.01, it=1000):
        # Initialize Hyperparameters
        self.lr = lr
        self.it = it

        # Initialize Model Parameters
        self.w = 0
        self.b = 0

    def fit(self, X, y):
        """
        Train the model using Gradient Descent.
        """

        n = len(X)

        for _ in range(self.it):

            # Hypothesis Function
            pred = self.w * X + self.b

            # Compute Residuals
            residuals = y - pred

            # Compute Gradients
            dw = (-2 / n) * np.sum(X * residuals)
            db = (-2 / n) * np.sum(residuals)

            # Update Parameters
            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict(self, X):
        """
        Generate predictions using the learned parameters.
        """

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

# Create Model
model = LinearRegression(
    lr=0.01,
    it=1000
)

# Train Model
model.fit(X_train, y_train)

# Predict on Test Data
pred = model.predict(X_test)

# Compare Predictions
comparison = pd.DataFrame({
    "Hours Studied": X_test.values,
    "Actual Marks": y_test.values,
    "Predicted Marks": np.round(pred, 2)
})

print(comparison)

# Plot Best Fit Line
plt.figure(figsize=(8, 6))

plt.scatter(X_train, y_train, label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Test Data")

x_line = np.linspace(X.min(), X.max(), 100)
y_line = model.predict(x_line)
