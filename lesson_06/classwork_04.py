"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту,
в случае положительного ответа  - вытягивать случайную карту. Игра заканчивается если игрок отказывается брать карту,
либо сумма его карт больше 21-го.
"""

from classwork_03 import get_random_card

my_dict = {
    "6":6, "7":7, "8":8, "9":9, "10":10, "J":2, "D":3, "K":4, "A":1
}
def nom_to_value(n):
    return my_dict[n]

n, m = get_random_card()
value = nom_to_value(n)


summ_card = value
while True:
    choice = input("Достать след карту [Y/n]:")
    if choice == "n":
        break

    n, _ = get_random_card()
    value = nom_to_value(n)
    summ_card += value

    if summ_card > 21:
        print("Game Over", summ_card)
        break

    if summ_card == 21:
        print("You win")
        break

    if summ_card < 21:
        print("Твоя текуща сумма: ", summ_card)


