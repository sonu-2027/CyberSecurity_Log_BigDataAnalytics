import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/cybersecurity_logs.csv")

print("Original dataset:")
print(df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove completely empty rows
df = df.dropna(how="all")

print("\nAfter cleaning:")
print(df.shape)

# Show missing values
print("\nMissing values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("output/cleaned_cybersecurity_logs.csv", index=False)

print("\nCleaned dataset saved successfully!")