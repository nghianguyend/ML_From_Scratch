from visualization import plot_training_results
from gradient_descent import gradient_descent
import numpy as np


def main() :
    # Initialize dataset
    X = np.array([1.0, 2.0, 3.0])
    y_true = np.array([2.0, 5.0, 8.0])

    # Initialize parameters
    W = 2.0
    b = 1.0

    # Training model
    loss_history = []
    W_train, b_train, loss_history = gradient_descent(W, X, b, y_true)

    print(f"Trained weight after 100 iterations : {W_train}")
    print(f"Trained bias after 100 iterations : {b_train}")

    # Visualizing the training process
    plot_training_results(X, y_true, W, b, loss_history)
    


if __name__ == "__main__" :
    main()
