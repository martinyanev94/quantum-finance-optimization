import tensorflow as tf
from tensorflow.keras import layers

# Sample historical price data
price_data = np.array([10, 12, 11, 13, 12, 15, 14, 16, 17])

# Prepare input data (features)
X = np.array([[x] for x in range(len(price_data) - 1)])  # Previous day prices
y = np.array([price_data[i + 1] - price_data[i] for i in range(len(price_data) - 1)])  # Price changes

# Define the model
model = tf.keras.Sequential([
    layers.Dense(8, activation='relu', input_shape=(1,)),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=50)

# Predict volatility for the next day
volatility_prediction = model.predict(np.array([[len(price_data)]]))
print(f"Predicted volatility change: {volatility_prediction[0][0]}")
