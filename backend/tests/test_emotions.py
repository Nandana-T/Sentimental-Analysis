from app.services.emotion_service import predict_emotion

def test_emotion_detection():
    result = predict_emotion("I love this product!")
    assert result["emotion"] == "Positive"
