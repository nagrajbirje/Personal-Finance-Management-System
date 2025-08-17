# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib
data = pd.read_csv("finance_dataset.csv")
X = data['description']
y = data['category']
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(X, y)
joblib.dump(model, "finance_model.pkl")
