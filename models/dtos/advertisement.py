from models.dtos.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Advertisement(Base):
        __tablename__ = "ads"
        id = Column(Integer, primary_key=True)
        title = Column(String)
        description = Column(Text)
        photo_url = Column(String)
        category_id = Column(Integer, ForeignKey("categories.id"))
        category = relationship("AdvertisementCategory", back_populates="ads")
        price = Column(Integer)
        created_at = Column(DateTime)
        updated_at = Column(DateTime)
        expired_at = Column(DateTime)
        created_by_id = Column(Integer, ForeignKey("users.id"))
        user = relationship("User", back_populates="ads")
        location = Column(Integer)
        is_expired = Column(Boolean, default=False)
        is_redeemed = Column(Boolean, default=False)
        questions = relationship("Question", back_populates="advertisement")
        deals = relationship("Deal", back_populates="ad")