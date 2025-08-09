from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Create a base model
model = LogisticRegression()

# Create RFE model and select the top 3 features
rfe = RFE(model, 3)
fit = rfe.fit(X, y)

print(f'Num Features: {fit.n_features_}')
print(f'Selected Features: {fit.support_}')
print(f'Feature Ranking: {fit.ranking_}')
