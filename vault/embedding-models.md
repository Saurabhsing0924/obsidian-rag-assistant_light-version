---
tags: [embeddings, vector, nlp]
---

# Embedding Models

Embedding models convert text into fixed-length numerical vectors where semantic similarity is reflected as geometric closeness.

## How They Work

- Input: a text string (sentence, paragraph, or chunk)
- Output: a vector of N numbers (e.g., 1536-dim for OpenAI's model)
- Similar texts → vectors that are close in space (high cosine similarity)

## Popular Models

| Model | Dimensions | Max Tokens | Cost |
|-------|-----------|------------|------|
| OpenAI text-embedding-3-small | 1536 | 8191 | $0.02/1M tokens |
| OpenAI text-embedding-3-large | 3072 | 8191 | $0.13/1M tokens |
| sentence-transformers/all-MiniLM-L6-v2 | 384 | 256 | Free (local) |
| Cohere embed-english-v3.0 | 1024 | 1024 | $0.10/1M tokens |

## Choosing a Model

- **Small + cheap**: Good for prototyping, high-volume applications
- **Large + expensive**: Better for nuanced semantic understanding
- **Local**: No API cost, no data leaves your machine, but slower   