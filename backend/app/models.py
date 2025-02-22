from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Feedback(Base):
    """Stores customer feedback with detected emotions & topics."""
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    emotion = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    adorescore = Column(Float, nullable=True)

    # Relationship with topics
    topics = relationship("Topic", back_populates="feedback")

class Topic(Base):
    """Stores topics detected from feedback."""
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    feedback_id = Column(Integer, ForeignKey("feedback.id"))
    
    feedback = relationship("Feedback", back_populates="topics")
