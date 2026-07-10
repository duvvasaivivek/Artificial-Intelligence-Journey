# Linear Regression - Final Revision

> This document is a complete end-to-end revision of Linear Regression. It summarizes the theory, mathematics, implementation, evaluation, and practical usage in one place.

---

# 1. What is Linear Regression?

Linear Regression is a **Supervised Machine Learning Algorithm** used to predict **continuous numerical values** by learning the best-fit straight line between the input feature(s) and the target variable.

Its objective is to learn a mathematical relationship that minimizes the prediction error.

---

# 2. Types of Linear Regression

## Simple Linear Regression

Uses one independent variable.

\[
\hat y = wx + b
\]

Example

Salary ← Years of Experience

---

## Multiple Linear Regression

Uses multiple independent variables.

\[
\hat y = w_1x_1+w_2x_2+\cdots+w_nx_n+b
\]

Example

House Price ← Area + Bedrooms + Age

---

# 3. Workflow

```text
Collect Data
      ↓
Load Dataset
      ↓
Understand Dataset
      ↓
Visualize Data
      ↓
Train-Test Split
      ↓
Train Model
      ↓
Generate Predictions
      ↓
Evaluate Model
      ↓
Deploy
```

---

# 4. Mathematical Workflow

```text
Feature (X)
      ↓
Hypothesis Function
      ↓
Prediction (ŷ)
      ↓
Residual
      ↓
Loss
      ↓
Cost Function
      ↓
Partial Derivatives
      ↓
Gradient
      ↓
Gradient Descent
      ↓
Updated Parameters
```

---

# 5. Important Terminology

| Symbol | Meaning |
|---------|----------|
| X | Feature |
| y | Actual Target |
| ŷ | Predicted Target |
| w | Weight (Slope) |
| b | Bias (Intercept) |
| n | Number of Samples |
| α | Learning Rate |
| J | Cost Function |

---

# 6. Core Equations

## Hypothesis Function

\[
\hat y = wx+b
\]

Predicts the output using the learned parameters.

---

## Residual

\[
Residual = y-\hat y
\]

Difference between actual and predicted values.

---

## Loss

\[
(y-\hat y)^2
\]

Measures the error for one training example.

---

## Cost Function

\[
J(w,b)=\frac1{2n}\sum(y-\hat y)^2
\]

Measures the average error across the dataset.

Objective:

Minimize this function.

---

## Weight Gradient

\[
\frac{\partial J}{\partial w}
=
-\frac2n
\sum x(y-\hat y)
\]

---

## Bias Gradient

\[
\frac{\partial J}{\partial b}
=
-\frac2n
\sum(y-\hat y)
\]

---

## Gradient Descent

\[
\theta
=
\theta
-
\alpha
\nabla J(\theta)
\]

Updates parameters iteratively to reduce the Cost.

---

# 7. Gradient Descent Pipeline

```text
Initialize Parameters

↓

Predict

↓

Residual

↓

Loss

↓

Cost

↓

Gradients

↓

Update Parameters

↓

Repeat

↓

Convergence
```

---

# 8. Scratch Implementation Flow

## Step 1

Load Dataset

---

## Step 2

Visualize Dataset

---

## Step 3

Implement

\[
\hat y = wx+b
\]

---

## Step 4

Compute Residuals

---

## Step 5

Compute Cost

---

## Step 6

Compute Gradients

---

## Step 7

Update Parameters

---

## Step 8

Repeat until convergence

---

## Step 9

Generate Predictions

---

## Step 10

Evaluate Model

---

# 9. OOP Implementation

Instead of writing everything procedurally,

we package everything into a reusable class.

Properties

- w
- b
- lr
- it

Methods

- fit()
- predict()
- score()

Purpose

Reusable implementation.

---

# 10. Scikit-Learn Workflow

```python
model = LinearRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)
```

Scikit-Learn hides

- Cost Function
- Gradient Descent
- Parameter Updates

but performs the same mathematical operations internally.

---

# 11. Scratch vs Scikit-Learn

| Scratch | Scikit-Learn |
|----------|--------------|
| Manual Implementation | Library Implementation |
| Educational | Production Ready |
| Full Mathematical Control | Optimized Code |
| Slower Development | Faster Development |

---

# 12. Evaluation Metrics

## MAE

Average absolute error.

Lower is better.

---

## MSE

Average squared error.

Penalizes larger errors.

Lower is better.

---

## RMSE

Square root of MSE.

Measured in the original unit.

Lower is better.

---

## R²

Measures how well the model explains the data.

Higher is better.

---

# 13. Hyperparameters

## Learning Rate (lr)

Controls update size.

Small

↓

Slow Learning

Large

↓

Overshooting

Optimal

↓

Stable Convergence

---

## Iterations (it)

Controls the number of Gradient Descent updates.

Too Few

↓

Underfitting

Too Many

↓

Longer Training

---

# 14. Common Applications

- Salary Prediction
- House Price Prediction
- Sales Forecasting
- Demand Forecasting
- Revenue Prediction
- Temperature Prediction

---

# 15. Advantages

- Easy to understand
- Easy to implement
- Fast training
- Highly interpretable
- Good baseline model

---

# 16. Limitations

- Assumes linear relationship
- Sensitive to outliers
- Poor for nonlinear data
- Limited expressive power

---

# 17. When to Use

Use when

- Target is continuous
- Relationship is approximately linear
- Dataset is simple
- Model interpretability is important

---

# 18. When Not to Use

Avoid when

- Classification problems
- Strong nonlinear relationships
- Highly complex datasets
- Many interacting variables

---

# 19. Common Mistakes

- Using Accuracy instead of regression metrics.
- Confusing Loss and Cost.
- Ignoring train-test split.
- Choosing a poor learning rate.
- Too few iterations.
- Ignoring outliers.
- Forgetting to evaluate on unseen data.

---

# 20. End-to-End Learning Summary

```text
Understand Problem
        ↓
Collect Dataset
        ↓
Load Dataset
        ↓
Visualize Dataset
        ↓
Understand Relationship
        ↓
Train-Test Split
        ↓
Implement Hypothesis Function
        ↓
Compute Cost Function
        ↓
Compute Gradients
        ↓
Gradient Descent
        ↓
Learn Weight & Bias
        ↓
Predict
        ↓
Evaluate
        ↓
Improve Model
        ↓
Deploy
```

---

# 21. Interview Questions

### What is Linear Regression?

A supervised learning algorithm that predicts continuous values by fitting the best-fit line.

---

### What is the objective?

Minimize the Cost Function.

---

### Why use Gradient Descent?

To iteratively find the optimal weight and bias that minimize the Cost Function.

---

### Why square the error?

- Removes negative signs.
- Penalizes larger errors.
- Makes differentiation easier.

---

### Difference between Residual, Loss, and Cost?

Residual

↓

Prediction error for one sample.

Loss

↓

Squared error for one sample.

Cost

↓

Average loss over the entire dataset.

---

### Why Train-Test Split?

To evaluate model performance on unseen data and estimate how well it generalizes.

---

### Why MSE instead of MAE during optimization?

MSE is smooth and differentiable, making Gradient Descent easier to apply.

---

### What does R² measure?

How well the regression model explains the variance in the target variable.

---

### Difference between Scratch and Scikit-Learn?

Scratch implementation builds understanding by implementing every step manually.

Scikit-Learn provides an optimized, production-ready implementation of the same algorithm.

---

# 22. Key Takeaways

- Linear Regression predicts **continuous numerical values**.
- The hypothesis function is **ŷ = wx + b**.
- Training minimizes the **Cost Function**.
- Gradient Descent learns the optimal **weight** and **bias**.
- Evaluate the model using **MAE, MSE, RMSE, and R²**.
- Always train on the training set and evaluate on the test set.
- Scratch implementation builds intuition; Scikit-Learn accelerates development.

---

# One-Line Summary

> **Linear Regression learns the best-fit line by minimizing prediction error using Gradient Descent and then uses that learned equation to predict continuous values on unseen data.**