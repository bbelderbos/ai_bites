import uuid
from typing import Protocol
from pydantic import BaseModel, Field


class Expense(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    amount: float
    category: str


class ExpenseRepo(Protocol):
    def add(self, expense: Expense) -> Expense: ...
    def get(self, expense_id: str) -> Expense | None: ...
    def list_all(self) -> list[Expense]: ...
    def delete(self, expense_id: str) -> bool: ...


class InMemoryExpenseRepo:
    def __init__(self):
        self._store: dict[str, Expense] = {}

    def add(self, expense: Expense) -> Expense:
        # TODO
        pass

    def get(self, expense_id: str) -> Expense | None:
        # TODO
        pass

    def list_all(self) -> list[Expense]:
        # TODO
        pass

    def delete(self, expense_id: str) -> bool:
        # TODO
        pass
