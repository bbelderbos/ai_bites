import anthropic

CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Health", "Bills", "Other"]

# TODO: rewrite this prompt so the model returns exactly one category name, nothing else
SYSTEM_PROMPT = "Classify the expense."


def classify_with_role(description: str, client: anthropic.Anthropic) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=32,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": description}],
    )
    return message.content[0].text.strip()
