---
tags: [data, pipelines, etl]
---

# Data Pipelines

Data pipelines are automated workflows that move, transform, and load data from source systems into a format ready for model training or serving.

## Pipeline Stages

1. **Ingestion**: Pull raw data from databases, APIs, or event streams
2. **Cleaning**: Handle missing values, deduplicate, normalize formats
3. **Transformation**: Feature engineering, aggregation, encoding
4. **Storage**: Load into a data warehouse or feature store
5. **Triggering**: Signal to the training or serving system that new data is ready

## Tools

- **Orchestration**: Apache Airflow, Dagster, Prefect
- **Streaming**: Apache Kafka, AWS Kinesis
- **Batch**: Spark, dbt
- **Cloud**: AWS Glue, GCP Dataflow

## Data Drift

One of the hardest problems in pipelines is detecting when the input data distribution shifts away from what the model was trained on. This requires continuous monitoring of feature distributions.   