import numpy as np


class LinearRegression:
    """
    Linear Regression implemented from scratch
    using Gradient Descent.
    """

    def __init__(self, lr=0.01, it=1000):

        # Hyperparameters
        self.lr = lr
        self.it = it

        # Model Parameters
        self.w = 0
        self.b = 0

    def fit(self, X, y):
        """
        Train the model using Gradient Descent.

        Parameters
        ----------
        X : Feature values
        y : Target values
        """

        n = len(X)

        for _ in range(self.it):

            # Hypothesis Function
            pred = self.predict(X)

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
        Predict target values.
        """

        return self.w * X + self.b

    def score(self, X, y):
        """
        Compute the R² Score.
        """

        pred = self.predict(X)

        ss_res = np.sum((y - pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)

        return 1 - (ss_res / ss_tot)