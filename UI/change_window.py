# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_window.ui'
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
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setObjectName("change")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.change)
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Cancel.setObjectName("Cancel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Cancel)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.new_quest = QtWidgets.QLineEdit(self.centralwidget)
        self.new_quest.setObjectName("new_quest")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.new_quest)
        self.new_answer = QtWidgets.QLineEdit(self.centralwidget)
        self.new_answer.setObjectName("new_answer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.new_answer)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменить"))
        self.change.setText(_translate("MainWindow", "ОК"))
        self.Cancel.setText(_translate("MainWindow", "Отмена"))
        self.label_2.setText(_translate("MainWindow", "Ответ"))
        self.label.setText(_translate("MainWindow", "Вопрос"))
