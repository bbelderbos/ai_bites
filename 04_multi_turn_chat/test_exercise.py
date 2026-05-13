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
    captured: list[list[dict]] = []
    replies = iter(["First reply", "Second reply"])

    def fake_create(**kwargs):
        captured.append(list(kwargs["messages"]))
        return MagicMock(content=[MagicMock(text=next(replies))])

    client = MagicMock()
    client.messages.create.side_effect = fake_create

    chat = Chat(client)
    chat.ask("msg1")
    chat.ask("msg2")

    assert len(captured[1]) == 3  # user, assistant, user
