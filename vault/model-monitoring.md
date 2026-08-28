---
tags: [monitoring, observability, production]
---

# Model Monitoring

Model monitoring is the practice of continuously tracking a deployed model's performance, input data quality, and system health in production.

## What to Monitor

- **Data drift**: Are input features changing distribution over time?
- **Prediction drift**: Are model outputs shifting (e.g., predicting more positives)?
- **Accuracy**: Compare predictions against ground truth when available
- **Latency**: Is the model responding within SLA?
- **Fairness**: Are predictions equally accurate across demographic groups?

## Alerting Strategies

- Statistical tests (KS test, PSI) for drift detection
- Threshold-based alerts on accuracy drop
- Automated retraining triggers when drift exceeds a threshold

## Tools

- Evidently AI, WhyLabs, Arize, Fiddler
- Custom dashboards in Grafana or Datadog   