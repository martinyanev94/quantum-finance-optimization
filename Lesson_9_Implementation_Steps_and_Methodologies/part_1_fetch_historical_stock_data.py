import yfinance as yf

# Define the stock ticker symbol and time period
ticker = 'AAPL'  # Apple Inc.
start_date = '2020-01-01'
end_date = '2022-01-01'

# Fetch historical data
data = yf.download(ticker, start=start_date, end=end_date)
print(data.head())
