# Creating signals
data['Signal'] = 0  # Default no position
data['Signal'][30:] = np.where(data['SMA_30'][30:] > data['SMA_100'][30:], 1, 0)  # Buy signal
data['Position'] = data['Signal'].diff()  # Identify when to buy/sell

# Plotting buy/sell signals
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='AAPL Close Price', color='blue', alpha=0.5)
plt.plot(data[data['Position'] == 1].index, 
         data['SMA_30'][data['Position'] == 1], 
         '^', markersize=10, color='g', label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, 
         data['SMA_30'][data['Position'] == -1], 
         'v', markersize=10, color='r', label='Sell Signal')
plt.title('Trading Signals for AAPL Stock')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
