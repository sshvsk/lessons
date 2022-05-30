"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ,
 из этих чисел составляется первый список. Далее таким же образом вводятся второй и третий списки.
 Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем.
"""
my_list1, my_list2, my_list3 = [], [], []

while True:
    i = input("Введите число для первого списка: ")
    if i.isdigit():
        i = int(i)
        my_list1.append(i)
    else:
        break
print("Первый список:", my_list1)


while True:
    i = input("Введите число для второго списка: ")
    if i.isdigit():
        i = int(i)
        my_list2.append(i)
    else:
        break
print("Первый список:", my_list2)


while True:
    i = input("Введите число для третьего списка: ")
    if i.isdigit():
        i = int(i)
        my_list3.append(i)
    else:
        break
print("Третий список", my_list3)


result = list((set(my_list1) & set(my_list2)) - set(my_list3))
print("Четвертый список", result)
