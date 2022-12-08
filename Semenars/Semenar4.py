# 1. Считать строку из набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат заисать в конец исходного файла (х1 х2).

# file_path = r"text.txt"
#
# with open(file_path, "r") as f_data:
#     list_r = f_data.read()
#
# list_r = list_r.split(" ")
#
# max_ = str(max(list_r))
# min_ = str(min(list_r))
#
# result = "\n" + max_ + " " + min_
#
# with open(file_path, "a") as f_data:
#     f_data.write(result)

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами (получить кортеж):
#     1) с помощью математических формул нахождения корней квадратного уравнения

def discriminant (a: int, b:int, c:int):
    new_list = []
    dis = b**2 - (4 * a * c)
    if dis < 0:
        x_1 = -b / 2 * a
        new_list.append(x_1)
        return tuple(new_list)
    elif dis > 0:
        x_1 = round((-b + dis**0.5) / (2 * a), 2)
        x_2 = round((-b - dis ** 0.5) / (2 * a), 2)
        new_list.append(x_1)
        new_list.append(x_2)
        return tuple(new_list)
    else:
        return tuple(new_list)

tuple_ = discriminant(3, 7, 10)
print(tuple_)


# def foo(x):
#     return x**2
#
# arr = [2, 3, 5, 8, 15, 23, 38]
#
# new_arr = [(i ,foo(i)) for i in arr if i % 2 == 0]
# print(new_arr)