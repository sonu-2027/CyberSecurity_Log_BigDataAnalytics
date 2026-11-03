import pandas as pd
from pymongo import MongoClient

df = pd.read_csv("output/cleaned_cybersecurity_logs.csv")

client = MongoClient("mongodb://localhost:27017/")

db = client["cybersecurity_db"]
collection = db["security_logs"]

collection.delete_many({})

df = df.astype(object).where(pd.notnull(df), None)

records = df.to_dict("records")

if records:
    collection.insert_many(records)

print("Data loaded into MongoDB successfully!")
print("Records inserted:", len(records))

client.close()