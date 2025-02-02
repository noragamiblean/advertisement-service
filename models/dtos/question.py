from models.dtos.base import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Question(Base):
        __tablename__ = "questions"
        id = Column(Integer, primary_key=True)
        text = Column(Text)
        created_by_id = Column(Integer, ForeignKey("users.id"))
        user = relationship("User", back_populates="questions")
        advertisement_id = Column(Integer, ForeignKey("ads.id"))
        advertisement = relationship("Advertisement", back_populates="questions")
        created_at = Column(DateTime)
        answers = relationship("Answer", back_populates="question")
