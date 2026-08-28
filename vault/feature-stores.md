---
tags: [features, infrastructure]
---

# Feature Stores

A feature store is a centralized repository for ML features that can be shared across teams and used consistently in both training and serving.

## Why Feature Stores Exist

Without one, every team computes features independently. This leads to:
- Inconsistent definitions (e.g., "7-day average" means different things to different teams)
- Training-serving skew (features computed differently offline vs online)
- Wasted compute (same feature calculated 10 times)

## Architecture

- **Offline store**: Historical features for training (e.g., BigQuery, Redshift)
- **Online store**: Low-latency features for real-time inference (e.g., Redis, DynamoDB)
- **Feature registry**: Metadata catalog of all available features

## Examples

- **Tecton**: Commercial, managed
- **Feast**: Open-source, self-hosted
- **Hopsworks**: Open-source, integrated with Hopsworks platform   