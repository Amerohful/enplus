import sys

import pymsgbox
from PyQt5 import QtWidgets

import DB
import UI.login as log
import UI.Pyregister as registration
import UI.Pymain as chat


class Login(QtWidgets.QMainWindow, log.Ui_MainWindow):
    con = ""
    reg = ""
    chat = ""
    data = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_error.setVisible(False)
        self.check_lp.clicked.connect(self.auth)
        self.Registr.clicked.connect(self.registration)
        self.data = DB.DB()

    def auth(self):
        res = self.data.check_user(self.login.text(), self.password.text())
        if res == "ошибка":
            self.login_error.setVisible(True)
        else:
            self.login_error.setVisible(False)
            botid = self.data.get_botid(res[0][0])
            if botid != 0:
                self.chat = chat.Chat(self.login.text(), self.password.text(), self.data, botid[len(botid)-1])
                self.chat.show()
                self.close()
            else:
                pymsgbox.alert("Бот не обнаружен", "Ошибка")

    def registration(self):
        self.reg = registration.Register(self.data)
        self.reg.show()


app = QtWidgets.QApplication(sys.argv)
window = Login()
window.show()
app.exec()
