import pymsgbox
from PyQt5 import QtWidgets
import UI.change_window as cw


class Change(QtWidgets.QMainWindow, cw.Ui_MainWindow):
    id = ""
    data = ""
    bot = ""

    def __init__(self, id, question, answer, data, bot):
        super().__init__()
        self.setupUi(self)
        self.new_quest.setText(str(question))
        self.new_answer.setText(str(answer))
        self.Cancel.clicked.connect(self.Close)
        self.change.clicked.connect(self.OK)
        self.id = str(id)
        self.data = data
        self.bot = bot

    def Close(self):
        self.close()

    def OK(self):
        if self.data.update_ansquest(self.id, self.new_answer.text(), self.new_quest.text(), self.bot[0]) == 0:
            pymsgbox.alert("Успешно", "Готово")
            self.close()
