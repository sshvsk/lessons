"""
Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n
(включая n) используя цикл while.
"""

number = int(input())
i = 1
result = 0
while number >= i:
    result += i ** 3
    i += 1
print(result)

