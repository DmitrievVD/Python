# 1. Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора псевдослучайных чисел.

# import time
#
# def Rand(a: int = 1):
#     if a == 2:
#         a = 10
#     elif a == 3:
#         a = 100
#     a = int((round(time.time(), 6) * 1000000 % (10 * a)))
#     print(a)
# Rand(3)


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['sdf13', 'fds66', '34']
# -> 3
# 'sdf13', '34'

# arr = ["sdg345", "sdgsd7", "pngng", "46dhdr"]
# a = input("Введите что ищете: ")
# def serch(a_1: str, arrey: list[str]):
#     for el in arr:
#         for i in el:
#             if i == a_1:
#                 print(el, end=", ")
#                 break
#
# serch(a, arr)


# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


arr1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
arr2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
arr3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
arr4 = ["123", "234", 123, "567"]
arr5 = []

def serch(arrey: list):
    a = input("Введите что вы ищете: ")
    result = -1
    position = 1
    for el in arrey[1:]:
        if el == a:
            result = position
        position += 1
    print("Позиция искомого значения:", result)

serch(arr4)

