# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_user.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 108)
        MainWindow.setMinimumSize(QtCore.QSize(663, 108))
        MainWindow.setMaximumSize(QtCore.QSize(663, 108))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Cancel.setObjectName("Cancel")
        self.gridLayout.addWidget(self.Cancel, 2, 1, 1, 1)
        self.new_login = QtWidgets.QLineEdit(self.centralwidget)
        self.new_login.setObjectName("new_login")
        self.gridLayout.addWidget(self.new_login, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setMaximumSize(QtCore.QSize(100, 16777215))
        self.change.setObjectName("change")
        self.gridLayout.addWidget(self.change, 2, 0, 1, 1)
        self.new_password = QtWidgets.QLineEdit(self.centralwidget)
        self.new_password.setObjectName("new_password")
        self.gridLayout.addWidget(self.new_password, 1, 1, 1, 1)
        self.new_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_name.setObjectName("new_name")
        self.gridLayout.addWidget(self.new_name, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменить"))
        self.Cancel.setText(_translate("MainWindow", "Отмена"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.change.setText(_translate("MainWindow", "ОК"))
        self.label_3.setText(_translate("MainWindow", "Имя"))
