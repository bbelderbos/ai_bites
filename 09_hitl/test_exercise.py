from unittest.mock import patch

from solution import process_with_hitl, ClassificationResult


def _result(category: str = "Food", confidence: float = 0.9) -> ClassificationResult:
    return ClassificationResult(
        category=category, confidence=confidence, reason="test reason"
    )


def test_high_confidence_auto_accepts():
    assert process_with_hitl(_result(confidence=0.95)) == "Food"


def test_exact_threshold_auto_accepts():
    assert process_with_hitl(_result(confidence=0.8), threshold=0.8) == "Food"


def test_low_confidence_user_confirms():
    with patch("builtins.input", return_value=""):
        assert process_with_hitl(_result(confidence=0.5)) == "Food"


def test_low_confidence_user_confirms_with_y():
    with patch("builtins.input", return_value="y"):
        assert process_with_hitl(_result(confidence=0.3)) == "Food"


def test_low_confidence_user_overrides():
    with patch("builtins.input", return_value="Transport"):
        assert (
            process_with_hitl(_result(category="Food", confidence=0.4)) == "Transport"
        )


def test_custom_threshold():
    assert process_with_hitl(_result(confidence=0.6), threshold=0.5) == "Food"
