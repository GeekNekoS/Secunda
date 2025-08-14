from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class OrganizationActivityAssoc(Base):
    __tablename__ = "organization_activity_assoc"

    organization_id = Column(Integer, ForeignKey("organization.id"), primary_key=True)
    activity_id = Column(Integer, ForeignKey("activity.id"), primary_key=True)
