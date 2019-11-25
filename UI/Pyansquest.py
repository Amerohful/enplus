import keyboard

import pymsgbox
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
import UI.ansquest as aq
import UI.Pychange as change


class AQ(QtWidgets.QMainWindow, aq.Ui_MainWindow):
    temp = ""
    res = ""
    data = ""
    bot = ""

    def __init__(self, data, bot):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.bot = bot
        self.delete_ansquest.clicked.connect(self.addRow)
        self.DB_ansquest.cellClicked.connect(self.click)
        self.DB_ansquest.cellDoubleClicked.connect(self.doubleclick)
        self.refresh.clicked.connect(self.refreshTable)
        self.DB_ansquest.setColumnCount(2)
        self.refreshTable()

        keyboard.add_hotkey('delete', self.delete_row)

    def click(self, row):
        self.DB_ansquest.selectRow(row)

    def delete_row(self):
        if len(self.DB_ansquest.selectionModel().selectedRows()) > 0:
            if self.data.delete_ansquest(self.res[self.DB_ansquest.currentRow()][0], self.bot[0]) == 0:
                pymsgbox.alert("Удалено", "Готово")
            else:
                pymsgbox.alert("Произошла ошибка", "Ошибка")
        else:
            pymsgbox.alert("Ошибка", "Готово")

    def doubleclick(self, row):
        self.temp = change.Change(self.res[row][0], self.res[row][1], self.res[row][2], self.data, self.bot)
        self.temp.show()

    def refreshTable(self):
        # Заголовки
        self.DB_ansquest.setHorizontalHeaderLabels(["Вопрос", "Ответ"])

        # Выравниваем на центру
        self.DB_ansquest.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        self.DB_ansquest.horizontalHeaderItem(1).setTextAlignment(Qt.AlignCenter)

        # Получаем данные из БД
        self.res = self.data.get_ansquest(self.bot[0])
        i = 0
        self.DB_ansquest.setRowCount(len(self.res))
        while i < len(self.res):
            self.DB_ansquest.setItem(i, 0, QTableWidgetItem(str(self.res[i][1])))
            self.DB_ansquest.setItem(i, 1, QTableWidgetItem(str(self.res[i][2])))
            i = i + 1

        self.DB_ansquest.resizeColumnsToContents()

    def addRow(self):
        if self.lineEdit == "" or self.lineEdit_2 == "":
            pymsgbox.alert("Заполните поля", "Ошибка")
        else:
            if self.data.add_ansquest(self.lineEdit_2.text().lower().strip(), self.lineEdit.text().lower().strip(), self.bot[0]) == 0:
                pymsgbox.alert("Данные добавлены", "Успешно")
                self.refreshTable()
