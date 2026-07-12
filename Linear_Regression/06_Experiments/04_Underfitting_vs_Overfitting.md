# Underfitting vs Overfitting

## Objective

The objective of this experiment is to understand how the complexity of a machine learning model affects its ability to learn from data.

We compare three polynomial regression models with different degrees:

- Degree 1
- Degree 3
- Degree 12

Although Polynomial Regression is used, the underlying learning algorithm is still **Linear Regression**.

---

# Why Polynomial Regression?

A Simple Linear Regression model learns only a straight line.

\[
\hat y = wx+b
\]

This model has limited flexibility.

To increase flexibility, we create additional polynomial features from the original feature.

Example:

Original Feature

\[
x
\]

Degree 2

\[
x,\;x^2
\]

Degree 3

\[
x,\;x^2,\;x^3
\]

The model now learns

\[
\hat y=w_0+w_1x+w_2x^2+w_3x^3
\]

Although the resulting graph is curved, the model remains **Linear Regression** because it is linear with respect to the parameters (weights).

---

# Loading the Dataset

The Salary Dataset is loaded using Pandas.

The feature is

- YearsExperience

The target is

- Salary

The objective is to learn the relationship between experience and salary.

---

# Choosing Different Polynomial Degrees

Three polynomial degrees are selected.

## Degree 1

Represents a straight line.

Very simple model.

Likely to underfit.

---

## Degree 3

Adds moderate flexibility.

Usually captures the trend well.

Often provides a good balance between bias and variance.

---

## Degree 12

Very flexible.

Can pass close to almost every training sample.

May start learning noise instead of the true relationship.

Likely to overfit.

---

# Creating the Figure

A Matplotlib figure is created before plotting.

Every regression curve will be drawn on the same graph.

This allows direct visual comparison between different model complexities.

---

# Plotting the Dataset

The original observations are displayed as black scatter points.

Each point represents

- X-axis → Years of Experience
- Y-axis → Salary

These points represent the actual training data.

---

# Generating Smooth X Values

The original dataset contains only a small number of samples.

If predictions are generated only for those samples, the curve will appear rough.

Instead, many evenly spaced X-values are generated using

```python
np.linspace()
```

This creates a smooth sequence between the minimum and maximum Years of Experience.

Example

```text
1.2
1.3
1.4
1.5
...
10.6
```

The values are reshaped because Scikit-Learn expects input data in the format

```
(Number of Samples, Number of Features)
```

instead of a one-dimensional array.

---

# Generating Polynomial Features

The PolynomialFeatures class creates additional columns from the original feature.

Example

Original Feature

| x |
|---|

Degree 2

| x | x² |

Degree 3

| x | x² | x³ |

Higher polynomial degrees generate more features.

These additional features allow the regression model to learn more complex relationships.

---

# Training the Model

A new Linear Regression model is trained for every polynomial degree.

The model learns the optimal coefficients for every polynomial feature.

For example,

Degree 3 learns

\[
\hat y=w_0+w_1x+w_2x^2+w_3x^3
\]

The optimization process is still Ordinary Least Squares (OLS).

---

# Predicting the Curve

Predictions are generated for the smooth X-values created earlier.

These predictions produce a smooth regression curve instead of isolated prediction points.

---

# Plotting Each Polynomial Curve

Every trained model is plotted on the same graph.

This allows us to compare

- Simple model
- Moderately complex model
- Highly complex model

using one visualization.

---

# Understanding Underfitting

A model underfits when it is too simple to capture the relationship in the data.

Characteristics

- High Bias
- Low Variance
- Large Training Error
- Large Testing Error

Example

Degree 1 may not capture nonlinear patterns.

The model ignores important trends.

---

# Understanding Good Fit

A good model captures the underlying relationship without learning random noise.

Characteristics

- Balanced Bias
- Balanced Variance
- Low Training Error
- Low Testing Error

Degree 3 often demonstrates this behavior.

---

# Understanding Overfitting

A model overfits when it becomes excessively complex.

Instead of learning the underlying relationship, it starts memorizing individual training samples.

Characteristics

- Very Low Training Error
- High Testing Error
- High Variance
- Poor Generalization

Degree 12 often produces this behavior.

---

# Bias-Variance Tradeoff

Increasing model complexity decreases bias but increases variance.

```text
Model Too Simple
        ↓
High Bias
        ↓
Underfitting

--------------------------

Balanced Model
        ↓
Good Generalization

--------------------------

Model Too Complex
        ↓
High Variance
        ↓
Overfitting
```

The objective is to find the balance where both bias and variance remain reasonably low.

---

# Key Observations

Degree 1

- Straight regression line.
- Too simple for complex relationships.
- Underfitting.

Degree 3

- Smooth curve.
- Captures the trend.
- Good generalization.

Degree 12

- Highly irregular curve.
- Fits almost every training point.
- Learns noise.
- Overfitting.

---

# Key Takeaways

- Increasing polynomial degree increases model complexity.
- A simple model may underfit.
- An overly complex model may overfit.
- Polynomial Regression is still Linear Regression because it remains linear in the parameters.
- The best model is one that generalizes well to unseen data rather than memorizing the training data.