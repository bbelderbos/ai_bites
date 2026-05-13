import anthropic


class Chat:
    def __init__(self, client: anthropic.Anthropic):
        self.client = client
        self.history: list[dict] = []

    def ask(self, user_msg: str) -> str:
        # TODO: append {"role": "user", "content": user_msg} to self.history
        # TODO: call self.client.messages.create with the full self.history
        # TODO: extract the assistant text from the response
        # TODO: append {"role": "assistant", "content": text} to self.history
        # TODO: return the text
        pass
