import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from feature_extraction import extract_features

print("Loading Kaggle Dataset...")
df = pd.read_csv('../data/phishing_site_urls.csv')
df['Label'] = df['Label'].map({'good': 0, 'bad': 1})

print("Sampling balanced data...")
# Balanced 50,000 records for high accuracy & zero false positives
df_good = df[df['Label'] == 0].sample(n=25000, random_state=42)
df_bad = df[df['Label'] == 1].sample(n=25000, random_state=42)
df_sampled = pd.concat([df_good, df_bad]).sample(frac=1, random_state=42).reset_index(drop=True)

print("Extracting features... (Wait ~20-30 secs)")
X = []
for url in df_sampled['URL']:
    X.append(extract_features(url))

y = df_sampled['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Model...")
model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")

joblib.dump(model, '../phishing_model.pkl')
print("Model retrained successfully!")