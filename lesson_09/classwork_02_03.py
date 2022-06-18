"""
02-Переопределить магические методы сложения, вычитания, умножения на число.
03-Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
"""
from __future__ import annotations

from classwork_01 import MyTime


class NewTime(MyTime):

    @staticmethod
    def seconds_to_time(seconds) -> NewTime:
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60
        return NewTime(hours=hours, minutes=minutes, seconds=seconds)

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
        return f"{self.housr}:{self.minutes}:{self.seconds}"


def main():
    print(NewTime.seconds_to_time(541111))


if __name__ == "__main__":
    main()