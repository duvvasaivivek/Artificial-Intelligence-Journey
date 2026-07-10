# Common Mistakes in Linear Regression

> A practical guide to the most common mistakes made while learning, implementing, and using Linear Regression.

---

# 1. Theory Mistakes

## Mistake 1: Using Linear Regression for Classification

### Wrong

Predicting

- Spam / Not Spam
- Yes / No
- True / False

using Linear Regression.

### Why?

Linear Regression predicts **continuous numerical values**, not categories.

### Correct Algorithms

- Logistic Regression
- Decision Trees
- Random Forest
- SVM

---

## Mistake 2: Assuming Every Dataset is Linear

### Wrong

Applying Linear Regression without checking the relationship.

### Why?

Linear Regression assumes a **linear relationship** between features and target.

If the relationship is nonlinear, predictions become poor.

### Solution

Always visualize the dataset first.

```text
Scatter Plot

↓

Check Linearity

↓

Then Apply Linear Regression
```

---

## Mistake 3: Ignoring Assumptions

Linear Regression assumes:

- Linear relationship
- Independent observations
- Constant variance (Homoscedasticity)
- Normally distributed residuals
- Low multicollinearity (Multiple Linear Regression)

Ignoring these assumptions reduces model reliability.

---

# 2. Mathematical Mistakes

## Mistake 4: Confusing Residual, Loss, and Cost

### Residual

\[
Residual = y-\hat y
\]

Error for one sample.

---

### Loss

\[
(y-\hat y)^2
\]

Squared error for one sample.

---

### Cost

\[
J(w,b)
=
\frac1{2n}
\sum(y-\hat y)^2
\]

Average loss over the entire dataset.

---

## Mistake 5: Forgetting Why Errors are Squared

Many beginners think squaring is only to remove negative values.

Actually, squaring also

- Penalizes large errors.
- Makes the function differentiable.
- Produces a smooth optimization surface.

---

## Mistake 6: Confusing Weight and Bias

### Weight (w)

Controls the slope.

Changes how steep the line is.

---

### Bias (b)

Moves the line up or down.

Does **not** change the slope.

---

## Mistake 7: Forgetting Why Mean is Used

We divide by **n** because we want the **average error**, not the total error.

Average error is independent of dataset size and allows fair comparison across datasets.

---

# 3. Gradient Descent Mistakes

## Mistake 8: Learning Rate Too Small

Symptoms

- Very slow learning.
- Cost decreases slowly.
- Many iterations required.

Solution

Increase the learning rate.

---

## Mistake 9: Learning Rate Too Large

Symptoms

- Cost oscillates.
- Cost increases.
- Model diverges.

Solution

Reduce the learning rate.

---

## Mistake 10: Too Few Iterations

Symptoms

- Model stops before convergence.
- High training error.
- Poor predictions.

Solution

Increase the number of iterations.

---

## Mistake 11: Too Many Iterations

Usually not harmful for Linear Regression.

However,

- Wastes computation.
- Training becomes unnecessarily slow.

Stop when the Cost stabilizes.

---

## Mistake 12: Initializing Random Large Weights

Large initial weights can make optimization unstable.

Preferred initialization

```python
w = 0
b = 0
```

---

# 4. Data Preprocessing Mistakes

## Mistake 13: Not Splitting the Dataset

### Wrong

Training and testing on the same data.

### Why?

The model memorizes the dataset.

Evaluation becomes overly optimistic.

### Correct

```text
Dataset

↓

Training Set (80%)

↓

Test Set (20%)
```

---

## Mistake 14: Ignoring Missing Values

Missing values cause errors or unreliable models.

Always check

```python
df.isnull().sum()
```

---

## Mistake 15: Ignoring Outliers

Outliers significantly affect the regression line.

Always visualize data before training.

---

## Mistake 16: Wrong Feature Shape

Wrong

```python
X = df["YearsExperience"]
```

Sometimes this creates issues because it is a Series.

Preferred

```python
X = df[["YearsExperience"]]
```

This keeps X as a DataFrame.

---

# 5. Implementation Mistakes

## Mistake 17: Forgetting to Update Parameters

Wrong

```python
dw = ...
db = ...
```

Without

```python
w -= lr * dw
b -= lr * db
```

The model never learns.

---

## Mistake 18: Updating Before Computing Gradients

Correct order

```text
Predict

↓

Residuals

↓

Gradients

↓

Update Parameters
```

Never change the order.

---

## Mistake 19: Mixing X and y

Feature

↓

X

Target

↓

y

Never interchange them.

---

## Mistake 20: Using Training Data for Prediction Evaluation

Always evaluate using

```text
X_test

↓

Predict

↓

Compare with

↓

y_test
```

---

# 6. Evaluation Mistakes

## Mistake 21: Using Accuracy

Accuracy is for **classification**.

Regression uses

- MAE
- MSE
- RMSE
- R²

---

## Mistake 22: Looking at Only One Metric

Always inspect multiple metrics.

Good practice

- MAE
- RMSE
- R²

together.

---

## Mistake 23: Misinterpreting R²

High R² does not always mean a perfect model.

Always inspect

- Scatter Plot
- Residuals
- Error Metrics

---

# 7. Scikit-Learn Mistakes

## Mistake 24: Treating fit() as Magic

Remember

```python
model.fit()
```

internally performs

- Learning
- Optimization
- Parameter estimation

The mathematics is the same as your scratch implementation.

---

## Mistake 25: Forgetting predict()

Training does not generate predictions.

Always call

```python
model.predict()
```

after training.

---

## Mistake 26: Confusing coef_ and intercept_

```python
model.coef_
```

↓

Weight (Slope)

---

```python
model.intercept_
```

↓

Bias (Intercept)

---

# 8. Interview Mistakes

## Mistake 27: Saying Linear Regression Predicts Classes

Wrong.

Linear Regression predicts continuous values.

---

## Mistake 28: Forgetting the Objective

Objective

↓

Minimize the Cost Function.

---

## Mistake 29: Saying Gradient Descent Finds Predictions

Wrong.

Gradient Descent finds

- Weight
- Bias

Predictions are then generated using

\[
\hat y = wx+b
\]

---

## Mistake 30: Not Knowing When to Use Linear Regression

Use

- Continuous target
- Linear relationship
- Simple baseline model

Avoid

- Classification problems
- Strong nonlinear relationships
- Highly complex datasets

---

# Best Practices Checklist

Before Training

- ✔ Inspect dataset
- ✔ Handle missing values
- ✔ Visualize data
- ✔ Check linearity
- ✔ Split dataset

---

During Training

- ✔ Choose suitable learning rate
- ✔ Choose enough iterations
- ✔ Monitor Cost
- ✔ Verify convergence

---

After Training

- ✔ Evaluate on test data
- ✔ Compute MAE
- ✔ Compute RMSE
- ✔ Compute R²
- ✔ Visualize predictions

---

# Debugging Checklist

If predictions are poor, check:

- Is the relationship actually linear?
- Is the learning rate appropriate?
- Are iterations sufficient?
- Are there outliers?
- Was the dataset split correctly?
- Are features and target correct?
- Are parameters updating?
- Is the Cost decreasing?

---

# Key Takeaways

- Linear Regression is designed for **continuous prediction**, not classification.
- Always visualize the data before training.
- Understand the difference between **Residual**, **Loss**, and **Cost**.
- Choose appropriate hyperparameters (`lr` and `it`).
- Evaluate only on **unseen test data**.
- Don't rely solely on one evaluation metric.
- Understanding the mathematics behind `fit()` and `predict()` is what distinguishes using a library from truly understanding the algorithm.