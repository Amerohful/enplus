# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 419)
        MainWindow.setMinimumSize(QtCore.QSize(165, 301))
        MainWindow.setMaximumSize(QtCore.QSize(530, 419))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(150, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.new_login = QtWidgets.QLineEdit(self.centralwidget)
        self.new_login.setObjectName("new_login")
        self.gridLayout.addWidget(self.new_login, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.new_password = QtWidgets.QLineEdit(self.centralwidget)
        self.new_password.setObjectName("new_password")
        self.gridLayout.addWidget(self.new_password, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.new_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_name.setObjectName("new_name")
        self.gridLayout.addWidget(self.new_name, 6, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.reg = QtWidgets.QPushButton(self.centralwidget)
        self.reg.setObjectName("reg")
        self.gridLayout.addWidget(self.reg, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Регистрация"))
        self.label_2.setText(_translate("MainWindow", "Введите новый логин"))
        self.label_3.setText(_translate("MainWindow", "Придумайте пароль"))
        self.label_4.setText(_translate("MainWindow", "Введите свое имя"))
        self.reg.setText(_translate("MainWindow", "Готово"))
        self.label.setText(_translate("MainWindow", "Регистрация"))
