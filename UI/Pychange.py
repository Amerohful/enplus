import pymsgbox
from PyQt5 import QtWidgets
import UI.change_window as cw


class Change(QtWidgets.QMainWindow, cw.Ui_MainWindow):
    id = ""
    data = ""

    def __init__(self, id, question, answer, data):
        super().__init__()
        self.setupUi(self)
        self.new_quest.setText(str(question))
        self.new_answer.setText(str(answer))
        self.Cancel.clicked.connect(self.Close)
        self.change.clicked.connect(self.OK)
        self.id = str(id)
        self.data = data

    def Close(self):
        self.close()

    def OK(self):
        if self.data.update_ansquest(self.id, self.new_answer.text(), self.new_quest.text()) == 0:
            pymsgbox.alert("Успешно", "Готово")
            self.close()
