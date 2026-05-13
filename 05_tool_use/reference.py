import anthropic

TOOLS = [
    {
        "name": "get_exchange_rate",
        "description": "Get the exchange rate between two currencies",
        "input_schema": {
            "type": "object",
            "properties": {
                "from_currency": {"type": "string"},
                "to_currency": {"type": "string"},
            },
            "required": ["from_currency", "to_currency"],
        },
    }
]


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    rates = {"USD": 1.0, "EUR": 0.92, "GBP": 0.79, "JPY": 149.5}
    return rates.get(to_currency, 1.0) / rates.get(from_currency, 1.0)


def answer_with_tools(question: str, client: anthropic.Anthropic) -> str:
    messages = [{"role": "user", "content": question}]

    while True:
        response = client.messages.create(
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
                "content": str(get_exchange_rate(**block.input)),
            }
            for block in response.content
            if block.type == "tool_use"
        ]

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
