"""
Дан произвольный список, содержащий только числа.
Выведите результат сложения всех чисел больше 10.
"""

my_list = [20, 30, 17, 1, 2]
result = 0
for item in my_list:
    if item > 10:
        result += item
print(result)
