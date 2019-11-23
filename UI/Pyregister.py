import pymsgbox
from PyQt5 import QtWidgets

import UI.register as reg


class Register(QtWidgets.QMainWindow, reg.Ui_MainWindow):
    data = ""

    def __init__(self, data):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.reg.clicked.connect(self.register)

    def register(self):
        if self.new_login.text() == "" or self.new_password.text() == "" or self.new_name.text() == "":
            pymsgbox.alert("Заполните все поля", "Ошибка")
        else:
            if self.data.new_user(self.new_login.text(), self.new_password.text(), self.new_name.text()) == "готово":
                pymsgbox.alert("Вы успешно зарегестрированы", "Успешно")
                self.close()
