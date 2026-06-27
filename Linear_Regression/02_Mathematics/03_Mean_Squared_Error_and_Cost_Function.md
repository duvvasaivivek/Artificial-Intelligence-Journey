# 03. Mean Squared Error (MSE) & Cost Function

## Objective

Find the hypothesis that minimizes prediction error.

↓

Need an Objective Function.

---

## Residual

Residual = Actual − Predicted

Measures error for one observation.

---

## Why Not Sum Errors?

Positive and negative residuals cancel.

↓

Not a valid objective.

---

## Why Square Errors?

• Removes negative signs
• Penalizes larger errors
• Differentiable (required for Gradient Descent)
• Produces a convex objective for Linear Regression

---

## Why Take the Mean?

Without taking the mean, the total squared error increases with the number of samples.

Example:

Dataset A → 100 samples → SSE = 500

Dataset B → 10,000 samples → SSE = 50,000

The second model is **not necessarily worse**—it simply has more observations.

Taking the mean normalizes the error, making performance comparable across datasets of different sizes.

---

## Mean Squared Error (MSE)

MSE = Average of squared residuals.

Process

Residual
→ Square
→ Sum
→ Divide by Number of Samples

---

## Loss vs Cost

Loss
→ Error for one sample.

Cost
→ Average loss over the entire dataset.

---

## Why MSE?

• Eliminates sign cancellation
• Penalizes larger errors
• Normalizes across dataset sizes
• Convex for Linear Regression
• Differentiable, enabling Gradient Descent

---

## Optimization Goal

Find the parameters that minimize the Cost Function.

arg min J(θ)

---

## Remember

Residual
↓

Loss
↓

Cost (MSE)
↓

Optimization
↓

Best Model