import model
import view

def buttom_click():
    value_a = view.get_value()
    value_b = view.get_value()
    result = model.init(value_a, value_b)
    view.view_data(result)