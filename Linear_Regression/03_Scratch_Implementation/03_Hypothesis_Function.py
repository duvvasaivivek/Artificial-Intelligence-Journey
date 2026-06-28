import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/student_scores.csv")

# X : Input given to the model.
# y : Expected output the model should predict.
# ----------------------------------------------------

X = df["Hours_Studied"]
y = df["Marks"]

w = 8
b = 30

ps = w*X +b

# w -> weight (slope)
# b -> bias (intercept)
# x -> input feature
# ŷ -> predicted output

# This equation generates predictions.
# No learning happens here.


# Compare actual values with predicted values.
#
# This allows us to observe how close our manually
# chosen parameters are to the real data.
#
# In the next file we will mathematically measure
# this difference using the Cost Function.

comp = pd.DataFrame({
    "Hours Studied" : X,
    "Actual Marks" : y,
    "Predicted" : ps
})

print(comp)