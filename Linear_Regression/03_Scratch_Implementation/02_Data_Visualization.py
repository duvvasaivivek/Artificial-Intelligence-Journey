import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

df = pd.read_csv("../data/student_scores.csv")
print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df.info())
print(df.describe())

X = df['Hours_Studied']
y = df['Marks']

plt.figure(figsize=(8, 6))

plt.scatter(X,y)
plt.title("Marks Can Be Get")
plt.xlabel("Study Hours")
plt.ylabel("Expected Marks")
plt.grid(True)

plt.show()