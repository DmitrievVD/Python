import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
from redactor_ui import Ui_win_redactor
from win_list import *
from add_contact_ui import *
from search_ui import *



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

def open_win_list():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

def open_win_add():
    global add_contact
    add_contact = QtWidgets.QDialog()
    ui = Ui_add_contact()
    ui.setupUi(add_contact)
    add_contact.show()

    def add_func():
        name = ui.line_edit_name.text()
        ui.line_edit_name.setText("")
        surname = ui.line_edit_surname.text()
        ui.line_edit_surname.setText("")
        number = ui.line_edit_number.text()
        ui.line_edit_number.setText("")

        write_contact(name, surname, number)

    ui.btn_ok.clicked.connect(add_func)
    # ui.buttonClicked.connecr(ui.active_add())

    # ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(active_add)

def open_win_search():
    global serch_window
    serch_window = QtWidgets.QDialog()
    ui = Ui_serch_window()
    ui.setupUi(serch_window)
    serch_window.show()

    def add_search_func():
        search_data = ui.line_edit_serch.text()
        ui.line_edit_serch.setText("")
        result = search(data_To_List(), search_data)
        # print("\n".join(result))
        ui.result_search.setText("\n".join(result))

    ui.btn_search.clicked.connect(add_search_func)


ui.btn_redactor.clicked.connect(open_win_redactor)
ui.btn_print_list.clicked.connect(open_win_list)
ui.btn_add.clicked.connect(open_win_add)
ui.btn_serch.clicked.connect(open_win_search)

sys.exit(app.exec_())