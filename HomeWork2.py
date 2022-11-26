# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11


# try:
#     numbers = str(float(input("Введите вещественное число: ")))
# except ValueError:
#     print("Это строка, за место ',' надо '.'")
#     numbers = str(float(input("Введите вещественное число: ")))
# arr = []
# for i in numbers:
#     if i == ".":
#         continue
#     arr.append(i)
#
# result = 0
# for i in arr:
#     result += int(i)
#
# print(result)



# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# n = int(input())
# i = 0
# result = 1
# arr = list()
# while i < n:
#     i += 1
#     result *= i
#     arr.append(result)
# else:
#     print(arr)



# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06


# n = int(input())
# nums = {j: round(((1 + 1/j)**j), 3) for j in range(1, n + 1)}
# print(nums)
# print("Сумма: ",sum(nums.values()))



# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0


# n = int(input("Введите число: "))
# arr = [i for i in range(-n,n+1)]
# print(arr)
# index = input("--> ")
# index = index.split(" ")
#
# for i in range(0, len(index)):
#     index[i] = int(index[i])
# result = 1
# for i in index:
#     result *= arr[i]
# print(result)





# 5. Реализуйте алгоритм перемешивания списка.
# import random
#
#
# arr = [1, 2, 3, 4, 5]
# random.shuffle(arr)
# print(arr)
