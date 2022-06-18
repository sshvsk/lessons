"""
Создать функцию при помощи регулярных выражений для проверки,
что строка является валидным телефонным номером в формате +375 (29) 299-29-29.
"""

import re


def is_mobile_phone(string):
    return re.match(r"^\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$", string)

if __name__ == "__main__":

    for item in ("+375 (29) 299-29-29", "+375 (29) 299-29-29"):  #test1
        assert is_mobile_phone(item) is not None

    for item in ("375 (29) 299-29-29", "375292992929"):          #test2
        assert is_mobile_phone(item) is None


if is_mobile_phone("+375 (29) 299-29-29"):
    print("yes")
else:
    print("no")

