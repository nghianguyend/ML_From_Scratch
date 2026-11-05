import numpy as np


def predict(W, X, b) :
    # Calculate y_hat
    y_hat = W * X + b
    return y_hat

x = np.array([1.0, 2.0, 3.0])
w = 2.0
b = 1.0

y_pred = np.array([3.0, 5.0, 7.0])
y_true = np.array([2.0, 5.0, 8.0])