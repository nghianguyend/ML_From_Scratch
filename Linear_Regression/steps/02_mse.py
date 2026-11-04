import numpy as np

def mse(y_true, y_pred) :
    r = y_true - y_pred
    r_squared = r ** 2
    return r_squared.mean()

y_pred = np.array([3.0, 5.0, 7.0])
y_true = np.array([2.0, 5.0, 8.0])
print(f"Predicted MSE : {mse(y_true, y_pred)}")

y_pred_1 = np.array([2.0, 5.0, 8.0])
y_true_1 = np.array([2.0, 5.0, 8.0])
print(f"Case predictions equal targets : {mse(y_true_1, y_pred_1)}")

y_pred_2 = np.array([2.0, 5.0, 8.0])
y_true_2 = np.array([2.0, 5.0, 8.0])