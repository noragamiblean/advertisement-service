from models.dtos.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class AdvertisementCategory(Base):
        __tablename__ = "categories"
        id = Column(Integer, primary_key=True)
        title = Column(String)
        ads = relationship("Advertisement", back_populates="category")
