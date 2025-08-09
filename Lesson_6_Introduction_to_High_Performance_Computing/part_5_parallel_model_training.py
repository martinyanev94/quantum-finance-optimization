import tensorflow as tf
import numpy as np

# Simulate a large dataset
X = np.random.rand(10000, 10)
y = np.random.rand(10000, 1)

# Define a simple model
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Training function
def train_model(X_train, y_train):
    model = create_model()
    model.fit(X_train, y_train, epochs=10)

# Split data for parallel processing
num_processes = 4
chunk_size = len(X) // num_processes
chunks = [(X[i:i + chunk_size], y[i:i + chunk_size]) for i in range(0, len(X), chunk_size)]

# Train models in parallel
from multiprocessing import Pool

with Pool(num_processes) as pool:
    pool.starmap(train_model, chunks)
