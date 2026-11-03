import numpy as np

def predict(w, x, b) :
    y = w * x + b
    return y

x = np.array([1.0, 2.0, 3.0])
w = 2.0
b = 1.0

y_pred = np.array([3.0, 5.0, 7.0])
y_true = np.array([2.0, 5.0, 8.0])