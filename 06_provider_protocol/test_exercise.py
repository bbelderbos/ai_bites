from solution import MockProvider, ClaudeProvider


def test_mock_returns_fixed_response():
    provider = MockProvider(response="Food")
    assert provider.complete([{"role": "user", "content": "lunch"}]) == "Food"


def test_mock_records_calls():
    provider = MockProvider()
    messages = [{"role": "user", "content": "test"}]
    provider.complete(messages)
    provider.complete(messages)
    assert len(provider.calls) == 2


def test_mock_records_message_content():
    provider = MockProvider()
    messages = [{"role": "user", "content": "classify this"}]
    provider.complete(messages)
    assert provider.calls[0] == messages


def test_claude_provider_default_model():
    provider = ClaudeProvider()
    assert provider.model == "claude-sonnet-4-6"


def test_claude_provider_custom_model():
    provider = ClaudeProvider(model="claude-haiku-4-5-20251001")
    assert provider.model == "claude-haiku-4-5-20251001"
