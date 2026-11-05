import numpy as np
from predictions import predict

def compute_gradients(X, y_true, W, b) :

    # Calculate the predictions
    y_hat = predict(W, X, b)

    # Calculate the residuals
    r = y_hat - y_true

    # Calculate the gradients for each param w and b respectively
    dw = (2 * r * X).mean()
    db = (2 * r).mean()
    
    return dw, db
    

x = np.array([1.0, 2.0, 3.0])
y_true = np.array([2.0, 5.0, 8.0])
w = 1.0
b = 0.0

dw, db = compute_gradients(x, y_true, w, b)
print(f"The gradient with respect to parameter w is : {dw}")
print(f"The gradient with respect to parameter b is : {db}")
