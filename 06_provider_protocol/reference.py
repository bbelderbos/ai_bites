from typing import Protocol, cast

import anthropic
from anthropic.types import MessageParam, TextBlock


class LLMProvider(Protocol):
    def complete(self, messages: list[dict]) -> str: ...


class ClaudeProvider:
    def __init__(self, model: str = "claude-sonnet-4-6"):
        self.model = model
        self.client = anthropic.Anthropic()

    def complete(self, messages: list[dict]) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=cast(list[MessageParam], messages),
        )
        return cast(TextBlock, response.content[0]).text


class MockProvider:
    def __init__(self, response: str = "mocked"):
        self.response = response
        self.calls: list[list[dict]] = []

    def complete(self, messages: list[dict]) -> str:
        self.calls.append(messages)
        return self.response
