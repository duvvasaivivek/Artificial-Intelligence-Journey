# 08. Gradient Descent

## Core Idea

Gradient Descent is an iterative optimization algorithm used to minimize the Cost Function by updating the model parameters.

Learning = Repeatedly moving toward lower Cost.

---

## Gradient

The Gradient is a vector containing the partial derivatives of the Cost Function with respect to every parameter.

∇J(θ)

Properties

• Points in the direction of steepest increase.
• Magnitude indicates how steep the increase is.

---

## Why Negative Gradient?

Goal

Minimize the Cost Function.

Gradient → Steepest Increase

↓

Move in the opposite direction.

Negative Gradient

↓

Steepest Decrease

---

## Update Rule

θ ← θ − α∇J(θ)

where

θ → Parameter vector

α → Learning Rate

∇J(θ) → Gradient

---

## Learning Rate (α)

Controls the step size.

Small α
→ Slow convergence

Large α
→ Faster updates but may overshoot

Very Large α
→ Divergence

---

## Convergence

Stop when

• Cost stops decreasing significantly
• Gradient is approximately zero
• Maximum iterations are reached

---

## Types of Gradient Descent

Batch
→ Uses the entire dataset

Stochastic (SGD)
→ Uses one sample

Mini-Batch
→ Uses a subset of samples

---

## Why It Works

Linear Regression + MSE

↓

Convex Cost Function

↓

One Global Minimum

↓

Gradient Descent converges to the optimal parameters (with an appropriate learning rate).

---

## Remember

Current Parameters

↓

Compute Gradient

↓

Move Along Negative Gradient

↓

Update Parameters

↓

Reduce Cost

↓

Repeat Until Convergence