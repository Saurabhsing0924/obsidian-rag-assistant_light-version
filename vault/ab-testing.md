---
tags: [experiments, testing, deployment]
---

# A/B Testing for ML Models

A/B testing compares two or more model versions in production by splitting traffic and measuring business metrics.

## How It Works

1. Deploy both Model A (champion) and Model B (challenger)
2. Split incoming traffic (e.g., 90/10 or 50/50)
3. Measure the business metric (conversion, CTR, revenue)
4. After statistical significance, promote the winner

## Challenges with ML

- **Non-stationarity**: User behavior changes over time, so test results may not be stable
- **Network effects**: In recommendation systems, showing different items to different users changes the pool
- **Long feedback loops**: Some metrics (churn, LTV) take weeks to observe

## Best Practices

- Run tests for at least one full business cycle
- Pre-register your primary metric to avoid p-hacking
- Use sequential testing methods for early stopping   