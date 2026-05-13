import anthropic
from pydantic import BaseModel

CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Health", "Bills", "Other"]


class ExpenseResult(BaseModel):
    category: str
    confidence: float
    reason: str


def classify_expense(description: str, client: anthropic.Anthropic) -> ExpenseResult:
    # TODO: build a system prompt that lists CATEGORIES and requests JSON output
    # TODO: call client.messages.create with system prompt + description as user message
    # TODO: parse and return with ExpenseResult.model_validate_json(...)
    pass
