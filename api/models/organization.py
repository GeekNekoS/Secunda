# api/models/organization.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    office_id = Column(Integer, ForeignKey("office.id"))

    office = relationship("Office", back_populates="organizations")
    phones = relationship("Phone", back_populates="organization")
    activities = relationship(
        "Activity",
        secondary="organization_activity_assoc",
        back_populates="organizations"
    )
