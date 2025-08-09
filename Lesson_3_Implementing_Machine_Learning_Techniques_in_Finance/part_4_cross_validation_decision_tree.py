from sklearn.model_selection import cross_val_score

# Initialize the decision tree classifier
classifier = DecisionTreeClassifier()

# Perform K-Fold Cross Validation
scores = cross_val_score(classifier, X, y, cv=5)  # 5-Fold Cross Validation

print(f'Cross-Validation Accuracy Scores: {scores}')
print(f'Mean Accuracy: {scores.mean() * 100:.2f}%')
