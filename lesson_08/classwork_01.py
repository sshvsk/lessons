"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""
from classwork_04 import Animal


class Dog(Animal):

    def talk(self):
        print(f"{self.name} is barking")


def main():
    dog = Dog(1, 2,"Boris")
    dog.jump()
    dog.run()
    dog.talk()


if __name__ == "__main__":
    main()