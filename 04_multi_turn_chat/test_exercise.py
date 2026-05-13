from unittest.mock import MagicMock

from solution import Chat


def _mock_client(*replies: str) -> MagicMock:
    client = MagicMock()
    client.messages.create.side_effect = [
        MagicMock(content=[MagicMock(text=r)]) for r in replies
    ]
    return client


def test_returns_response_text():
    chat = Chat(_mock_client("Hi there!"))
    assert chat.ask("Hello") == "Hi there!"


def test_history_grows_each_turn():
    chat = Chat(_mock_client("Reply 1", "Reply 2"))
    chat.ask("First")
    chat.ask("Second")
    assert len(chat.history) == 4


def test_history_alternates_roles():
    chat = Chat(_mock_client("Answer"))
    chat.ask("Question")
    assert chat.history[0]["role"] == "user"
    assert chat.history[1]["role"] == "assistant"


def test_full_history_sent_on_second_call():
    chat = Chat(_mock_client("First reply", "Second reply"))
    chat.ask("msg1")
    chat.ask("msg2")
    second_call_messages = chat.client.messages.create.call_args_list[1].kwargs["messages"]
    assert len(second_call_messages) == 3  # user, assistant, user
