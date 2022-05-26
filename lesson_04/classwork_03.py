"""
Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n
(включая n) используя цикл while.
"""

number = int(input())
result = 0
index = 1

while index <= number:
    index += 1
    result += index ** 3
print(result)

