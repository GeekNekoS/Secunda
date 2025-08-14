from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base


class Office(Base):
    __tablename__ = "office"

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    organizations = relationship("Organization", back_populates="office")
