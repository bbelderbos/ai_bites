---
level: medium
tags: [protocols, design-patterns, testing, providers]
track: agentic_ai
sequence: 6
author: Bob Belderbos & Juanjo Expósito
---

# The Provider Protocol Pattern

When your code is tightly coupled to one LLM provider, swapping is painful and testing requires live API calls. Python's `Protocol` fixes both.

```python
class LLMProvider(Protocol):
    def complete(self, messages: list[dict]) -> str: ...
```

Any class with a matching `complete` method satisfies this — no inheritance needed. Your service only sees the Protocol, never the concrete class.

**Why care?** Swap providers by changing one line at the call site. Test without hitting any API. The cohort uses this same pattern to support OpenAI and Groq side by side — once you've got the Protocol, adding a third provider is a 30-line file.

## Task

The `LLMProvider` Protocol is defined. Implement:
- `ClaudeProvider` — wraps the Anthropic SDK
- `MockProvider` — returns a fixed string and records every call in `self.calls`
