"""
06-Добавить новый класс MyDateTime унаследованный от MyTime.
В конструктор добавить новые атрибуты: day, month, year.
“Исправить” все магические методы для этого класса.
07-Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""

from __future__ import annotations

from classwork_02_03 import NewTime


class MyDataTime(NewTime):
    def __init__(self, year: int, month: int, day: int, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.year = year
        self.month = month
        self.day = day
        self.housr = hours
        self.minutes = minutes
        self.seconds = seconds

    @staticmethod
    def seconds_to_time(seconds) -> MyDataTime:
        year = seconds // (60 * 60 * 24 * 30 * 12)
        month = seconds // (60 * 60 * 24 * 30)
        day = seconds // (60 * 60 * 24)
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60
        return MyDataTime(year=year, month=month, day=day, hours=hours, minutes=minutes, seconds=seconds)

    def __add__(self, other: NewTime) -> NewTime:
        seconds = self.to_seconds() + other
        return NewTime.seconds_to_time(seconds)

    def __sub__(self, other: NewTime) -> NewTime:
        seconds = self.to_seconds() - other
        return NewTime.seconds_to_time(seconds)

    def __mul__(self, other: NewTime) -> NewTime:
        seconds = self.to_seconds() * other
        return NewTime.seconds_to_time(seconds)

    def __str__(self):
        return f"{self.year}:{self.month}:{self.day}:{self.housr}:{self.minutes}:{self.seconds}"


def main():
    print(MyDataTime.seconds_to_time(1000000))


if __name__ == "__main__":
    main()