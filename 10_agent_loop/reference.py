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
                return response.content[0].text

            tool_results = [
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(TOOL_FUNCTIONS[block.name](**block.input)),
                }
                for block in response.content
                if block.type == "tool_use"
            ]

            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})
