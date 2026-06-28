import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("../data/student_scores.csv")

X = df["Hours_Studied"]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

lr = 0.01
it = 1000

w = 0
b = 0

n = len(X_train)

for _ in range(it):
    ps = w*X + b
    r = y-ps

    dw = (-2/n)*np.sum(X*r)
    db = (-2/n)*np.sum(r)

    w -= lr*dw
    b -= lr*db

predictions = w*X_test + b

print(f"Weight : {w:.4f}")
print(f"Bias   : {b:.4f}")

comparison = pd.DataFrame({
    "Hours Studied": X_test.values,
    "Actual Marks": y_test.values,
    "Predicted Marks": np.round(predictions, 2)
})

print(comparison)