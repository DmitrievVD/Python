# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


# Задача №1 из ДЗ 2 Семенара до этого 14 строчек кода щас 8


# try:
#     numbers = str(float(input("Введите вещественное число: ")))
# except ValueError:
#     print("Это строка, за место ',' надо '.'")
#     numbers = str(float(input("Введите вещественное число: ")))
# arr = list(filter(lambda x: x != ".", numbers))
# result = sum(map(int, arr))
#
# print(result)



# Задача №2 из ДЗ 2 Семенара до этого 10 строчек кода щас 5

# import math
# n = int(input("Введите число: "))
# arr = [(i+1) for i in range(n) ]
# arr = list(map(lambda x: math.prod(range(1,x+1)), arr))
# print(arr)



# Задача №1 из ДЗ 3 Семенара до этого 7 строчек кода щас 3

# arr = [2, 3, 5, 9, 3]
# result = sum([i for i in arr[1::2] ])
# print(f"Сумма элементов на нечетных позициях: {result}")



# Задача №3 из ДЗ 4 Семенара до этого 7 строчек кода щас 3

arr = [1, 1, 2, 3, 4, 4, 4]
arr = [i for i in arr if not arr.count(i) >= 2]
print(arr)

