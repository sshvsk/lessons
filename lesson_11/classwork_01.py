"""
Создать функцию, которая позволяет добавлять данные в таблицу user.
Добавить 5 различных записей
"""

import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()

if __name__ == "__main__":
    create_user("Viktor", "Lugin", "lug13@gmail.com", "qwerty", 23)
    create_user("Ivan", "Balutin", "balutini@gmail.com", "qwerty123", 39)
    create_user("Igor", "Chubukin", "chubakka@bk.ru", "454dsv2er", 23)
    create_user("Vova", "Gombalevsky", "gombal22@mail.ru", "454d@2sv2er", 24)
    create_user("Alina", "Ananenko", "anan@mail.ru", "1323kler", 32)