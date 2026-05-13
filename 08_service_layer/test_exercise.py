import json

from solution import ClassificationService, Expense


class MockProvider:
    def __init__(self, category: str):
        self.calls: list = []
        self._response = json.dumps({"category": category})

    def complete(self, messages: list[dict]) -> str:
        self.calls.append(messages)
        return self._response


class MockRepo:
    def __init__(self):
        self.saved: list[Expense] = []

    def add(self, expense: Expense) -> Expense:
        self.saved.append(expense)
        return expense


def test_returns_expense():
    service = ClassificationService(MockProvider("Food"), MockRepo())
    assert isinstance(service.classify_and_save("lunch", 12.50), Expense)


def test_expense_fields():
    service = ClassificationService(MockProvider("Transport"), MockRepo())
    result = service.classify_and_save("bus ticket", 2.50)
    assert result.description == "bus ticket"
    assert result.amount == 2.50
    assert result.category == "Transport"


def test_provider_called_once():
    provider = MockProvider("Food")
    ClassificationService(provider, MockRepo()).classify_and_save("coffee", 3.0)
    assert len(provider.calls) == 1


def test_expense_saved_to_repo():
    repo = MockRepo()
    ClassificationService(MockProvider("Health"), repo).classify_and_save("pharmacy", 15.0)
    assert len(repo.saved) == 1
