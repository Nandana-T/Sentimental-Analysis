import pytest
from app.services.topic_service import predict_topics

def test_single_topic():
    """Test prediction of a single topic."""
    result = predict_topics("The delivery was super fast and efficient!")
    assert "Delivery" in result["topics"]

def test_multiple_topics():
    """Test prediction of multiple topics."""
    result = predict_topics("The product quality is amazing, and the price is great!")
    assert "Quality" in result["topics"]
    assert "Price" in result["topics"]

def test_no_topic():
    """Test feedback that doesn't match any predefined topics."""
    result = predict_topics("I am feeling very neutral about this.")
    assert len(result["topics"]) > 0  # Should still classify something

if __name__ == "__main__":
    pytest.main()
