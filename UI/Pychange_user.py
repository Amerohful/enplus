import pymsgbox
from PyQt5 import QtWidgets
import UI.change_user as cw


class Change(QtWidgets.QMainWindow, cw.Ui_MainWindow):
    id = ""
    data = ""

    def __init__(self, id, login, password, name, data):
        super().__init__()
        self.setupUi(self)
        self.new_login.setText(str(login))
        self.new_password.setText(str(password))
        self.new_name.setText(str(name))
        self.Cancel.clicked.connect(self.Close)
        self.change.clicked.connect(self.OK)
        self.id = str(id)
        self.data = data

    def Close(self):
        self.close()

    def OK(self):
        if self.data.update_user(self.id, self.new_login.text(), self.new_password.text(), self.new_name.text()) == 0:
            pymsgbox.alert("Успешно", "Готово")
            self.close()
