# 06. Optimization Landscape


### Core Idea

The Cost Function measures how well a particular parameter vector (θ) fits the training data.

Learning in Linear Regression is equivalent to finding the parameter values that minimize this function.

---

### Logical Flow

Parameter Vector (θ)
        ↓
Defines the Hypothesis Function

Hypothesis Function
        ↓
Generates Predictions

Predictions + Actual Values
        ↓
Produce Residuals

Residuals
        ↓
Squared to eliminate sign cancellation and penalize larger errors

Squared Residuals
        ↓
Summed over the entire dataset

Total Squared Error
        ↓
Averaged to obtain the Cost Function

---

### Why Divide by n?

The total squared error grows with the number of observations.

Taking the mean normalizes the error, allowing fair comparison across datasets of different sizes.

---

### Why Divide by 2?

The factor ½ is introduced solely to simplify differentiation.

It cancels the exponent 2 during gradient computation and **does not change the optimal solution**.

---

### Final Cost Function

J(θ₀, θ₁)

Measures the average squared prediction error produced by the parameter vector θ.

Input  → Parameters (θ)

Output → One scalar representing model quality.

---

### Key Insights

• The Cost Function depends on the parameters, not the input features.

• Different parameter values produce different hypotheses.

• The hypothesis with the smallest Cost Function is the Best Fit Line.

---

### Remember

Learning does **not** optimize the equation.

Learning optimizes the **parameters** of the equation.

Equation remains fixed.

↓

Parameters change.

↓

Predictions change.

↓

Cost changes.

↓

Optimization finds the parameter vector with minimum cost.