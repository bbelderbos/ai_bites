---
level: medium
tags: [hitl, human-in-the-loop, confidence, ux]
track: agentic_ai
sequence: 9
author: Bob Belderbos & Juanjo Expósito
---

# Human-in-the-Loop

AI classifications aren't always right. When the model is confident, auto-accept. When it's not, ask the human.

This pattern:
1. Check the confidence score against a threshold
2. High confidence → accept automatically
3. Low confidence → show the suggestion, let the user confirm or override

**Why care?** HITL is the difference between a trusted AI assistant and one that silently makes mistakes. The cohort's Telegram bot uses this exact flow — high confidence auto-files, low confidence sends an inline keyboard for human review.

## Task

Complete `process_with_hitl(result, threshold)`:
- If `confidence >= threshold`, return the category directly
- Otherwise print the low-confidence result and prompt the user
  - Prompt: `f"Accept '{result.category}'? (Enter to confirm, or type a category): "`
  - Empty input or `"y"` → return the suggested category
  - Anything else → return the user's input as the category
