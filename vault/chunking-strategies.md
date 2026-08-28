---
tags: [chunking, rag, ingestion]
---

# Chunking Strategies

Chunking is the process of splitting documents into smaller pieces for embedding and retrieval. It's one of the most impactful decisions in a RAG system.

## Strategies

- **Fixed-size**: Split every N tokens/words. Simple but can break sentences mid-thought.
- **Recursive**: Try splitting by paragraphs first, then sentences, then words. Preserves structure better.
- **Semantic**: Use an embedding model to detect natural topic boundaries.
- **Structure-aware**: Split by markdown headings (##, ###). Works great for Obsidian notes.

## Key Parameters

- **Chunk size**: 100–500 words is typical. Smaller = more precise, larger = more context.
- **Overlap**: 10–20% overlap prevents losing information at chunk boundaries.
- **Metadata**: Store the source file, heading, and position with each chunk for citations.

## For Obsidian Specifically

Obsidian notes are naturally structured with headings. Splitting by `##` sections and then further splitting long sections by paragraph is usually the best approach.   