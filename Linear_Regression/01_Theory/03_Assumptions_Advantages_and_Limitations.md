# 03. Assumptions, Advantages and Limitations

Assumptions

1. Linear Relationship
Input and output should have an approximately linear relationship.

2. Independent Observations
Each data point should be independent of others.

3. Constant Error (Homoscedasticity)
Prediction errors should have roughly the same spread.

4. Normally Distributed Errors
Residuals should approximately follow a normal distribution.

5. No Strong Multicollinearity
Input features should not be highly correlated with each other.

Advantages

• Simple and easy to understand
• Fast to train
• Easy to interpret
• Good baseline model
• Computationally efficient

Limitations

• Cannot model complex non-linear relationships
• Sensitive to outliers
• Depends on assumptions
• May underfit complex data

Use Linear Regression When

• Target is numerical
• Relationship is approximately linear
• Model interpretability is important
• Need a fast baseline model

Avoid Linear Regression When

• Target is categorical
• Relationship is highly non-linear
• Dataset contains many outliers
• Features are strongly correlated

Remember

Linear Regression is simple, fast, and interpretable—but only when the data reasonably satisfies its assumptions.