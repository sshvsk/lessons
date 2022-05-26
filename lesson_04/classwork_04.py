""" 
Написать программу, которая будет выводить
на экран случайные числа от 1 до 10 до тех пор,
пока не выпадет 7.


import random

while True:
    x = random.randint(1, 10)
    if x == 7:
        break
    print(x)
print(x)
"""

n, m = int(input()), int(input())
result = 0
for i in range(n, m):
    result += i ** 3
    print(result)
