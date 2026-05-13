---
level: easy
tags: [prompts, system-prompt, classification, design]
track: agentic_ai
sequence: 3
author: Bob Belderbos & Juanjo Expósito
---

# System Prompt Design

A system prompt sets the model's role and constraints for the whole conversation. It's the difference between "maybe it classifies correctly" and "it always does."

A good system prompt:
- Defines the role clearly
- Lists exactly what's allowed
- Specifies output format with no room for improvisation

**Why care?** In Python you wouldn't `eval()` arbitrary strings. A tight system prompt is your API contract with the model — nail it once, trust it everywhere.

## Task

`SYSTEM_PROMPT` is currently vague. Rewrite it so `classify_with_role` consistently returns **exactly one category name** from `CATEGORIES` and nothing else.

The function body is already correct — only fix the system prompt constant.
