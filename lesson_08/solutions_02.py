"""
Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes,
модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""


from solutions_01 import Car


class NewCars(Car):

    def get_hundred(self):
        while True:
            self.speed += 5
            if self.speed == 100:
                break
            print(f"Yor speed {self.speed}")
        print(f"Yor speed {self.speed}")

    def name(self):
        print(f"{self.brand}")


def main():
    car = NewCars(brand="Mercedes", model="E500", release=2000)
    car.get_hundred()
    car.name()


if __name__ == "__main__":
    main()
