from typing import cast

import anthropic
from anthropic.types import TextBlock

CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Shopping",
    "Health",
    "Bills",
    "Other",
]

SYSTEM_PROMPT = (
    f"You are an expense classifier. "
    f"Classify the user's expense into exactly one of: {', '.join(CATEGORIES)}. "
    "Reply with the category name only — no punctuation, no explanation, nothing else."
)


def classify_with_role(description: str, client: anthropic.Anthropic) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=32,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": description}],
    )
    return cast(TextBlock, message.content[0]).text.strip()
