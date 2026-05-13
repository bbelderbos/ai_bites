---
level: easy
tags: [pydantic, structured-output, json, classification]
track: agentic_ai
sequence: 2
author: Bob Belderbos & Juanjo Expósito
---

# Structured Outputs with Pydantic

Raw LLM text is unpredictable. Structured outputs give you typed, validated Python objects.

The pattern:
1. Define a Pydantic model for the expected shape
2. Instruct the LLM to respond with JSON matching that shape
3. Parse with `Model.model_validate_json(response)`

**Why care?** This is how production AI systems stay reliable. Instead of parsing strings, you get objects with guaranteed types and validation errors when the model goes off-script.

## Task

Complete `classify_expense(description, client)` to return an `ExpenseResult`.

The `ExpenseResult` model and `CATEGORIES` list are already defined. Your system prompt must:
- Tell the model the allowed categories
- Request JSON with the shape `{"category": "...", "confidence": 0.0, "reason": "..."}`
