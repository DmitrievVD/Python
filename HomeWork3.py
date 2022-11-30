# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

# arr = [2, 3, 5, 9, 3]
#
# def summaodd(arrey_in: list):
#     result = 0
#     for i in arrey_in[1::2]:
#         result += i
#     return result
# print(f"Сумма элементов на нечетных позициях: {summaodd(arr)}")



# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# import math as m

# arr1 = [2, 3, 4, 5, 6]
# arr2 = [2, 3, 5, 6]
#
#
#
# def summa_doubl(arrey_in: list):
#     size = int(m.ceil(len(arrey_in) / 2))
#     new_arr = []
#     for i in range(0, size):
#         new_arr.append(arrey_in[i] * arrey_in[-1 - i])
#     return new_arr
#
#
# print(summa_doubl(arr1))




# 3.Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19



# arr = [1.1, 1.2, 3.1, 10.01]
#
# def sun_fraction(arrey_in: list):
#     new_arr = []
#     for el in arrey_in:
#         new_arr.append(round(el % 1, 5))
#     result = max(new_arr) - min(new_arr)
#     return result
#
# print(f"Разница между максимальной и минимальной дробной части: {sun_fraction(arr)}")



# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# n = float(input("Введите число: "))
#
# def double_num(num: float):
#     result = ""
#     while num != 1:
#         a = num // 2
#         result += str(int(num - (a*2)))
#         num //= 2
#     else:
#         result += str(int(num))
#     return result[::-1]
# print(double_num(n))



# 5. Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input("Введите число: "))

def fibonachi(k: int):
    new_arr = [0]
    k = abs(k)
    if k == 0:
        return new_arr
    elif k == 1:
        new_arr.append(1)
        return new_arr
    elif k == 2:
        new_arr.append(1)
        new_arr.append(1)
        return new_arr
    else:
        new_arr.append(1)
        new_arr.append(1)
        a = 1
        b = 1
        for i in range(2, k):
            a, b = b, a + b
            new_arr.append(b)
        return new_arr

def negafibonachi(arrey_in: list):
    new_arrey = (arrey_in[::-1])
    new_arrey.remove(0)
    for i in range(0, len(new_arrey)):
        new_arrey[i] = -abs(new_arrey[i])
    new_arrey.extend(arrey_in)
    return new_arrey

print(negafibonachi(fibonachi(n)))