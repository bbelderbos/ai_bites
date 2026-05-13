from pydantic import BaseModel


class ClassificationResult(BaseModel):
    category: str
    confidence: float
    reason: str


def process_with_hitl(result: ClassificationResult, threshold: float = 0.8) -> str:
    if result.confidence >= threshold:
        return result.category

    print(f"Low confidence ({result.confidence:.0%}): '{result.category}' — {result.reason}")
    user_input = input(
        f"Accept '{result.category}'? (Enter to confirm, or type a category): "
    ).strip()

    if not user_input or user_input.lower() == "y":
        return result.category
    return user_input
