import json
from unittest.mock import MagicMock

from solution import classify_expense, ExpenseResult, CATEGORIES


def _mock_client(payload: dict) -> MagicMock:
    client = MagicMock()
    client.messages.create.return_value.content = [MagicMock(text=json.dumps(payload))]
    return client


def test_returns_expense_result():
    client = _mock_client({"category": "Food", "confidence": 0.95, "reason": "meal"})
    assert isinstance(classify_expense("lunch at Pret", client), ExpenseResult)


def test_category_field():
    client = _mock_client({"category": "Transport", "confidence": 0.9, "reason": "bus"})
    result = classify_expense("bus pass", client)
    assert result.category in CATEGORIES


def test_confidence_is_float():
    client = _mock_client(
        {"category": "Health", "confidence": 0.8, "reason": "pharmacy"}
    )
    result = classify_expense("pharmacy", client)
    assert 0.0 <= result.confidence <= 1.0


def test_system_prompt_includes_all_categories():
    client = _mock_client({"category": "Other", "confidence": 0.5, "reason": "unknown"})
    classify_expense("mystery purchase", client)
    system = client.messages.create.call_args.kwargs["system"]
    assert all(cat in system for cat in CATEGORIES)
