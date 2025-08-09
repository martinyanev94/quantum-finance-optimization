import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

# Load the dataset
data = pd.read_csv('stock_movement.csv')
X = data[['feature1', 'feature2', 'feature3']]  # Features for prediction
y = data['movement']  # Target variable indicating price increase or decrease

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create SVM Classifier
classifier = SVC(kernel='rbf')  # Using radial basis function kernel

# Train the model
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
