import sys

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
        if self.data.check_user(self.login.text(), self.password.text()) != "готово":
            self.login_error.setVisible(True)
        else:
            self.login_error.setVisible(False)
            self.chat = chat.Chat(self.login.text(), self.password.text(), self.data)
            self.chat.show()
            self.close()

    def registration(self):
        self.reg = registration.Register(self.data)
        self.reg.show()


app = QtWidgets.QApplication(sys.argv)
window = Login()
window.show()
app.exec()
