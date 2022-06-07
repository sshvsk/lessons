"""
Дан список стран и городов каждой страны, где ключи это названия стран,
а значения - списки городов в этих странах. Написать функцию которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


def country_to_city(city):
    mapping = {
        "USA": ["Houston", "Chicago", "Atlanta"],
        "Japan": ["Tokyo", "Kyoto", "Sendai"],
        "Switzerland": ["Zurich", "Basel", "Geneva"]
    }
    for country, city_list in mapping.items():
        if city in city_list:
            return country

n_city = input("Enter city: ")
print(country_to_city(n_city))
