from models.dtos.base import Base
from sqlalchemy import Column, Integer, Float, String, Date, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    birth_date = Column(Date)
    register_at = Column(DateTime)
    rating = Column(Float, default=0)
    rating_avg = Column(Float, default=0)
    sold = Column(Integer, default=0)
    bought = Column(Integer, default=0)
    ads = relationship("Advertisement", back_populates="user")
    questions = relationship("Question", back_populates="user")
    deals = relationship("Deal", back_populates="redeemer")
    answers = relationship("Answer", back_populates="user")