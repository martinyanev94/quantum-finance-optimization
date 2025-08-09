# Check for missing values
data.isnull().sum()

# Interpolate missing values
data.interpolate(method='linear', inplace=True)

# Ensure the index is a datetime object
data.index = pd.to_datetime(data.index)
# Calculating Simple Moving Average (SMA)
data['SMA_30'] = data['Close'].rolling(window=30).mean()
data['SMA_100'] = data['Close'].rolling(window=100).mean()

# Visualizing the moving averages with closing prices
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='AAPL Close Price', color='blue', alpha=0.5)
plt.plot(data['SMA_30'], label='30-Day SMA', color='orange')
plt.plot(data['SMA_100'], label='100-Day SMA', color='red')
plt.title('Apple Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
