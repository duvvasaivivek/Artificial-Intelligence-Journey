# 07. Partial Derivatives

## Core Idea

The Cost Function depends on multiple parameters.

J(θ₀, θ₁)

An ordinary derivative measures change with respect to one variable.

A multivariable function requires **partial derivatives**.

---

## Why Partial Derivatives?

Changing θ₀ changes the Cost.

Changing θ₁ also changes the Cost.

To study the effect of one parameter independently, all other parameters are held constant.

---

## Definition

A partial derivative measures the rate of change of a multivariable function with respect to one variable while keeping the remaining variables constant.

Notation:

∂J/∂θ₀

→ Change in Cost when only θ₀ changes.

∂J/∂θ₁

→ Change in Cost when only θ₁ changes.

---

## Why the Symbol ∂?

d  → Single-variable functions

∂ → Multivariable functions

---

## Geometric Interpretation

The Cost Function forms a surface.

A partial derivative measures the slope of the surface along a single parameter axis.

Each parameter has its own direction of change.

---

## Importance in Linear Regression

Partial derivatives tell us how each parameter influences the Cost Function.

They provide the information required to update the parameters during optimization.

---

## Key Insights

• One parameter changes at a time.

• Remaining parameters are treated as constants.

• Every learnable parameter has its own partial derivative.

• Partial derivatives form the mathematical basis of Gradient Descent.

---

## Remember

Cost Function
        ↓
Multiple Parameters
        ↓
Need Individual Rates of Change
        ↓
Partial Derivatives
        ↓
Gradient
        ↓
Gradient Descent