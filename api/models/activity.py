from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("activity.id"))

    parent = relationship(
        "Activity",
        remote_side=lambda: [Activity.id],
        backref="sub_activities"
    )
    organizations = relationship(
        "Organization",
        secondary="organization_activity_assoc",
        back_populates="activities"
    )
