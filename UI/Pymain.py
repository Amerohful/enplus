from venv import logger

from PyQt5 import QtWidgets, QtGui, QtCore

import UI.main as chat
import UI.Pyansquest as aq
import UI.Pyuser as user


class Chat(QtWidgets.QMainWindow, chat.Ui_MainWindow):
    Name = ""
    data = ""
    DB_ansquest = ""
    DB_user = ""

    def __init__(self, login, password, data):
        try:
            super().__init__()
            self.setupUi(self)
            self.data = data
            self.pushButton.setIcon(QtGui.QIcon("UI/icon/send.png"))
            self.pushButton.setIconSize(QtCore.QSize(48, 48))
            self.pushButton.clicked.connect(self.send)
            self.Name = self.data.get_user(login, password)
            self.chat.setPlainText("BOT: добро пожаловать " + self.Name)
            self.action_exit.triggered.connect(self.close)
            self.action_users.triggered.connect(self.users)
            self.action_ansquest.triggered.connect(self.ansquest)

        except Exception as e:
            logger.exception(str(e))

    def send(self):
        try:
            self.chat.appendPlainText(self.Name + ": " + self.textEdit.toPlainText().replace("\n", " ").lower().strip())
            self.chat.appendPlainText("BOT: " + str(
                self.data.get_answer(str(self.textEdit.toPlainText().replace("\n", " ").lower().strip()))
            ))
            self.textEdit.setPlainText(None)
        except Exception as e:
            logger.exception(str(e))
        return 0

    def users(self):
        try:
            self.DB_ansquest = user.User(self.data)
            self.DB_ansquest.show()
        except Exception as e:
            logger.exception(str(e))

    def close(self):
        self.close()

    def ansquest(self):
        try:
            self.DB_ansquest = aq.AQ(self.data)
            self.DB_ansquest.show()
        except Exception as e:
            logger.exception(str(e))
