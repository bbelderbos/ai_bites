---
level: easy
tags: [conversation, history, multi-turn, messages]
track: agentic_ai
sequence: 4
author: Bob Belderbos & Juanjo Expósito
---

# Multi-turn Conversations

A single message is a prompt. A conversation is a sequence of messages where the model sees everything that came before.

Claude uses an alternating `user` / `assistant` list. After each response:
1. Append the user message to history
2. Call the API with the full history
3. Append the assistant reply
4. Send everything again on the next turn

**Why care?** Without history, your assistant forgets after one message. Every real chatbot needs this pattern — and getting the alternation order wrong breaks the API.

## Task

Complete the `Chat` class:
- `history` starts empty
- `ask(user_msg)` appends the user message, calls the API with full history, appends the reply, returns the text
