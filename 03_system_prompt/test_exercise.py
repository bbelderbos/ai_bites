from unittest.mock import MagicMock

from solution import classify_with_role, SYSTEM_PROMPT, CATEGORIES


def _mock_client(text: str) -> MagicMock:
    client = MagicMock()
    client.messages.create.return_value.content = [MagicMock(text=text)]
    return client


def test_returns_stripped_string():
    assert classify_with_role("coffee", _mock_client("  Food  ")) == "Food"


def test_system_prompt_lists_all_categories():
    for cat in CATEGORIES:
        assert cat in SYSTEM_PROMPT


def test_system_prompt_restricts_output():
    lower = SYSTEM_PROMPT.lower()
    assert "only" in lower or "nothing else" in lower or "no explanation" in lower


def test_uses_system_kwarg():
    client = _mock_client("Food")
    classify_with_role("lunch", client)
    assert client.messages.create.call_args.kwargs["system"] == SYSTEM_PROMPT
