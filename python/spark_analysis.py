from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("CybersecurityLogAnalysis")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("output/cleaned_cybersecurity_logs.csv")
)

print("Spark loaded the cybersecurity dataset!")
print("Number of records:", df.count())

print("\nDataset schema:")
df.printSchema()

print("\nFirst 10 records:")
df.show(10, truncate=False)

spark.stop()