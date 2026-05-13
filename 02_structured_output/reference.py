from typing import cast

import anthropic
from anthropic.types import TextBlock
from pydantic import BaseModel

CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Shopping",
    "Health",
    "Bills",
    "Other",
]


class ExpenseResult(BaseModel):
    category: str
    confidence: float
    reason: str


def classify_expense(description: str, client: anthropic.Anthropic) -> ExpenseResult:
    system = (
        f"Classify expense descriptions into one of: {', '.join(CATEGORIES)}.\n"
        'Respond with JSON only: {"category": "...", "confidence": 0.0, "reason": "..."}'
    )
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        system=system,
        messages=[{"role": "user", "content": description}],
    )
    return ExpenseResult.model_validate_json(
        cast(TextBlock, message.content[0]).text
    )
