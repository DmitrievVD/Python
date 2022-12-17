import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
from redactor_ui import Ui_win_redactor




app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def open_win_redactor():
    global win_redactor
    win_redactor = QtWidgets.QMainWindow()
    ui = Ui_win_redactor()
    ui.setupUi(win_redactor)
    win_redactor.show()

ui.btn_redactor.clicked.connect(open_win_redactor)

sys.exit(app.exec_())