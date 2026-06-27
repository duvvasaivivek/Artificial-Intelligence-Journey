# 05. Cost Function Derivation

## Goal

Estimate the optimal parameter vector θ.

Learning = Optimization.

---

## Hypothesis

hθ(x) = θ₀ + θ₁x

Prediction depends on θ.

↓

Residual depends on θ.

---

## Residual

Residual = Actual − Prediction

= yᵢ − hθ(xᵢ)

Measures error for one observation.

---

## Squared Residual

(yᵢ − hθ(xᵢ))²

Why?

• Removes sign cancellation
• Penalizes large errors quadratically

---

## Cost Function Derivation

Residual
↓

Square

↓

Σ (Total Squared Error)

↓

÷ n (Normalization)

↓

× ½ (Simplifies differentiation)

↓

J(θ)

---

## Final Cost Function

J(θ₀, θ₁)

= (1 / 2n) Σ (yᵢ − hθ(xᵢ))²

Input  → θ

Output → Model Error

---

## Why Divide by n?

Without normalization:

More samples ⇒ Larger total error.

Cannot compare models trained on different dataset sizes.

Mean makes the objective scale-independent.

---

## Why Divide by 2?

Purely for mathematical convenience.

During differentiation,

2 × ½ = 1

Simplifies the gradient.

Does NOT affect the minimum.

---

## Key Insight

J(θ) is **not a function of x**.

It is a function of θ.

Changing θ

↓

Changes Predictions

↓

Changes Residuals

↓

Changes Cost

---

## Optimization Objective

arg min J(θ)

Find the parameter values that produce the minimum cost.

---

## Mental Model

θ
↓

Hypothesis

↓

Prediction

↓

Residual

↓

Squared Residual

↓

Cost

↓

Optimization

↓

Best Fit Line