# 09. Normal Equation

## Core Idea

Gradient Descent searches for the optimal parameters iteratively.

The Normal Equation computes them directly using Linear Algebra.

---

## Matrix Form

Hypothesis

h(X) = Xθ

X → Feature Matrix

θ → Parameter Vector

Xθ → Predictions

---

## Matrix Cost Function

J(θ)

= (1 / 2n) (Xθ − y)ᵀ (Xθ − y)

Matrix representation of MSE.

---

## Normal Equation

θ = (XᵀX)⁻¹ Xᵀy

Computes the optimal parameter vector directly.

No iterative optimization required.

---

## Why It Works

Differentiate the Cost Function.

↓

Set Gradient = 0.

↓

Solve for θ.

---

## Advantages

• Exact solution

• No Learning Rate

• No Iterations

• No Convergence Issues

---

## Limitations

• Requires matrix inversion

• Computationally expensive for high-dimensional data

• XᵀX must be invertible

---

## Gradient Descent vs Normal Equation

Gradient Descent

→ Iterative optimization

→ Scales to large datasets

Normal Equation

→ Analytical solution

→ Suitable for small datasets

---

## Remember

Cost Function

↓

Differentiate

↓

Set Gradient = 0

↓

Solve for θ

↓

Optimal Parameters