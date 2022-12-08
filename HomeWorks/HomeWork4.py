# 1.Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141


# import math
#
# b = input("Введите число: ")
# b_size = b.split(".") if b[1] == "." else b.split(",")
#
# b_size = len(b_size[1])
#
# result = round(math.pi, b_size)
# print(result)




# 2.Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# a = int(input("Введите натуральное число: "))
# result = []
# num = a
# n = 2
#
# while n * n <= num:
# 	while num % n == 0:
# 		num //= n
# 		result.append(n)
# 	n += 1
# if num > 1:
# 	result.append(num)
# print(a, "=", " x ".join(str(el) for el in result))





# 3.Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


# arr = [1, 1, 5, 2, 3, 4, 4, 4, 3]
# arr.sort()
#
# for el in arr:
# 	if arr.count(el) >= 2:
# 		for i in range(0, arr.count(el)):
# 			arr.remove(el)
# print(arr)






# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

# import random
# num = int(input("Введите число: "))
#
#
# stepen = ""
#
# while num > 1:
# 	stepen = stepen + "x**" + str(num) + " "
# 	num -= 1
# else:
# 	stepen = stepen + "x" + " "
# arr = stepen.split(" ")
# arr[-1] = "= 0"
# for i in range(0, len(arr) - 1):
# 	a = random.randint(0, 100)
# 	if a == 0:
# 		del arr[i]
# 	else:
# 		arr[i] = str(a) + arr[i]
# rand = random.randint(0, 100)
# result = " + ".join(arr[:-1:]) + " + " + str(rand) + " " + arr[-1]
# print(arr)
# print(result)
#
# file_path = r"hw4.txt"
#
# with open(file_path, "a") as f_data:
# 	f_data.writelines(result + "\n")




# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).



file_path = r"hw4.txt"
arr = []

with open(file_path, "r") as f_data:
	for el in f_data:
		arr.append(el.split(" + " or " = "))
print(arr)
