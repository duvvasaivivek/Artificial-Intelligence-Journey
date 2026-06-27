# 02. Best Fit Line & Error Function

## Hypothesis

A candidate model that maps inputs to outputs.

Hypothesis Space = Set of all candidate models.

Linear Regression searches only linear hypotheses.

---

## Core Problem

Infinite candidate lines exist.

Need a criterion to identify the optimal hypothesis.

↓

Optimization Problem

---

## Prediction Error

Difference between observed and predicted value.

Measures prediction quality.

---

## Residual

Prediction error of a single observation.

Geometrically:
Vertical distance between the observed point and the fitted line.

---

## Limitation

Residuals cannot be summed directly.

(+10) + (-10) = 0 ❌

Sign cancellation produces misleading results.

---

## Objective Function

A scalar function that measures the quality of an entire hypothesis.

A good objective function should

• Penalize errors
• Prevent cancellation
• Compare hypotheses
• Be optimization-friendly

---

## Remember

Hypothesis Space
        ↓
Candidate Models
        ↓
Prediction Errors
        ↓
Objective Function
        ↓
Optimization
        ↓
Best Fit Line