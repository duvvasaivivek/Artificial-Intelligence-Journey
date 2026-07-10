# Linear Regression Formula Sheet

> A complete collection of all important mathematical formulas used in Linear Regression, along with their meanings and applications.

---

# 1. Hypothesis Function

## Formula

\[
\hat{y} = wx + b
\]

### Where

| Symbol | Meaning |
|---------|----------|
| x | Input Feature |
| y | Actual Target |
| ŷ | Predicted Target |
| w | Weight (Slope) |
| b | Bias (Intercept) |

### Purpose

Generates predictions using the learned parameters.

---

# 2. Best Fit Line

## Formula

\[
y = wx + b
\]

### Purpose

Represents the straight line that minimizes the overall prediction error.

---

# 3. Residual (Prediction Error)

## Formula

\[
Residual = y - \hat y
\]

### Purpose

Measures the difference between the actual and predicted values.

### Interpretation

Residual = 0

↓

Perfect Prediction

Residual > 0

↓

Model Underestimated

Residual < 0

↓

Model Overestimated

---

# 4. Loss Function

## Formula

\[
L = (y-\hat y)^2
\]

### Purpose

Measures the error for **one training example**.

### Why Square?

- Removes negative values.
- Penalizes larger errors more heavily.
- Makes differentiation easier.

---

# 5. Mean Squared Error (MSE)

## Formula

\[
MSE=\frac1n\sum_{i=1}^{n}(y_i-\hat y_i)^2
\]

### Where

n = Number of Training Examples

### Purpose

Measures the average squared prediction error.

### Properties

- Always ≥ 0
- Lower is better
- Penalizes large errors

---

# 6. Cost Function

## Formula

\[
J(w,b)=\frac1{2n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
\]

### Purpose

Objective function minimized during training.

### Why divide by 2?

Because

\[
\frac{d}{dx}(x^2)=2x
\]

The factor **2** cancels during differentiation, making the gradient equations cleaner.

---

# 7. Mean of Feature

## Formula

\[
\bar x=\frac1n\sum x_i
\]

### Purpose

Represents the average value of the feature.

---

# 8. Mean of Target

## Formula

\[
\bar y=\frac1n\sum y_i
\]

### Purpose

Represents the average target value.

---

# 9. Partial Derivative with respect to Weight

## Formula

\[
\frac{\partial J}{\partial w}
=
-\frac2n
\sum
x(y-\hat y)
\]

### Purpose

Determines how the Cost changes when the weight changes.

---

# 10. Partial Derivative with respect to Bias

## Formula

\[
\frac{\partial J}{\partial b}
=
-\frac2n
\sum
(y-\hat y)
\]

### Purpose

Determines how the Cost changes when the bias changes.

---

# 11. Gradient

## Formula

\[
\nabla J(w,b)
=
\left(
\frac{\partial J}{\partial w},
\frac{\partial J}{\partial b}
\right)
\]

### Purpose

Represents the direction of the steepest increase of the Cost Function.

Gradient Descent moves in the opposite direction.

---

# 12. Gradient Descent Update Rule

## Formula

\[
\theta
=
\theta
-
\alpha
\nabla J(\theta)
\]

### Where

| Symbol | Meaning |
|---------|----------|
| θ | Model Parameters |
| α | Learning Rate |
| ∇J | Gradient |

### Purpose

Updates the parameters to reduce the Cost Function.

---

# 13. Weight Update Equation

## Formula

\[
w
=
w
-
\alpha
\frac{\partial J}{\partial w}
\]

### Purpose

Updates the slope after every iteration.

---

# 14. Bias Update Equation

## Formula

\[
b
=
b
-
\alpha
\frac{\partial J}{\partial b}
\]

### Purpose

Updates the intercept after every iteration.

---

# 15. Mean Absolute Error (MAE)

## Formula

\[
MAE
=
\frac1n
\sum
|y-\hat y|
\]

### Purpose

Measures the average absolute prediction error.

### Properties

- Original unit
- Easy to interpret
- Lower is better

---

# 16. Root Mean Squared Error (RMSE)

## Formula

\[
RMSE
=
\sqrt{MSE}
\]

### Purpose

Converts MSE back to the original unit.

### Properties

- Original unit
- Lower is better

---

# 17. Total Sum of Squares (SSₜₒₜ)

## Formula

\[
SS_{tot}
=
\sum
(y-\bar y)^2
\]

### Purpose

Measures the total variation in the target variable.

---

# 18. Residual Sum of Squares (SSᵣₑₛ)

## Formula

\[
SS_{res}
=
\sum
(y-\hat y)^2
\]

### Purpose

Measures the unexplained variation after fitting the regression line.

---

# 19. R² Score

## Formula

\[
R^2
=
1-
\frac{SS_{res}}
{SS_{tot}}
\]

### Purpose

Measures how well the regression model explains the variation in the target.

### Interpretation

| R² | Meaning |
|-----|----------|
| 1 | Perfect Fit |
| >0.9 | Excellent |
| >0.8 | Good |
| 0 | Predicting Mean |
| <0 | Poor Model |

---

# 20. Learning Rate

## Symbol

\[
\alpha
\]

### Purpose

Controls the size of each Gradient Descent update.

Small α

↓

Slow Learning

Large α

↓

Overshooting

Optimal α

↓

Fast and Stable Convergence

---

# 21. Number of Iterations

## Symbol

\[
it
\]

### Purpose

Specifies how many Gradient Descent updates are performed.

Too Few

↓

Underfitting

Too Many

↓

Longer Training Time

---

# Formula Summary

| Formula | Purpose |
|----------|----------|
| ŷ = wx + b | Prediction |
| y − ŷ | Residual |
| (y − ŷ)² | Loss |
| MSE | Average Squared Error |
| J(w,b) | Cost Function |
| ∂J/∂w | Weight Gradient |
| ∂J/∂b | Bias Gradient |
| θ = θ − α∇J | Gradient Descent |
| MAE | Absolute Error |
| RMSE | Root Mean Squared Error |
| SSₜₒₜ | Total Variation |
| SSᵣₑₛ | Unexplained Variation |
| R² | Goodness of Fit |

---

# Formula Flow

```text
Input (X)
     │
     ▼
Hypothesis

ŷ = wx + b

     │
     ▼
Residual

y − ŷ

     │
     ▼
Loss

(y − ŷ)²

     │
     ▼
MSE

     │
     ▼
Cost Function

J(w,b)

     │
     ▼
Partial Derivatives

∂J/∂w
∂J/∂b

     │
     ▼
Gradient

∇J

     │
     ▼
Gradient Descent

θ = θ − α∇J

     │
     ▼
Updated Parameters

w, b

     │
     ▼
New Predictions
```

---

# Key Takeaways

- **Hypothesis Function** generates predictions.
- **Residual** measures prediction error.
- **Loss** measures error for a single sample.
- **Cost Function** measures average error across the dataset.
- **Partial Derivatives** indicate how the Cost changes.
- **Gradient Descent** minimizes the Cost by updating parameters.
- **MAE, MSE, RMSE, and R²** evaluate model performance.
- All training in Linear Regression revolves around minimizing the **Cost Function**.