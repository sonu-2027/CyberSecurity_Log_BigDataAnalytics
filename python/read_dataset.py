import pandas as pd

file_path = "../dataset/cybersecurity_logs.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Rows and columns:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())