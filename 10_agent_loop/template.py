import anthropic

TOOLS = [
    {
        "name": "add",
        "description": "Add two numbers",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "multiply",
        "description": "Multiply two numbers",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"},
            },
            "required": ["a", "b"],
        },
    },
]

TOOL_FUNCTIONS: dict[str, callable] = {
    "add": lambda a, b: a + b,
    "multiply": lambda a, b: a * b,
}


class Agent:
    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def run(self, task: str) -> str:
        messages = [{"role": "user", "content": task}]

        while True:
            response = self.client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=512,
                tools=TOOLS,
                messages=messages,
            )

            if response.stop_reason == "end_turn":
                # TODO: return the final text
                pass

            # TODO: for each tool_use block in response.content:
            #       - look up the function in TOOL_FUNCTIONS by block.name
            #       - call it with **block.input
            #       - build a tool_result block with the string result
            # TODO: append assistant turn and tool results to messages
