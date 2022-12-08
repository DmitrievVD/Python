
def print_box(in_box: list):
    for i in range(3):
        print(in_box[i])

def motion_hod(in_box: list, x_or_o: str):
    pl = input(f"Игрок {x_or_o} выбирает поле: ")
    check = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if pl not in check:
        print("Ввели не правельное значение!")
        return motion_hod(in_box, x_or_o)
    for i in range(3):
        if pl in in_box[i]:
            for j in range(3):
                if pl == in_box[i][j]:
                    in_box[i][j] = x_or_o

def index_switch(i: str):
    if i == "x":
        i = "o"
    else:
        i = "x"
    return i

def chek_win(in_box: list, i: str) -> bool: # Эта функция не работает, не правильно условие написал а как исправить не знаю
    if (in_box[0][0] and in_box[0][1] and in_box[0][2]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    elif (in_box[1][0] and in_box[1][1] and in_box[1][2]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    elif (in_box[2][0] and in_box[2][1] and in_box[2][2]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    elif (in_box[0][0] and in_box[1][0] and in_box[2][0]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    elif (in_box[0][1] and in_box[1][1] and in_box[2][1]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    elif (in_box[0][2] and in_box[1][2] and in_box[2][2]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    elif (in_box[0][0] and in_box[1][1] and in_box[2][2]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    elif (in_box[0][2] and in_box[1][1] and in_box[2][0]) == i:
        print(f"Игрок {i} Выиграл")
        return False
    return True


def new_chek_win(in_box: list, inx: str) -> bool:
    if in_box[0][0] == inx:
        if in_box[0][1] == inx:
            if in_box[0][2] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
        if in_box[1][0] == inx:
            if in_box[2][0] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
    if in_box[1][0] == inx:
        if in_box[1][1] == inx:
            if in_box[1][2] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
    if in_box[2][0] == inx:
        if in_box[2][1] == inx:
            if in_box[2][2] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
    if in_box[0][1] == inx:
        if in_box[1][1] == inx:
            if in_box[2][1] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
    if in_box[0][2] == inx:
        if in_box[1][2] == inx:
            if in_box[2][2] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
    if in_box[0][0] == inx:
        if in_box[1][1] == inx:
            if in_box[2][2] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
    if in_box[0][2] == inx:
        if in_box[1][1] == inx:
            if in_box[2][0] == inx:
                print(f"Игрок {inx} Выиграл")
                return False
    return True


box = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

index = "x"
play = True

while play:
    print_box(box)
    motion_hod(box, index)
    play = new_chek_win(box, index)
    if play == False:
        continue
    index = index_switch(index)

    print_box(box)

    motion_hod(box, index)
    play = new_chek_win(box, index)
    if play == False:
        continue
    index = index_switch(index)
    print_box(box)
    print("--------------")
else:
    print_box(box)
    print("--------------")
    print(f"Игрок {index} Выиграл")