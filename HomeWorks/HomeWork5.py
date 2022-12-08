# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'



# # С использованием list comprehension
# str_ = 'Я люблю Джавуабв абви Питон'
# arr = str_.split()
# result = [i for i in arr if 'абв' not in i]
# print(" ".join(result))


# # С использованием функции filter
# str_ = 'Я люблю Джавуабв абви Питон'
# arr = str_.split()
# result = list(filter(lambda x: "абв" not in x, arr))
# print(" ".join(result))



# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.



my_str = "wwwqttttbbfffff"


new_str =""
i = 0

while i < len(my_str): # Сжимает текст
    count = 1
    while i + 1 < len(my_str) and my_str[i] == my_str[i + 1]:
        count += 1
        i += 1
    new_str += str(count) + my_str[i]
    i += 1

print(new_str)

result = ""

for i in range(0, len(new_str), 2): # Распаковывает
    result += int(new_str[i]) * new_str[i+1]

print(result)



