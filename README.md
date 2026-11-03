# CyberSecurity Log Big Data Analytics

## Overview

CyberSecurity Log Big Data Analytics is a real-time log analysis pipeline that processes cybersecurity logs using Apache Kafka, Apache Spark, and Python. The project ingests streaming log data, performs analysis on security events, and generates insights to help identify potential threats and anomalous activities.

## Features

- Real-time log ingestion using Apache Kafka
- Distributed data processing with Apache Spark
- Cybersecurity event analysis
- Automated log streaming pipeline
- Detection of suspicious activities and anomalies
- Processed data storage and reporting

## Tech Stack

- Python
- Apache Kafka
- Apache Spark (PySpark)
- Big Data Analytics
- CSV Log Datasets

## Project Architecture

```text
Dataset
   │
   ▼
Kafka Producer
   │
   ▼
Apache Kafka Topic
   │
   ▼
Spark Streaming Consumer
   │
   ▼
Log Processing & Analytics
   │
   ▼
Processed Output Reports
