"""
Известно, что на шахматной доске 8×8 можно расставить ферзей так,
чтобы они не били друг друга (ферзь может ходить по горизонтали, вертикали и диагонали).
Вам дана расстановка двух ферзей на доске, определите могут ли ферзи бить друг друга.
Программа получает на вход две пары чисел, первое число в паре - координата по горизонтали,
второе - координата по вертикали. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
Используя условие первой задачи из урока, проверить то же самое только для коней.
"""

def horse(x1, y1, x2, y2):
    return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)


def main():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    if horse(x1, y1, x2, y2):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()