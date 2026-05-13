---
level: medium
tags: [agent, loop, tool-use, orchestration, react]
track: agentic_ai
sequence: 10
author: Bob Belderbos & Juanjo Expósito
---

# The Agent Loop

An agent is a model in a loop: think → act → observe → repeat.

The ReAct pattern (Reason + Act):
1. Send task to model with available tools
2. Model returns a final answer **or** requests a tool call
3. Execute the tool, send the result back
4. Repeat until done

This is the foundation of every AI agent — from arithmetic helpers to multi-step research pipelines.

**Why care?** This loop scales to any number of tools. Replace `add` and `multiply` with `search_web`, `query_database`, or `send_email` — the loop is identical. Understanding it here means you understand every agent framework under the hood.

## Task

Complete `Agent.run(task)`. Two arithmetic tools (`add`, `multiply`) and their schemas are already defined in `TOOLS` and `TOOL_FUNCTIONS`. Loop until the model returns `stop_reason == "end_turn"`.
