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
        # TODO: build messages asking the LLM to classify `description`
        #       response should be JSON: {"category": "..."}
        # TODO: call self.provider.complete(messages)
        # TODO: parse JSON and extract category
        # TODO: create Expense and return self.repo.add(expense)
        pass
