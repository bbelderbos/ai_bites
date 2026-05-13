---
level: easy
tags: [api, anthropic, claude, messages]
track: agentic_ai
sequence: 1
author: Bob Belderbos & Juanjo Expósito
---

# Your First Claude API Call

The Anthropic Python SDK lets you call Claude in a few lines. At its core:

- Create a client: `anthropic.Anthropic()`
- Send messages: `client.messages.create(...)`
- Read the reply: `message.content[0].text`

**Why care?** This is the foundation of every AI-powered app. Structured outputs, tool use, agents — everything builds on this one pattern.

## Task

Complete `get_completion(prompt)` so it calls Claude and returns the text response.

Requirements:
- Model: `claude-sonnet-4-6`
- `max_tokens=256`
- Return the text of the first content block
