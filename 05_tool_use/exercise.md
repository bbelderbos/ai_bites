---
level: medium
tags: [tool-use, function-calling, agentic, loop]
track: agentic_ai
sequence: 5
author: Bob Belderbos & Juanjo Expósito
---

# Tool Use (Function Calling)

Tools let Claude call your Python functions. The model decides *when* to call a tool and *what arguments* to pass — you execute it and feed the result back.

The loop:
1. Send message with tool definitions
2. If `stop_reason == "tool_use"`, execute the requested tools
3. Append the assistant turn + tool results and call again
4. Repeat until `stop_reason == "end_turn"`

**Why care?** This is how AI goes from chatbot to agent. Claude can look up live data, call external APIs, or run calculations mid-conversation — all while you stay in control of execution.

## Task

Complete `answer_with_tools(question, client)`. A `get_exchange_rate` function and its tool schema are already defined. Run the agentic loop until the model returns a final text answer.
