from collections.abc import Callable
from typing import cast

import anthropic
from anthropic.types import (
    MessageParam,
    TextBlock,
    ToolParam,
    ToolResultBlockParam,
    ToolUseBlock,
)

TOOLS: list[ToolParam] = [
    {
        "name": "add",
        "description": "Add two numbers",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "multiply",
        "description": "Multiply two numbers",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
            },
            "required": ["a", "b"],
        },
    },
]

TOOL_FUNCTIONS: dict[str, Callable[..., float]] = {
    "add": lambda a, b: a + b,
    "multiply": lambda a, b: a * b,
}


class Agent:
    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def run(self, task: str) -> str:
        messages: list[MessageParam] = [{"role": "user", "content": task}]

        while True:
            response = self.client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=512,
                tools=TOOLS,
                messages=messages,
            )

            if response.stop_reason == "end_turn":
                return cast(TextBlock, response.content[0]).text

            tool_uses = [
                cast(ToolUseBlock, b)
                for b in response.content
                if b.type == "tool_use"
            ]
            tool_results: list[ToolResultBlockParam] = [
                {
                    "type": "tool_result",
                    "tool_use_id": b.id,
                    "content": str(TOOL_FUNCTIONS[b.name](**b.input)),
                }
                for b in tool_uses
            ]

            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
