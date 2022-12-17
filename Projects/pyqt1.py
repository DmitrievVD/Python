from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()


        self.setWindowTitle("Первая программа")
        self.setGeometry(300, 250, 700, 400)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Какой то текст")
        self.main_text.move(120, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(100, 150)
        self.btn.setText("Не Жми")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_lable)

    def add_lable(self):
        self.new_text.setText("Опа, не ждали")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()