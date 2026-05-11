import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sys

def main():
    try:
        # Load MNIST dataset (downloads automatically if not present)
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

        # Normalize pixel values to range [0, 1]
        x_train = x_train.astype("float32") / 255.0
        x_test = x_test.astype("float32") / 255.0

        # Flatten 28x28 images into 784-dimensional vectors
        x_train = x_train.reshape(-1, 28 * 28)
        x_test = x_test.reshape(-1, 28 * 28)

        # Build a simple feedforward neural network
        model = keras.Sequential([
            layers.Input(shape=(784,)),
            layers.Dense(128, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')  # 10 classes for digits 0-9
        ])

        # Compile the model
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        # Train the model
        print("Training the model...")
        model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

        # Evaluate the model
        print("\nEvaluating on test data...")
        test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
        print(f"Test accuracy: {test_acc:.4f}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
