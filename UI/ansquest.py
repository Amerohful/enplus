# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ansquest.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 70))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.delete_ansquest = QtWidgets.QPushButton(self.widget)
        self.delete_ansquest.setObjectName("delete_ansquest")
        self.gridLayout.addWidget(self.delete_ansquest, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.widget)
        self.refresh.setObjectName("refresh")
        self.gridLayout.addWidget(self.refresh, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.DB_ansquest = QtWidgets.QTableWidget(self.centralwidget)
        self.DB_ansquest.setObjectName("DB_ansquest")
        self.DB_ansquest.setColumnCount(0)
        self.DB_ansquest.setRowCount(0)
        self.verticalLayout.addWidget(self.DB_ansquest)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вопрос/Ответ"))
        self.delete_ansquest.setText(_translate("MainWindow", "Добавить"))
        self.label_2.setText(_translate("MainWindow", "Ответ"))
        self.label.setText(_translate("MainWindow", "Вопрос"))
        self.refresh.setText(_translate("MainWindow", "Обновить"))
