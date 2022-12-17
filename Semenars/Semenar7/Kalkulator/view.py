import funcs


def data_in():
    return int(input("Введите значение: "))

def operation(arr:list) -> int:
    n = input("Выберите операцию (+|-|*|/) -> ")
    if n == "+":
        return funcs.v_sum(arr)
    elif n == "-":
        return funcs.v_sub(arr)
    elif n == "*":
        return funcs.v_mult(arr)
    elif n == "/":
        return funcs.v_share(arr)
    return operation(arr)

def data_print(res):
    print(res)