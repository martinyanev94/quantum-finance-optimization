import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
    'Price': [100, 102, 101, 104, 105]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Preparing the data for training
X = np.array(range(len(df))).reshape(-1, 1)  # Days since first observation
y = df['Price'].to_numpy()  # Prices

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predicting future price
future_days = np.array(range(len(df), len(df) + 5)).reshape(-1, 1)
predictions = model.predict(future_days)

# Plotting results
plt.plot(df.index, df['Price'], label='Historical Prices')
plt.plot(pd.date_range(start='2020-01-06', periods=5, freq='D'), predictions, label='Predicted Prices', color='orange')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stock Price Prediction")
plt.legend()
plt.show()
