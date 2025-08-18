from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    """Базовый класс для всех моделей"""
    def save(self, session: Session):
        session.add(self)
        session.commit()
        session.refresh(self)
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit()

    def update(self, session: Session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        session.refresh(self)
        return self

    @classmethod
    def bulk_update(cls, session: Session, filter_dict: dict, update_dict: dict):
        session.query(cls).filter_by(**filter_dict).update(
            update_dict,
            synchronize_session=False
        )
        session.commit()
