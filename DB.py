import sqlite3


class DB:

	database = sqlite3.connect("DataBase/question.db")
	cursor = database.cursor()
	
	def __init__(self):
		self.cursor.execute("""
		CREATE TABLE IF NOT EXISTS answer
		(question TEXT PRIMARY KEY, answer TEXT)
		""")
		print("База подключена успешно")
		
	def get_table():
		
		