"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить,
причем сам себе человек не может подарить, дубликаты тоже не допустимы.
"""

import random

"""
my_list = ["Masha", "Igor", "Ivan", "Anna", "Elena", "Vlad"]
import random

def random_list(my_list):
    random.shuffle(my_list)
    return my_list

def secret_santa(name, my_list):
    size = len(my_list)

print(random_list(my_list))
"""
def secret_santa(list):
    size = len(list)

    return size



my_list = ["Masha", "Igor", "Ivan", "Anna", "Elena", "Vlad"]
print(secret_santa(my_list))