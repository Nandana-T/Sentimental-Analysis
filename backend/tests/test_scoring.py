import pytest
from app.services.scoring_service import calculate_adorescore

def test_positive_adorescore():
    """Test Adorescore for Positive emotion with topics."""
    result = calculate_adorescore("Positive", ["Delivery", "Quality"])
    assert result["adorescore"] == 100  # Max capped at 100

def test_neutral_adorescore():
    """Test Adorescore for Neutral emotion with topics."""
    result = calculate_adorescore("Neutral", ["Delivery"])
    assert result["adorescore"] == 60  # 50 + 10*1 = 60

def test_negative_adorescore():
    """Test Adorescore for Negative emotion with topics."""
    result = calculate_adorescore("Negative", ["Price", "Customer Service"])
    assert result["adorescore"] == 20  # 0 + 10*2 = 20

def test_no_topics():
    """Test Adorescore when no topics are detected."""
    result = calculate_adorescore("Positive", [])
    assert result["adorescore"] == 100  # 100 + 10*0 = 100

if __name__ == "__main__":
    pytest.main()
