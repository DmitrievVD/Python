# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'

# str_ = 'Я люблю Джавуабв абви Питон'
# arr = str_.split()
# result = [i for i in arr if 'абв' not in i]
# print(" ".join(result))




# 2. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 5 6 7 9

# my_list = None
# with open("Text5.txt", "r") as file_data:
#     my_list = file_data.read().split()
#
# my_list = list(map(int, my_list))
#
# for i in range(1, len(my_list)):
#     if my_list[i] != my_list[i - 1] + 1 :
#         print("Не хватает: ", my_list[i] - 1)








# 3. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

arr = [1, 5, 2, 3, 4, 6, 1, 7]
# my_list = list(filter(lambda x: x >= x, arr))
my_list = []
score = 0
my_list.append(arr[0])
for i in range(1, len(arr)):
    if my_list[score] <= arr[i]:
        my_list.append(arr[i])
        score += 1


print(my_list)