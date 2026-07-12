import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ----------------------------------------------------
# Experiment: Effect of Outliers
#
# Objective
# ---------
# Observe how a few extreme data points (outliers)
# affect the learned regression line.
#
# Experiment
#
# 1. Train on Original Dataset
# 2. Add Artificial Outliers
# 3. Train Again
# 4. Compare Regression Lines
# ----------------------------------------------------

df = pd.read_csv("../data/Salary_dataset.csv")

X = df[["YearsExperience"]]
y = df["Salary"]

# ----------------------------------------------------
# Original Model
# ----------------------------------------------------

original_model = LinearRegression()

original_model.fit(X, y)

# ----------------------------------------------------
# Create Outliers
#
# These points do not follow the normal trend.
# ----------------------------------------------------

outlier_X = pd.DataFrame({
    "YearsExperience": [18, 20, 22]
})

outlier_y = pd.Series([
    50000,
    70000,
    90000
])

X_outlier = pd.concat(
    [X, outlier_X],
    ignore_index=True
)

y_outlier = pd.concat(
    [y, outlier_y],
    ignore_index=True
)

# ----------------------------------------------------
# Train Model with Outliers
# ----------------------------------------------------

outlier_model = LinearRegression()

outlier_model.fit(
    X_outlier,
    y_outlier
)

x_line = pd.DataFrame({
    "YearsExperience":
    [i / 10 for i in range(0, 221)]
})

# This gives us 221 evenly spaced points.

y_original = original_model.predict(x_line)

y_outlier = outlier_model.predict(x_line)



# ----------------------------------------------------
# Visualization
# ----------------------------------------------------

plt.figure(figsize=(10,6))

# Original Data
plt.scatter(
    X,
    y,
    color="blue",
    label="Original Data"
)

# Outliers
plt.scatter(
    outlier_X,
    outlier_y,
    color="red",
    s=120,
    marker="X",
    label="Outliers"
)

# Original Regression Line
plt.plot(
    x_line,
    y_original,
    color="green",
    linewidth=2,
    label="Original Regression Line"
)

# Regression Line with Outliers
plt.plot(
    x_line,
    y_outlier,
    color="orange",
    linewidth=2,
    linestyle="--",
    label="Regression Line with Outliers"
)

plt.title("Effect of Outliers on Linear Regression")

plt.xlabel("Years of Experience")

plt.ylabel("Salary")

plt.legend()

plt.grid(True)

plt.show()

# ----------------------------------------------------
# Learned Parameters
# ----------------------------------------------------

print("Original Model")

print(f"Slope : {original_model.coef_[0]:.2f}")

print(f"Intercept : {original_model.intercept_:.2f}")

print("\nModel with Outliers")

print(f"Slope : {outlier_model.coef_[0]:.2f}")

print(f"Intercept : {outlier_model.intercept_:.2f}")


"""
Predictions for normal samples become less accurate.

Linear Regression is sensitive to outliers because it minimizes squared error.

Large errors receive a much larger penalty, pulling the regression line toward outliers.
"""