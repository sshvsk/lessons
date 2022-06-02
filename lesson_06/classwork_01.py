"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский,
 где слово - это входной параметр, вторая функция - с русского на английский.
"""

my_d = {
        "apple":  "яблоко",
        "grey": "серый",
        "fly": "летать",
}

def ang_to_rus(word):
    return my_d[word]


#def rus_to_ang(word):
#    for key, value in my_d.items():
#        if value == word:
#            return key

def rus_to_ang(word):
    new_d = {
        value: key
        for key, value in my_d.items()
        if value == word
    }
    return key




print(ang_to_rus("apple"))
print(rus_to_ang("летать"))
