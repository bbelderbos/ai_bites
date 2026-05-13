from typing import cast

import anthropic
from anthropic.types import MessageParam, TextBlock


class Chat:
    def __init__(self, client: anthropic.Anthropic):
        self.client = client
        self.history: list[MessageParam] = []

    def ask(self, user_msg: str) -> str:
        self.history.append({"role": "user", "content": user_msg})
        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            messages=list(self.history),
        )
        text = cast(TextBlock, response.content[0]).text
        self.history.append({"role": "assistant", "content": text})
        return text
