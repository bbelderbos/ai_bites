import anthropic
from typing import Protocol


class LLMProvider(Protocol):
    def complete(self, messages: list[dict]) -> str: ...


class ClaudeProvider:
    def __init__(self, model: str = "claude-sonnet-4-6"):
        # TODO: store model, create self.client = anthropic.Anthropic()
        pass

    def complete(self, messages: list[dict]) -> str:
        # TODO: call client.messages.create and return the text
        pass


class MockProvider:
    def __init__(self, response: str = "mocked"):
        # TODO: store response, init self.calls = []
        pass

    def complete(self, messages: list[dict]) -> str:
        # TODO: append messages to self.calls, return self.response
        pass
