# coding=cp1251
import pythoncom
import win32com.client
import datetime


#����� � �����������
# newdoc.�������������� = '�����������.��������.�������������������("������ ������� ��������")'


#������� ����� ������

#q = '''
#�������
#	�������.��� ��� ���,
#	�������.������������ ��� ������������
#��
#	����������.������� ��� �������
#
#���
#	�������.������������ = "������ ������� ��������"
#'''
# query = v8.NewObject("Query", q)
# selection = query.Execute().Choose()
# selection.Next()


#newdoc.���� = "15.10.2019 00:00:00"
#newdoc.������������� = "15.10.2019 01:00:00"
#newdoc.������������ = "15.10.2019 02:11:00"


class OneC:
    CONSTR = 'File="F:\\����\\1�\\1C ��\\1� ����������";Usr="�����";Pwd="1234"'
    v8 = ""

    def __init__(self):
        pythoncom.CoInitialize()
        self.v8 = win32com.client.Dispatch("V83.COMConnector").Connect(self.CONSTR)

    def create_doc(self, fio1, fio2, promo):
        �������� = getattr(self.v8.Documents, "�������������")
        newdoc = ��������.CreateDocument()
        dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(str(dt))
        newdoc.���� = str(dt)
        newdoc.�������������� = str(fio1)
        newdoc.���������� = str(fio2)
        newdoc.�������� = str(promo)
        newdoc.write()

    def get_docs(self):
        �������� = getattr(self.v8.Documents, "�������������").select()
        while ��������.next():
            doc = ��������.GetObject()
            print(str(getattr(doc, "����")))





