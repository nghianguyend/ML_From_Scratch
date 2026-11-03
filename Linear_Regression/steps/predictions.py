import numpy as np

def predict(w, x, b) :
    y = w * x + b
    return y

x = np.array([1.0, 2.0, 3.0])
w = 2.0
b = 1.0

predictions = predict(w, x, b)
print(predictions)
print(predictions.shape)