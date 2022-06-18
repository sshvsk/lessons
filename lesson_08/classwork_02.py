"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя.
"""

from classwork_01 import Dog


class NewDog(Dog):

    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    new_dog = NewDog(height=10, weight=5, name="Felix")
    print("Old name: ", new_dog.name)
    new_dog.change_name("Boris")
    print("New name: ", new_dog.name)

