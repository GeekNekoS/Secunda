from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organization.id"))
    phone = Column(String, nullable=False)

    organization = relationship("Organization", back_populates="phones")
