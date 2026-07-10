# Linear Regression Cheat Sheet

> A quick revision guide for Linear Regression covering theory, mathematics, implementation, and evaluation.

---

# 1. What is Linear Regression?

Linear Regression is a **Supervised Machine Learning Algorithm** used to predict **continuous numerical values** by finding the best-fit straight line that describes the relationship between input features and the target variable.

### Examples

- Predict Salary from Years of Experience
- Predict House Price from Area
- Predict Sales from Advertising Budget
- Predict Temperature from Time

---

# 2. Types of Linear Regression

### Simple Linear Regression

Uses **one independent variable**.

\[
\hat y = wx + b
\]

Example:

Salary ← Years of Experience

---

### Multiple Linear Regression

Uses **multiple independent variables**.

\[
\hat y = w_1x_1+w_2x_2+\cdots+w_nx_n+b
\]

Example:

House Price ← Area + Bedrooms + Age

---

# 3. Terminology

| Symbol | Meaning |
|---------|----------|
| X | Feature / Independent Variable |
| y | Actual Target |
| ŷ | Predicted Target |
| w | Weight / Slope |
| b | Bias / Intercept |
| n | Number of Training Examples |
| α | Learning Rate |
| J(w,b) | Cost Function |

---

# 4. Workflow

```text
Collect Data
      ↓
Load Dataset
      ↓
Visualize Data
      ↓
Train-Test Split
      ↓
Initialize Parameters
      ↓
Generate Predictions
      ↓
Compute Cost
      ↓
Compute Gradients
      ↓
Update Parameters
      ↓
Repeat
      ↓
Best Fit Line
      ↓
Evaluate Model
```

---

# 5. Mathematical Flow

```text
Feature (X)
      ↓
Hypothesis Function

ŷ = wx + b

      ↓
Residual

y - ŷ

      ↓
Loss

(y - ŷ)²

      ↓
Cost Function

J(w,b)

      ↓
Partial Derivatives

∂J/∂w
∂J/∂b

      ↓
Gradient Descent

Update Parameters

      ↓
Repeat Until Convergence
```

---

# 6. Training Pipeline

```text
Initialize

w = 0
b = 0

↓

Predict

↓

Calculate Cost

↓

Compute Gradients

↓

Update Parameters

↓

Repeat

↓

Optimal Weight & Bias
```

---

# 7. Prediction Pipeline

```text
Input Feature

↓

Use Learned Parameters

↓

ŷ = wx + b

↓

Predicted Output
```

---

# 8. Gradient Descent Pipeline

```text
Predictions

↓

Residuals

↓

Loss

↓

Cost

↓

Gradients

↓

Parameter Update

↓

Repeat
```

---

# 9. Model Evaluation

Regression models are evaluated using:

### MAE

Average absolute error.

↓

Lower is better.

---

### MSE

Average squared error.

↓

Penalizes larger errors.

↓

Lower is better.

---

### RMSE

Square root of MSE.

↓

Same unit as target variable.

↓

Lower is better.

---

### R² Score

Measures how well the model explains the data.

| R² | Interpretation |
|-----|---------------|
| 1 | Perfect Fit |
| >0.9 | Excellent |
| >0.8 | Good |
| 0 | Predicting Mean |
| <0 | Poor Model |

Higher is better.

---

# 10. Scratch Implementation

Implemented manually:

- Load Dataset
- Visualize Data
- Hypothesis Function
- Cost Function
- Gradient Descent
- Training
- Prediction
- Evaluation
- Debugging

Purpose:

Understand every mathematical step.

---

# 11. Scikit-Learn Implementation

Uses built-in APIs.

```python
model = LinearRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)
```

Purpose:

Use an optimized implementation in real projects.

---

# 12. Scratch vs Scikit-Learn

| Scratch | Scikit-Learn |
|----------|--------------|
| Manual Implementation | Library Implementation |
| Educational | Production Ready |
| Full Mathematical Control | Faster Development |
| Gradient Descent Visible | Internals Hidden |

---

# 13. Important Hyperparameters

### Learning Rate (lr)

Controls the update step size.

Small lr

↓

Slow Learning

Large lr

↓

Overshoots Minimum

Good lr

↓

Smooth Convergence

---

### Iterations (it)

Number of Gradient Descent updates.

Too Few

↓

Underfitting

Too Many

↓

Longer Training Time

---

# 14. Advantages

- Easy to understand
- Fast to train
- Highly interpretable
- Good baseline model
- Works well for linear relationships

---

# 15. Limitations

- Assumes linear relationship
- Sensitive to outliers
- Cannot model complex nonlinear patterns
- Performance decreases with irrelevant features

---

# 16. Common Applications

- Salary Prediction
- House Price Prediction
- Sales Forecasting
- Demand Forecasting
- Stock Trend Approximation
- Temperature Prediction

---

# 17. Key Terms

| Term | Meaning |
|------|---------|
| Feature | Input Variable |
| Target | Output Variable |
| Weight | Slope of Line |
| Bias | Y-axis Intercept |
| Residual | Prediction Error |
| Loss | Error for One Sample |
| Cost | Average Error for Entire Dataset |
| Gradient | Direction of Maximum Increase |
| Gradient Descent | Optimization Algorithm |

---

# 18. Interview Cheat Sheet

### What is Linear Regression?

A supervised learning algorithm used to predict continuous numerical values by fitting the best possible straight line to the data.

---

### What is the objective?

Minimize the Cost Function.

---

### What is the hypothesis function?

\[
\hat y = wx+b
\]

---

### What does Gradient Descent do?

Finds the optimal values of **w** and **b** by minimizing the Cost Function.

---

### Why is MSE used?

- Removes negative errors.
- Penalizes large errors.
- Differentiable.

---

### Why divide Cost by 2?

Simplifies differentiation during Gradient Descent.

---

### Difference between Loss and Cost?

Loss

↓

Error for one training example.

Cost

↓

Average loss over the entire dataset.

---

### Why Train-Test Split?

To evaluate the model on unseen data and measure its ability to generalize.

---

### Evaluation Metrics

- MAE
- MSE
- RMSE
- R² Score

---

# 19. End-to-End Flow

```text
Data Collection
      ↓
Data Loading
      ↓
Visualization
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Gradient Descent
      ↓
Learn Parameters
      ↓
Prediction
      ↓
Evaluation
      ↓
Deployment
```

---

# 20. Final Takeaways

- Linear Regression predicts **continuous values**.
- It learns a **best-fit straight line**.
- The model minimizes the **Cost Function**.
- Gradient Descent updates **w** and **b** iteratively.
- Lower **MAE**, **MSE**, and **RMSE** indicate better performance.
- Higher **R² Score** indicates a better fit.
- Scratch implementation builds understanding.
- Scikit-Learn provides an optimized production-ready implementation.

---

## One-Line Summary

> **Linear Regression learns the best-fit line by minimizing prediction error using Gradient Descent, then uses that learned equation to predict continuous values.**