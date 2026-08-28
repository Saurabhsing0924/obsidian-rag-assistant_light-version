---
tags: [rag, llm, retrieval]
---

# RAG Systems

Retrieval-Augmented Generation (RAG) combines information retrieval with LLM generation to ground answers in specific documents, reducing hallucination.

## Pipeline

1. **Ingestion**: Split documents into chunks, embed them, store in vector DB
2. **Retrieval**: Embed the user query, find top-K most similar chunks
3. **Augmentation**: Inject retrieved chunks into the LLM prompt as context
4. **Generation**: LLM generates an answer using only the provided context

## Key Design Decisions

- **Chunk size**: Too small loses context, too large dilutes relevance
- **Top-K**: More chunks = more context but more noise and higher cost
- **Reranking**: Use a cross-encoder to re-score retrieved chunks for better precision
- **Hybrid search**: Combine vector similarity with keyword (BM25) search

## Limitations

- Can't reason across documents that aren't retrieved
- Chunking can break logical flow
- Retrieval quality is the bottleneck — garbage in, garbage out   