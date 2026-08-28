---
tags: [serving, inference, deployment]
---

# Model Serving

Model serving is the process of making a trained model available as an API endpoint that applications can call in real-time or batch mode.

## Batch vs Real-Time

Batch inference processes large datasets overnight (e.g., scoring 10 million users). Real-time inference responds to individual requests within milliseconds (e.g., fraud detection on a single transaction).

## Common Approaches

- **REST API**: Model wrapped in Flask/FastAPI, deployed behind a load balancer
- **Dedicated servers**: TensorFlow Serving, TorchServe, or Triton Inference Server
- **Serverless**: AWS Lambda with model loaded from S3 (cold start is the tradeoff)
- **Edge**: Model compiled to ONNX or TFLite, running on-device

## Key Metrics

- **P99 latency**: 99th percentile response time
- **Throughput**: requests per second
- **GPU utilization**: cost efficiency   