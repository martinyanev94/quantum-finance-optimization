from sklearn.metrics import mean_absolute_error, mean_squared_error

# Calculating MAE and RMSE
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions, squared=False)

print(f'Mean Absolute Error: {mae}')
print(f'Root Mean Squared Error: {rmse}')
