from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

""" 
The code generates a sample dataset using NumPy's random function. The dataset consists of 100 samples, 
each with two features (represented by the X matrix) and a corresponding target value (represented by the y vector). 
The target values are generated as a linear combination of the two features, with some added Gaussian noise. 
"""

# Generate sample data
X = np.random.rand(100, 2)
y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.normal(0, 1, 100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
print('Coefficient of determination (R-squared):', model.score(X_test, y_test))
