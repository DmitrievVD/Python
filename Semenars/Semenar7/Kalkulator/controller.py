import view
import data_buse

def start():
    value1 = view.data_in()
    value2 = view.data_in()

    data_buse.data_save(value1, value2)
    value_arr = data_buse.data_open()

    result = view.operation(value_arr)

    data_buse.data_save_add(result)

    itog = data_buse.data_open_res()

    view.data_print(itog)

