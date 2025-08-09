from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Preparing the features and target variable
# We predict 'Close' price based on the SMA features
X = data[['SMA_30', 'SMA_100']].iloc[100:]  # Skip the first 100 rows due to rolling mean
y = data['Close'].iloc[100:]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Creating and training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
predictions = model.predict(X_test)
