# coding=cp1251
import pythoncom
import win32com.client
import datetime


#Поиск в справочнике
# newdoc.ФИОПарикмахера = 'Справочники.Персонал.НайтиПоНаименованию("Иванов Василий Петрович")'


#Выборка через запрос

#q = '''
#ВЫБРАТЬ
#	Клиенты.Код КАК Код,
#	Клиенты.Наименование КАК Наименование
#ИЗ
#	Справочник.Клиенты КАК Клиенты
#
#ГДЕ
#	Клиенты.Наименование = "Пупкин Василий Петрович"
#'''
# query = v8.NewObject("Query", q)
# selection = query.Execute().Choose()
# selection.Next()


#newdoc.Дата = "15.10.2019 00:00:00"
#newdoc.НачалоСтрижки = "15.10.2019 01:00:00"
#newdoc.КонецСтрижки = "15.10.2019 02:11:00"


class OneC:
    CONSTR = 'File="F:\\Софт\\1С\\1C ДЗ\\1С Разработка";Usr="Админ";Pwd="1234"'
    v8 = ""

    def __init__(self):
        pythoncom.CoInitialize()
        self.v8 = win32com.client.Dispatch("V83.COMConnector").Connect(self.CONSTR)

    def create_doc(self, fio1, fio2, promo):
        Документ = getattr(self.v8.Documents, "ОказаниеУслуг")
        newdoc = Документ.CreateDocument()
        dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(str(dt))
        newdoc.Дата = str(dt)
        newdoc.ФИОПарикмахера = str(fio1)
        newdoc.ФИОКлиента = str(fio2)
        newdoc.Промокод = str(promo)
        newdoc.write()

    def get_docs(self):
        Документ = getattr(self.v8.Documents, "ОказаниеУслуг").select()
        while Документ.next():
            doc = Документ.GetObject()
            print(str(getattr(doc, "Дата")))





