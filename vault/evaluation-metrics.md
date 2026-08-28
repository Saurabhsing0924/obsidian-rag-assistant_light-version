---
tags: [evaluation, metrics, rag]
---

# Evaluation Metrics for RAG

Evaluating a RAG system requires measuring both retrieval quality and generation quality separately.

## Retrieval Metrics

- **Recall@K**: Did the correct chunk appear in the top K results?
- **MRR** (Mean Reciprocal Rank): How high was the correct chunk ranked?
- **NDCG**: Does the ranking order make sense (most relevant first)?

## Generation Metrics

- **Faithfulness**: Is the answer grounded in the retrieved context? (No hallucination)
- **Relevance**: Does the answer actually address the question?
- **Completeness**: Does it cover all aspects of the question?

## Tools

- **RAGAS**: Open-source framework for automated RAG evaluation
- **LangSmith**: LLM observability + evaluation platform
- **Manual**: Always include human evaluation for final quality check

## Golden Rule

If retrieval is bad, no amount of prompt engineering will fix the answer. Fix retrieval first.   