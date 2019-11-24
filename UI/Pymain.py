from venv import logger

from PyQt5 import QtWidgets, QtGui, QtCore

import UI.main as chat
import UI.Pyansquest as aq
import UI.Pyuser as user
import modules.OneC.OneC as OneC


class Chat(QtWidgets.QMainWindow, chat.Ui_MainWindow):
    Name = ""
    data = ""
    DB_ansquest = ""
    DB_user = ""
    prov = False

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
            text = str(self.textEdit.toPlainText().replace("\n", " ").lower().strip())
            self.chat.appendPlainText(self.Name + ": " + text)
            if not self.prov:
                if text == "создать документ":
                    self.prov = not self.prov
                    self.chat.appendPlainText("BOT: " + "Введите ФИО парикмахера, ФИОклиента и промокод через запятую")
                elif text == "посмотреть документы":
                    OC = OneC.OneC()
                    OC.get_docs()
                else:
                    self.chat.appendPlainText("BOT: " + str(self.data.get_answer(text)))
                    self.textEdit.setPlainText(None)
            else:
                if text == "\hel" or text == "/hel":
                    self.chat.appendPlainText("BOT: " + "Доступные команды:")
                    self.chat.appendPlainText("     " + "'отмена': отменяет создание документа.")
                elif text == "отмена":
                    self.prov = not self.prov
                    self.chat.appendPlainText("BOT: " + "Создание документа отменено")
                else:
                    try:
                        temp = text.split(",")
                        OC = OneC.OneC()
                        OC.create_doc(temp[0], temp[1], temp[2])
                        self.chat.appendPlainText("BOT: " + "Документ создан")
                        self.prov = not self.prov
                    except Exception as e:
                        self.chat.appendPlainText("BOT: " + "Что-то пошло не так. Убедитесь в правильности введеных вами данных и попробуйте еще раз. Список доступных команд с документами: \help")

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
