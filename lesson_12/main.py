"""
04-Создать программу, которая создает таблицы для моделей в базе данных и запустить.
05-Создать функцию, которая позволяет создавать пользователя, его профиль и адрес.
Добавить 5 различных записей пользователей.
06-Cоздать функции для добавления нового и обновления существующего адреса пользователя.
"""

from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Profile, Address
from utils import setup_db_engine, create_database_if_not_exists


def create_user(session: Session, email: str, password: str, phone: str, age: int, city: str, address: str) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)

    session.add_all((user, profile, address))
    session.commit()

    return user


def update_of_create_adress(session: Session, user: User, city: str, address: str) -> Address:
    if len(user.addresses):
        currentaddress = user.addresses[0]
        currentaddress.city = city
        currentaddress.address = address
    else:
        address = Address(user=user, city=city, address=address)

    session.add_all(address)
    session.commit()

    return address


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    # Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    currentsession = CurrentSession()

    # user = create_user(
    #     session=currentsession,
    #     email="Fabled@gamil.com",
    #     password="password",
    #     phone="phone",
    #     age=10,
    #     city="Minsk",
    #     address="address"
    # )

    user = currentsession.query(User).filter_by(email="test@test.com").first()
    address = Address(user=user, city="New city", address="New address")
    currentsession.add(address)
    currentsession.commit()

