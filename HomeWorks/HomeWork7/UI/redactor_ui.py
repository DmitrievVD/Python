# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_redactor.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win_redactor(object):
    def setupUi(self, win_redactor):
        win_redactor.setObjectName("win_redactor")
        win_redactor.resize(240, 100)
        win_redactor.setMaximumSize(QtCore.QSize(240, 100))
        self.centralwidget = QtWidgets.QWidget(win_redactor)
        self.centralwidget.setObjectName("centralwidget")
        self.serch_name = QtWidgets.QLineEdit(self.centralwidget)
        self.serch_name.setGeometry(QtCore.QRect(10, 20, 221, 22))
        self.serch_name.setObjectName("serch_name")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(60, 50, 93, 28))
        self.btn_ok.setObjectName("btn_ok")
        win_redactor.setCentralWidget(self.centralwidget)

        self.retranslateUi(win_redactor)
        QtCore.QMetaObject.connectSlotsByName(win_redactor)

    def retranslateUi(self, win_redactor):
        _translate = QtCore.QCoreApplication.translate
        win_redactor.setWindowTitle(_translate("win_redactor", "Редактор"))
        self.serch_name.setText(_translate("win_redactor", "Введите имя"))
        self.btn_ok.setText(_translate("win_redactor", "Ок"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     win_redactor = QtWidgets.QMainWindow()
#     ui = Ui_win_redactor()
#     ui.setupUi(win_redactor)
#     win_redactor.show()
#     sys.exit(app.exec_())