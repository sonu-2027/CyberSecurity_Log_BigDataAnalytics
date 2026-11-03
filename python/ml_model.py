import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load cleaned data
df = pd.read_csv("output/cleaned_cybersecurity_logs.csv")

# Features used for the model
features = [
    "src_port",
    "dst_port",
    "protocol",
    "bytes_sent",
    "bytes_received",
    "is_internal_traffic"
]

X = df[features].copy()
y = df["label"]

# Convert categorical columns into numeric columns
X = pd.get_dummies(
    X,
    columns=["protocol", "is_internal_traffic"],
    drop_first=False
)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Results
print("\n=== ML MODEL RESULTS ===")
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

print("\n=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

# Predict the complete dataset
all_predictions = model.predict(X)

df["predicted_label"] = all_predictions

# Save results
df.to_csv("output/ml_predictions.csv", index=False)

print("\nML predictions saved successfully!")
print("File: output/ml_predictions.csv")
