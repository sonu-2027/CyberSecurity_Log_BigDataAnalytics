import json
import pandas as pd
from kafka import KafkaProducer

df = pd.read_csv("output/cleaned_cybersecurity_logs.csv")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

for record in df.to_dict("records"):
    producer.send("security_logs", value=record)

producer.flush()
producer.close()

print("Cybersecurity logs sent to Kafka successfully!")
print("Records sent:", len(df))