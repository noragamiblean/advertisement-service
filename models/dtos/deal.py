from models.dtos.base import Base
from sqlalchemy import Column, Integer, Float, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Deal(Base):
        __tablename__ = "deals"
        id = Column(Integer, primary_key=True)
        ad_id = Column(Integer, ForeignKey("ads.id"))
        ad = relationship("Advertisement", back_populates="deals")
        redeemer_id = Column(Integer, ForeignKey("users.id"))
        redeemer = relationship("User", back_populates="deals")
        rating = Column(Float)
        text = Column(Text)
        redeemed_at = Column(DateTime)
