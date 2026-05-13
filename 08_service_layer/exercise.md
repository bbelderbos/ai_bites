---
level: medium
tags: [service-layer, dependency-injection, orchestration]
track: agentic_ai
sequence: 8
author: Bob Belderbos & Juanjo Expósito
---

# The Service Layer

Services orchestrate. They sit between your interfaces (CLI, API, bot) and your infrastructure (LLM providers, databases).

A service:
- Accepts interfaces (Protocol types), not concrete implementations — this is dependency injection
- Handles the "what" — call LLM → parse → save → return
- Is ignorant of *how* storage works or *which* model is called

**Why care?** The same `ClassificationService` powers the cohort's CLI, Telegram bot, and REST API without any changes. Swap `MockProvider` for `ClaudeProvider` at the call site — nothing else changes.

## Task

Complete `classify_and_save(description, amount)`:
1. Build a message asking the LLM to classify the description, requesting JSON `{"category": "..."}`
2. Call `self.provider.complete(messages)`
3. Parse the JSON to extract the category
4. Create and save an `Expense` via `self.repo.add()`
5. Return the saved expense
