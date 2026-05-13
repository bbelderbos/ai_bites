import json
import uuid
from typing import Protocol
from pydantic import BaseModel, Field


class Expense(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    amount: float
    category: str


class LLMProvider(Protocol):
    def complete(self, messages: list[dict]) -> str: ...


class ExpenseRepo(Protocol):
    def add(self, expense: Expense) -> Expense: ...


class ClassificationService:
    def __init__(self, provider: LLMProvider, repo: ExpenseRepo):
        self.provider = provider
        self.repo = repo

    def classify_and_save(self, description: str, amount: float) -> Expense:
        messages = [
            {
                "role": "user",
                "content": f'Classify this expense: "{description}". Respond with JSON only: {{"category": "..."}}',
            }
        ]
        raw = self.provider.complete(messages)
        category = json.loads(raw)["category"]
        expense = Expense(description=description, amount=amount, category=category)
        return self.repo.add(expense)
