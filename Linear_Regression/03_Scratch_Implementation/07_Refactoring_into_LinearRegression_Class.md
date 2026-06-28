# 07. Refactoring into a LinearRegression Class

## Objective

Until now, we implemented Linear Regression using procedural programming, where variables and logic were written directly in the program.

In this file, we will reorganize the same implementation using **Object-Oriented Programming (OOP)**.

**Important:**
The Linear Regression algorithm does **not** change. Only the way we organize the code changes.

---

# Why Refactor?

Our previous implementation looked like this:

```python
weight = 0
bias = 0

predictions = weight * X + bias
```

This works well for one model.

However, if we wanted multiple Linear Regression models, we would need separate variables for each one.

```python
weight1, bias1
weight2, bias2
weight3, bias3
```

Managing many variables quickly becomes difficult.

A class solves this problem by grouping everything related to one model together.

---

# What is a Class?

A **class** is a blueprint for creating objects.

It defines:

* What data an object stores.
* What actions an object can perform.

For our Linear Regression model,

**Data**

* Weight
* Bias
* Learning Rate
* Number of Iterations

**Actions**

* Train the model (`fit()`)
* Make predictions (`predict()`)

A class does not create a model.

It only defines how a model should look.

---

# What is an Object?

An **object** is an actual instance created from a class.

Example:

```python
model = LinearRegression()
```

Now `model` is a real Linear Regression model with its own:

* Weight
* Bias
* Learning Rate
* Iterations

We can create multiple independent models.

```python
model1 = LinearRegression()
model2 = LinearRegression()
```

Each object stores its own parameters.

---

# What is **init**()?

`__init__()` is called the **constructor**.

It runs automatically whenever an object is created.

Example:

```python
model = LinearRegression()
```

Python automatically executes

```python
__init__()
```

Its purpose is to initialize the model before training begins.

For Linear Regression, we initialize:

* Learning Rate
* Number of Iterations
* Weight
* Bias

---

# What is self?

`self` refers to the **current object**.

Whenever you see

```python
self.weight
```

read it as

> **This model's weight**

Similarly,

```python
self.bias
```

means

> **This model's bias**

---

# Why self.weight instead of weight?

Without classes

```python
weight = 0
```

The variable exists independently.

With classes

```python
self.weight = 0
```

The variable belongs to the current model.

This allows multiple Linear Regression models to exist without interfering with one another.

---

# What is fit()?

`fit()` is responsible for training the model.

It performs Gradient Descent repeatedly to learn the optimal values of:

* Weight
* Bias

The same Gradient Descent algorithm from the previous file is simply moved inside this method.

---

# What is predict()?

`predict()` implements the hypothesis function.

Mathematically,

[
\hat{y}=wx+b
]

In code,

```python
return self.weight * X + self.bias
```

It generates predictions using the learned parameters.

---

# Program Flow

```
Create Model
      │
      ▼
Initialize Parameters (__init__)
      │
      ▼
Train Model (fit)
      │
      ▼
Learn Weight and Bias
      │
      ▼
Predict (predict)
      │
      ▼
Generate Predictions
```

---

# Mapping Procedural Code to OOP

| Procedural Programming | Object-Oriented Programming |
| ---------------------- | --------------------------- |
| `weight`               | `self.weight`               |
| `bias`                 | `self.bias`                 |
| Gradient Descent Loop  | `fit()`                     |
| Hypothesis Function    | `predict()`                 |

---

# Advantages of Using Classes

* Better code organization.
* Reusable implementation.
* Multiple models can exist independently.
* Easier to maintain and extend.
* Similar to how machine learning libraries such as Scikit-learn are designed.

---

# Key Takeaways

* A class is a blueprint.
* An object is a real instance of that blueprint.
* `__init__()` initializes object variables.
* `self` refers to the current object.
* `fit()` trains the model.
* `predict()` generates predictions.
* Only the code organization changes; the Linear Regression mathematics remains exactly the same.

---

# Final Thought

Think of procedural programming as writing instructions directly.

Think of Object-Oriented Programming as packaging those instructions into a reusable machine.

We did **not** create a new algorithm.

We simply transformed our working Linear Regression implementation into a reusable and professional software design.
