from api.models import Activity, Office, Organization, Phone, OrganizationActivityAssoc
from api.models.base import engine, Base
from sqlalchemy.orm import Session


def gen_test_data(db: Session):
    # --- Создаем офисы ---
    office1 = Office(
        address="г. Москва, ул. Пушкина, д. 10",
        latitude=55.751244,
        longitude=37.618423)
    office2 = Office(
        address="г. Санкт-Петербург, Невский пр., д. 20",
        latitude=59.934280,
        longitude=30.335099)

    # --- Создаем виды деятельности ---
    act_food = Activity(name="Еда")
    act_cafe = Activity(name="Кафе", parent=act_food)
    act_restaurant = Activity(name="Ресторан", parent=act_food)
    act_sport = Activity(name="Спорт")
    act_gym = Activity(name="Тренажерный зал", parent=act_sport)
    act_yoga = Activity(name="Йога", parent=act_sport)

    # --- Создаем организации ---
    org1 = Organization(name="Кафе Вкусняшки", office=office1)
    org2 = Organization(name="Фитнес-центр СпортЛайф", office=office2)

    # --- Привязываем телефоны ---
    phone1 = Phone(organization=org1, phone="+7 (999) 111-22-33")
    phone2 = Phone(organization=org2, phone="+7 (888) 444-55-66")

    # Добавляем всё сразу
    db.add_all([
        office1, office2,
        act_food, act_cafe, act_restaurant, act_sport, act_gym, act_yoga,
        org1, org2,
        phone1, phone2
    ])
    db.flush()  # чтобы ids появились в памяти, без коммита

    # --- Привязываем виды деятельности через связь ---
    assoc1 = OrganizationActivityAssoc(organization_id=org1.id, activity_id=act_cafe.id)
    assoc2 = OrganizationActivityAssoc(organization_id=org2.id, activity_id=act_gym.id)
    db.add_all([assoc1, assoc2])

    db.commit()  # один общий коммит
    print("✅ Seed data успешно создана!")


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    db = next(Base.get_db())
    gen_test_data(db)
