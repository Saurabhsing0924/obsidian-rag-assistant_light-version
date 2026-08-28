---
tags: [llm, transformers, nlp]
---

# LLM Fundamentals

Large Language Models are transformer-based neural networks trained on massive text corpora to predict the next token in a sequence.

## Architecture

- **Transformer**: Uses self-attention to weigh the importance of every token relative to every other token
- **Decoder-only**: GPT-style models only use the decoder half (predict next token)
- **Parameters**: GPT-4 has an estimated 1.8 trillion parameters; LLaMA-2-70B has 70 billion

## Training Stages

1. **Pre-training**: Learn language patterns from trillions of tokens
2. **Fine-tuning**: Adapt to a specific task or domain
3. **RLHF**: Use human feedback to align outputs with user preferences

## Key Concepts

- **Tokens**: Sub-word units (roughly 0.75 words per token in English)
- **Context window**: Maximum tokens the model can process at once (4K to 200K+)
- **Temperature**: Controls randomness (0 = deterministic, 1 = more creative)
- **Top-p / Top-k**: Sampling strategies to control diversity   