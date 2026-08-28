---
tags: [mlops, devops, ml]
---

# MLOps

MLOps is the set of practices for deploying, monitoring, and maintaining machine learning models in production. It extends DevOps principles to ML-specific challenges.

## The MLOps Loop

1. **Train**: Build and evaluate models
2. **Register**: Store model artifacts in a registry (MLflow, W&B)
3. **Deploy**: Ship to staging, then production
4. **Monitor**: Track accuracy, drift, and infrastructure health
5. **Retrain**: Trigger retraining when performance degrades

## Key Challenges vs Traditional DevOps

- Non-deterministic: Same input can give different outputs (stochastic models)
- Data dependencies: Model quality depends on data quality, not just code
- Multi-stakeholder: Data scientists, engineers, and domain experts all touch the pipeline

## Platforms

- **Managed**: SageMaker Pipelines, Vertex AI Pipelines
- **Open-source**: Kubeflow, MLflow, ZenML   