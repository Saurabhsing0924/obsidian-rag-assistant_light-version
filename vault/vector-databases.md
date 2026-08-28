---
tags: [vectors, databases, embeddings]
---

# Vector Databases

A vector database is a specialized database optimized for storing and searching high-dimensional numerical vectors (embeddings).

## Why You Need One

Traditional databases can't efficiently answer "find the 10 most similar items to this query vector" when you have millions of vectors in 1536 dimensions. Vector databases use approximate nearest neighbor (ANN) algorithms to make this fast.

## Key Algorithms

- **HNSW** (Hierarchical Navigable Small World): Best recall/speed tradeoff, used by most modern systems
- **IVF** (Inverted File Index): Partition vectors into clusters, search only relevant clusters
- **PQ** (Product Quantization): Compress vectors to reduce memory

## Popular Options

- **ChromaDB**: Lightweight, embedded, great for prototyping
- **Pinecone**: Managed cloud service, zero-config
- **Weaviate**: Open-source, supports hybrid search
- **Qdrant**: Open-source, Rust-based, fast
- **Milvus**: Open-source, distributed, enterprise-scale   