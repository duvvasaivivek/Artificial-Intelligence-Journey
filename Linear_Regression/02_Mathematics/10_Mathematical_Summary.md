# 10. Mathematical Summary

## The Complete Pipeline

Dataset
↓

Hypothesis Function

↓

Prediction

↓

Residual

↓

Mean Squared Error

↓

Cost Function

↓

Optimization

↓

Gradient

↓

Gradient Descent

↓

Optimal Parameters

↓

Best Fit Line

---

## Key Equations

Hypothesis

hθ(x) = θ₀ + θ₁x

Purpose:
Generate predictions.

---

Residual

y − ŷ

Purpose:
Measure prediction error.

---

MSE

Average squared residual.

Purpose:
Measure overall model error.

---

Cost Function

J(θ)

Purpose:
Evaluate parameter quality.

---

Gradient

∇J(θ)

Purpose:
Direction of steepest increase.

---

Gradient Descent

θ ← θ − α∇J(θ)

Purpose:
Update parameters to minimize Cost.

---

Normal Equation

θ = (XᵀX)⁻¹Xᵀy

Purpose:
Directly compute optimal parameters.

---

## Four Perspectives

Geometry
→ Best Fit Line

Statistics
→ Least Squares

Optimization
→ Minimize Cost

Linear Algebra
→ Matrix Solution

---

## Remember

Linear Regression is not about drawing a line.

It is about estimating the parameter vector that minimizes the Mean Squared Error using optimization or linear algebra.