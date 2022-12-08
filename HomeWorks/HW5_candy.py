import random

def index_switch(i: int): # Меняет игрока
    if i == 1:
        i = 0
    elif i == 0:
        i = 1
    return i

def motion_hod(i: int, c: int): # Ход игрока
    try:
        num = int(input(f"Игрок {i + 1}: "))
    except:
        print("Что-то не так")
        return motion_hod(i, c)

    if num > c:
        print("Бери то что осталось", c)
        return motion_hod(i, c)
    if num < 1:
        print("Бери конфету правильно!!!")
        return motion_hod(i, c)
    elif num > 28:
        print("Больше 28 конфет брать нельзя!!!")
        return motion_hod(i, c)
    return num

def bot_hod(mon: int, c: int): # Бот

    num = 29 - mon
    if num > c:
        num = c
    print(f"Бот берет {num} конфет")
    return num


candy = 145 # Кол-во конфет сделал меньше так игра быстро идет
players = [0, 0]


motion = 0
play = True
index = random.randint(0, 1)

print(f"Ходит {index + 1}й игрок")
print("-----------")
while play:
    print("Всего конфет: ", candy)
    print(f"Конфет у 1 игрока: {players[0]}")
    print(f"Конфет у 2 игрока: {players[1]}")
    print("-----------")
    motion = motion_hod(index, candy)
    candy -= motion
    players[index] += motion
    print("Осталось конфет: ", candy)
    if candy <= 0:
        play = False
        continue
    index = index_switch(index)
    motion = bot_hod(motion, candy) # Тут можно поменять кто будет играть человек или бот
    candy -= motion
    players[index] += motion
    print("-----------")
    if candy <= 0:
        play = False
        continue
    index = index_switch(index)
else:
    print(f"Конфет у 1 игрока: {players[0]}")
    print(f"Конфет у 2 игрока: {players[1]}")
    print("-----------")
    print(f"Последним был игрок: {index + 1}")
    print(f"Он победил и забирает все конфеты!")