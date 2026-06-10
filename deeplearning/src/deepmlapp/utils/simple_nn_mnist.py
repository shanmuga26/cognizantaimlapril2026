import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras import layers, Sequential
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

def mnist_nn_process():
    # 1. Load the MNIST dataset directly from Keras
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # 2. Preprocess the image data
    # Scale pixel values to a range of 0 to 1 (replaces StandardScaler)
    x_train, x_test = x_train / 255.0, x_test / 255.0
    
    # 3. Build the Neural Network Model
    model = Sequential([
        # Flatten transforms the 2D image (28x28) into a 1D vector (784 features)
        layers.Flatten(input_shape=(28, 28)), 
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        # 10 output units for digits 0-9; softmax handles multi-class probabilities
        layers.Dense(10, activation='softmax') 
    ])
    
    # 4. Compile the model
    # Use sparse_categorical_crossentropy since labels are integers (0-9)
    model.compile(
        optimizer='adam', 
        loss='sparse_categorical_crossentropy', 
        metrics=['accuracy']
    )
    
    # 5. Train the model
    print("Training the model...")
    model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))
    
    # 6. Evaluate the model using the unseen test set
    print("\nEvaluating on Test Data...")
    loss, accuracy = model.evaluate(x_test, y_test)
    print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}\n")
    
    # 7. Predictions & Metrics
    # argmax converts probability distributions back into exact digit predictions (0-9)
    y_pred_probabilities = model.predict(x_test)
    y_pred = np.argmax(y_pred_probabilities, axis=1)
    
    # Confusion Matrix
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Classification Report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Model Summary
    print("\nModel Summary:")
    print(model.summary())

if __name__ == "__main__":
    mnist_nn_process()