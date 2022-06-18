"""
04-Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
05-Создать второй объект класса MyTime, найти разницу с первым,
добавить к нему 7 часов и 45 минут, вывести на печать результат.
"""

from classwork_02_03 import NewTime

if __name__ == "__main__":
    a = NewTime.seconds_to_time(255)
    b = NewTime.seconds_to_time(200)
    print(a)
    print(a * 2)
    print(a - b)
    print(b + 27900)
