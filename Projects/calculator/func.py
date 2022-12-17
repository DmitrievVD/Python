def results(self):
    res = eval(self.label_result.text())
    self.label_result.setText(f"Результат: " + str(res))
    self.is_equal = True