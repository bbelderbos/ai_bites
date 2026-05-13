from unittest.mock import MagicMock

from solution import Agent, TOOL_FUNCTIONS


def test_add():
    assert TOOL_FUNCTIONS["add"](2, 3) == 5


def test_multiply():
    assert TOOL_FUNCTIONS["multiply"](4, 5) == 20


def _tool_call(name: str, tool_id: str, **kwargs) -> MagicMock:
    block = MagicMock()
    block.type = "tool_use"
    block.name = name
    block.id = tool_id
    block.input = kwargs
    return block


def test_returns_final_answer():
    final = MagicMock(type="text", text="The answer is 7")
    client = MagicMock()
    client.messages.create.side_effect = [
        MagicMock(stop_reason="tool_use", content=[_tool_call("add", "t1", a=3, b=4)]),
        MagicMock(stop_reason="end_turn", content=[final]),
    ]
    assert Agent(client).run("What is 3 + 4?") == "The answer is 7"


def test_tool_result_sent_to_model():
    client = MagicMock()
    client.messages.create.side_effect = [
        MagicMock(
            stop_reason="tool_use", content=[_tool_call("multiply", "t2", a=6, b=7)]
        ),
        MagicMock(stop_reason="end_turn", content=[MagicMock(type="text", text="42")]),
    ]
    Agent(client).run("What is 6 * 7?")

    last_message = client.messages.create.call_args_list[1].kwargs["messages"][-1]
    result_block = last_message["content"][0]
    assert result_block["type"] == "tool_result"
    assert result_block["content"] == "42"


def test_correct_tool_called():
    client = MagicMock()
    client.messages.create.side_effect = [
        MagicMock(stop_reason="tool_use", content=[_tool_call("add", "t3", a=10, b=5)]),
        MagicMock(stop_reason="end_turn", content=[MagicMock(type="text", text="15")]),
    ]
    Agent(client).run("10 + 5?")

    last_message = client.messages.create.call_args_list[1].kwargs["messages"][-1]
    assert last_message["content"][0]["content"] == "15"
