import matplotlib.pyplot as plt
from predictions import predict
import numpy as np

def plot_training_results(X, y_true, W, b, loss_history):

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left : Loss curve
    axes[0].plot(
        range(1, len(loss_history) + 1),
        loss_history,
        label="Training Loss"
    )

    axes[0].set_xlabel("Iteration")
    axes[0].set_ylabel("MSE Loss")
    axes[0].set_title("Gradient Descent Convergence")
    axes[0].legend()
    axes[0].grid(True)

    # Right : Regression line
    y_hat = predict(W, X, b)
    order = np.argsort(X)

    axes[1].scatter(X, y_true, label="Actual Data")
    axes[1].plot(
        X[order],
        y_hat[order],
        label="Predicted Line"
    )

    axes[1].set_xlabel("X (Feature)")
    axes[1].set_ylabel("Y (Target)")
    axes[1].set_title("Linear Regression")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()