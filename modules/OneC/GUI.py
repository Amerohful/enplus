# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.obzor = QtWidgets.QPushButton(self.centralwidget)
        self.obzor.setGeometry(QtCore.QRect(550, 40, 75, 23))
        self.obzor.setObjectName("obzor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 491, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 101, 16))
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(40, 90, 121, 20))
        self.login.setObjectName("login")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 47, 13))
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(40, 140, 121, 20))
        self.password.setObjectName("password")
        self.connect = QtWidgets.QPushButton(self.centralwidget)
        self.connect.setGeometry(QtCore.QRect(40, 170, 91, 23))
        self.connect.setObjectName("connect")
        self.document = QtWidgets.QLineEdit(self.centralwidget)
        self.document.setGeometry(QtCore.QRect(500, 130, 113, 20))
        self.document.setObjectName("document")
        self.Data = QtWidgets.QLineEdit(self.centralwidget)
        self.Data.setGeometry(QtCore.QRect(500, 190, 113, 20))
        self.Data.setObjectName("Data")
        self.StartStr = QtWidgets.QLineEdit(self.centralwidget)
        self.StartStr.setGeometry(QtCore.QRect(500, 220, 113, 20))
        self.StartStr.setObjectName("StartStr")
        self.EndStr = QtWidgets.QLineEdit(self.centralwidget)
        self.EndStr.setGeometry(QtCore.QRect(500, 250, 113, 20))
        self.EndStr.setObjectName("EndStr")
        self.writeDoc = QtWidgets.QPushButton(self.centralwidget)
        self.writeDoc.setGeometry(QtCore.QRect(510, 300, 75, 23))
        self.writeDoc.setObjectName("writeDoc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.obzor.setText(_translate("MainWindow", "Обзор"))
        self.label.setText(_translate("MainWindow", "Укажите путь к БД"))
        self.label_2.setText(_translate("MainWindow", "Имя пользователя"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.connect.setText(_translate("MainWindow", "Подключится"))
        self.writeDoc.setText(_translate("MainWindow", "Записать"))
