
# n = int(input())
# i = 0
# result = 1
# while i < n:
#     if i % 2 == 0:
#         print(result, end=" ")
#     else:
#         print(-result, end=" ")
#     result *= 3
#     i += 1




# n = int(input())
# i = 0
# result = 1
# while i < n:
#     i += 1
#     result = 3 * i +1
#     print(result, end=" ")






a = input()
b = input()
len_b = len(b)
score = 0
i = 0
while i < len(a):
    if b.lower() == a[i: len_b + i].lower(): score += 1
    i += 1

print(score)



