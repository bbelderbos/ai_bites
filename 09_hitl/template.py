from pydantic import BaseModel


class ClassificationResult(BaseModel):
    category: str
    confidence: float
    reason: str


def process_with_hitl(result: ClassificationResult, threshold: float = 0.8) -> str:
    # TODO: if confidence >= threshold, return category directly
    # TODO: otherwise print the low-confidence result and prompt:
    #       f"Accept '{result.category}'? (Enter to confirm, or type a category): "
    # TODO: empty input or "y" → return result.category
    # TODO: anything else → return the user's input
    pass
