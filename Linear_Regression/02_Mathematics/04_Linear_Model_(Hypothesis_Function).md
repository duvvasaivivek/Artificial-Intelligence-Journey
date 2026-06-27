# 04. Linear Model (Hypothesis Function)

## Core Idea

Machine Learning learns **parameters**, not equations.

Learning = Parameter Estimation.

---

## Model

A mathematical function that maps inputs to outputs.

Unknown relationship:

f(x)

Learned approximation:

h(x)

Goal:

h(x) ≈ f(x)

---

## Hypothesis

A candidate model.

Hypothesis Space = Set of all candidate models.

Linear Regression restricts the hypothesis space to **linear functions**.

---

## Linear Model

School Mathematics

y = mx + c

↓

Machine Learning

hθ(x) = θ₀ + θ₁x

---

## Parameters

θ₀ → Bias / Intercept
• Prediction when x = 0
• Shifts the line vertically

θ₁ → Weight / Slope
• Rate of change of prediction
• Controls the slope

---

## Key Insight

Equation is fixed.

Parameters are learned.

Optimization searches for the best values of θ.

---

Remember

Unknown Function f(x)
        ↓
Choose Hypothesis h(x)
        ↓
Estimate Parameters θ
        ↓
Generate Predictions