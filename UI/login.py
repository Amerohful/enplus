# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(397, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(500, 30))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 8, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 6, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(200, 40))
        self.widget.setMaximumSize(QtCore.QSize(500, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_lp = QtWidgets.QPushButton(self.widget)
        self.check_lp.setObjectName("check_lp")
        self.horizontalLayout.addWidget(self.check_lp)
        self.Registr = QtWidgets.QPushButton(self.widget)
        self.Registr.setObjectName("Registr")
        self.horizontalLayout.addWidget(self.Registr)
        self.gridLayout.addWidget(self.widget, 9, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(500, 30))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.login_error = QtWidgets.QLabel(self.centralwidget)
        self.login_error.setMaximumSize(QtCore.QSize(350, 30))
        self.login_error.setStyleSheet("color: red;")
        self.login_error.setObjectName("login_error")
        self.gridLayout.addWidget(self.login_error, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать в чат-бот ENoT. "))
        self.label_2.setText(_translate("MainWindow", "Введите логин"))
        self.check_lp.setText(_translate("MainWindow", "Вход"))
        self.Registr.setText(_translate("MainWindow", "Регистрация"))
        self.label_3.setText(_translate("MainWindow", "Введите пароль"))
        self.login_error.setText(_translate("MainWindow", "Введен неправильный логин и/или пароль"))
