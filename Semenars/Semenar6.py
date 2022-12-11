# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

num = input("Введите выражение: ")

lst = []
buf = ""

for i in range(len(num)):
    if num[i].isdigit():
        buf += num[i]
    else:
        lst.append(int(buf))
        lst.append(num[i])
        buf =""
else:
    lst.append(int(buf))


while '*' in lst or '/' in lst:
    unm = None
    if '*' in lst:
        umn = lst.index('*')
    deli = None
    if '/' in lst:
        deli = lst.index('/')
    if (umn < deli) and (umn != -1):
        res = lst[umn - 1] * lst[umn + 1]
        lst[umn - 1: umn + 2] = res
    elif (deli < umn) and (deli != -1):
        res = lst[deli - 1] / lst[deli + 1]
        lst[deli - 1: deli + 2] = res

print(lst)