# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(873, 641)
        MainWindow.setMinimumSize(QtCore.QSize(521, 384))
        MainWindow.setMaximumSize(QtCore.QSize(873, 641))
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(884, 628))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.chat.setMinimumSize(QtCore.QSize(0, 30))
        self.chat.setReadOnly(True)
        self.chat.setObjectName("chat")
        self.verticalLayout.addWidget(self.chat)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon/send.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 873, 21))
        self.menuBar.setStyleSheet("background-color: rgb(245,245,245);")
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setStyleSheet("QMenu::item:selected {\n"
" background: rgb(235,235,235);\n"
" color:black;\n"
"}\n"
" QMenu::item:pressed {\n"
"  background: rgb(220,220,220);\n"
" }")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action_ansquest = QtWidgets.QAction(MainWindow)
        self.action_ansquest.setCheckable(False)
        self.action_ansquest.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.action_ansquest.setObjectName("action_ansquest")
        self.action_users = QtWidgets.QAction(MainWindow)
        self.action_users.setObjectName("action_users")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu.addAction(self.action_ansquest)
        self.menu.addAction(self.action_users)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Меню"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action_ansquest.setText(_translate("MainWindow", "Вопрос/Ответ"))
        self.action_users.setText(_translate("MainWindow", "Пользователи"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
