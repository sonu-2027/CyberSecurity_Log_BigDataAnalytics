import pandas as pd

df = pd.read_csv("output/ml_predictions.csv")

summary = (
    df.groupby(["attack_type", "predicted_label"])
      .size()
      .reset_index(name="count")
)

summary.to_csv("output/dashboard_summary.csv", index=False)

print("Dashboard summary created successfully!")
print("File: output/dashboard_summary.csv")