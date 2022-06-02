"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся
и самое длинное, в идеале не использовать библиотечные функции.
"""


text = "Beautiful is better than ugly. Explicit, is better than implicit."
def long_item_in_text(text):
    words = text.replace(".", "").replace(",", "").replace("!", "").replace(":", "")
    words = words.split(" ")
    long_value = words[0]
    for i in words:
        if len(i) > len(long_value):  # сравниваем первый элемент по количетву символов
            long_value = i
    return long_value


print(long_item_in_text(text))


def repeated_element_in_text(text):
    words = text.replace(".", "").replace(",", "").replace("!", "").replace(":", "")
    words = words.split(" ")
    repeat_value = 0
    for item in words:
        entry_n = words.count(item)  # переменной entry_n присваивается количество
        if entry_n > repeat_value:   # вхождений item в words
            repeat_value = entry_n
            entry = item
    return entry


print(repeated_element_in_text(text))
