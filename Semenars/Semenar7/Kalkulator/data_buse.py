file_path = r"data.txt"
def data_save(x: int, y: int):
    with open(file_path, "w") as f_data:
        f_data.write(f"{x} {y}")

def data_open() -> list:
    with open(file_path, "r") as f_data:
        return list(map(int, f_data.read().split()))

def data_save_add(res:int):
    with open(file_path, "a") as f_data:
        f_data.write(f"\n{res}")

def data_open_res() -> int:
    with open(file_path, "r") as f_data:
        return (f_data.readlines()[1])