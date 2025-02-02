from models.dtos.base import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    created_by_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="answers")
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="answers")
    created_at = Column(DateTime)
