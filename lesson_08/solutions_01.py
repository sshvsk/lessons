"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задний ход (изменение знака скорости).
"""

class Car:
    brand: str = None
    model: str = None
    year_release: int = None
    speed: int = 0

    def __init__(self, **kwargs):
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.year_release = kwargs.get("year_release")
        if kwargs.get("speed") is not None:
            self.speed = kwargs.get("speed")

    def speed_increase(self):
        self.speed += 5

    def speed_reduction(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def speed_display(self):
        print(f"Speed {self.brand} {self.speed} km\h")

    def reverse_gear(self):
        pass

def main():
    car = Car(brand="Lada", model="Vesta", year_release=2018)
    car.speed_increase()
    car.speed_increase()
    car.speed_display()
    car.speed_reduction()
    car.speed_display()
    car.stop()
    car.speed_display()


if __name__ == "__main__":
    main()


