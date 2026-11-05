import numpy as np
from predictions import predict

def compute_gradients(X, y_true, W, b) :
    y_hat = predict(W, X, b)
    r = y_hat - y_true
    dw = (2 * r * X).mean()
    db = (2 * r).mean()
    return dw, db
    

x = np.array([1.0, 2.0, 3.0])
y_true = np.array([2.0, 5.0, 8.0])
w = 1.0
b = 0.0

print(compute_gradients(x, y_true, w, b))