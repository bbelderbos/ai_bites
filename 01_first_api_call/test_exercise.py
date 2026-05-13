from unittest.mock import MagicMock, patch

from solution import get_completion


def test_returns_text():
    mock_client = MagicMock()
    mock_client.messages.create.return_value.content = [MagicMock(text="Hello, Pythonista!")]
    with patch("solution.anthropic.Anthropic", return_value=mock_client):
        assert get_completion("Say hello") == "Hello, Pythonista!"


def test_uses_correct_model():
    mock_client = MagicMock()
    mock_client.messages.create.return_value.content = [MagicMock(text="ok")]
    with patch("solution.anthropic.Anthropic", return_value=mock_client):
        get_completion("test")
    kwargs = mock_client.messages.create.call_args.kwargs
    assert kwargs["model"] == "claude-sonnet-4-6"
    assert kwargs["max_tokens"] == 256


def test_sends_user_message():
    mock_client = MagicMock()
    mock_client.messages.create.return_value.content = [MagicMock(text="ok")]
    with patch("solution.anthropic.Anthropic", return_value=mock_client):
        get_completion("What is 2+2?")
    messages = mock_client.messages.create.call_args.kwargs["messages"]
    assert messages[0]["role"] == "user"
    assert "2+2" in messages[0]["content"]
