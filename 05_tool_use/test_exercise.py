from unittest.mock import MagicMock

from solution import answer_with_tools, get_exchange_rate


def test_usd_to_eur_rate():
    assert abs(get_exchange_rate("USD", "EUR") - 0.92) < 0.01


def test_same_currency_returns_one():
    assert get_exchange_rate("USD", "USD") == 1.0


def _tool_call(tool_id: str, **kwargs) -> MagicMock:
    block = MagicMock()
    block.type = "tool_use"
    block.id = tool_id
    block.input = kwargs
    return block


def test_returns_final_text():
    final = MagicMock(type="text", text="The rate is 0.92")
    client = MagicMock()
    client.messages.create.side_effect = [
        MagicMock(stop_reason="tool_use", content=[_tool_call("t1", from_currency="USD", to_currency="EUR")]),
        MagicMock(stop_reason="end_turn", content=[final]),
    ]
    assert answer_with_tools("USD to EUR?", client) == "The rate is 0.92"


def test_tool_result_sent_back():
    client = MagicMock()
    client.messages.create.side_effect = [
        MagicMock(stop_reason="tool_use", content=[_tool_call("t2", from_currency="USD", to_currency="GBP")]),
        MagicMock(stop_reason="end_turn", content=[MagicMock(type="text", text="done")]),
    ]
    answer_with_tools("USD to GBP?", client)
    last_message = client.messages.create.call_args_list[1].kwargs["messages"][-1]
    assert last_message["content"][0]["type"] == "tool_result"
    assert last_message["content"][0]["tool_use_id"] == "t2"
