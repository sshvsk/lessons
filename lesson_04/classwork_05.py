"""
Получить сумму кубов натуральных чисел от n до m
используя цикл for, числа n и m вводятся с клавиатуры.
"""

n, m = int(input("Введите число n: ")), int(input("Введите число m: "))
result = 0
for i in range(n, m):
    result += i ** 3
print(result)
