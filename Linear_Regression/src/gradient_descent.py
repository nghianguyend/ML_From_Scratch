import numpy as np
from predictions import predict
from gradients import compute_gradients
from mse import mse

def gradient_descent(W, X, b, y_true, lr=0.1, num_iterations=100) :

    loss_history = []

    for i in range(0, num_iterations) :

        # Calculate gradients
        dw, db = compute_gradients(X, y_true, W, b)

        # Update parameters
        W = W - lr * dw
        b = b - lr * db

        # Calculate loss after update   
        y_hat = predict(W, X, b)
        loss = mse(y_hat, y_true)

        loss_history.append(round(float(loss), 3))

    return W, b, loss_history

x = np.array([1.0, 2.0, 3.0])
y_true = np.array([2.0, 5.0, 8.0])
W = 2
b = 1

loss_history = []
W_calc, b_calc, loss_history = gradient_descent(W, x, b, y_true)
print(f"Param W after 100 iterations : {W_calc}")
print(f"Param b after 100 iterations : {b_calc}")
print(f"Recorded loss after 100 iterations : {loss_history}")
