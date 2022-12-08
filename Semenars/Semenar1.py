# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# if (num2 == num1*num1) or (num1 == num2*num2):
#     print("yes")
# else:
#     print("no")



array = []

# for _ in range(5):
#     k = int(input())
#     array.append(k)
# print(array)
#
# def Max(input_arr):
#     x = 0
#     for i in input_arr:
#         if x < i:
#             x = i
#     print(x)
#
# Max(array)



# n = int(input())
# k = -n
#
# for _ in range((n*2)+1):
#     print(k, end = " ")
#     k += 1


# num = float(input())
#
# result = int(num*10)%10
# print(result)




num = int(input())

if (((num % 5 == 0) and (num % 10 == 0)) or (num % 15 == 0)) and (num % 30 != 0):
    print("Yes")