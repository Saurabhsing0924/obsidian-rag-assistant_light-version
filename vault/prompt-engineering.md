---
tags: [prompts, llm, techniques]
---

# Prompt Engineering

Prompt engineering is the practice of crafting input instructions to LLMs to elicit the most accurate, useful, and reliable outputs.

## Core Techniques

- **Zero-shot**: Give the task directly with no examples
- **Few-shot**: Provide 2–5 examples of input→output pairs in the prompt
- **Chain-of-thought**: Ask the model to "think step by step" before answering
- **Role prompting**: Assign a persona ("You are a senior ML engineer...")
- **Structured output**: Request JSON, XML, or specific formatting

## Best Practices

- Be specific and explicit about what you want
- Provide constraints ("Answer in 3 sentences max")
- Put important instructions at the beginning AND end of the prompt
- Use delimiters (```, ---, XML tags) to separate context from instructions
- Iterate: test with 10+ examples before shipping

## Common Failure Modes

- **Instruction following**: Model ignores part of the prompt
- **Hallucination**: Model fabricates facts not in the context
- **Sycophancy**: Model agrees with the user even when wrong   