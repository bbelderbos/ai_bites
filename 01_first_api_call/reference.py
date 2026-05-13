from typing import cast

import anthropic
from anthropic.types import TextBlock


def get_completion(prompt: str) -> str:
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )
    return cast(TextBlock, message.content[0]).text
