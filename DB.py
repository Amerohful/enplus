from venv import logger

import pymysql


class DB:
    database = pymysql.connect('a0365622.xsph.ru', 'a0365622_enot-plus', 'qwert', 'a0365622_enot-plus')

    def __init__(self):
        print("БД подключена")

    def __del__(self):
        self.database.close()

    # ---------------------USER----------------------------------

    def check_user(self, login, password):
        cursor = self.database.cursor()
        sql = "SELECT ownerID FROM owner WHERE email = '" + login + "' AND password = '" + password + "'"
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        if len(res) == 0:
            return "Ошибка"
        else:
            return res

    def new_user(self, login, password, user):
        try:
            cursor = self.database.cursor()
            sql = "INSERT INTO owner(email, password, fullName) VALUES('" + login + "', '" + password + "', '" + user + "')"
            cursor.execute(sql)
            self.database.commit()
            cursor.close()
        except Exception as e:
            logger.exception(str(e))
        return "готово"

    def get_user(self, login, password):
        res = ""
        cursor = self.database.cursor()
        try:
            sql = "SELECT fullName FROM owner WHERE email = '" + login + "' AND password = '" + password + "'"
            cursor.execute(sql)
            res = cursor.fetchone()
        except Exception as e:
            logger.exception(str(e))
        cursor.close()
        return res[0]

    def get_users(self):
        cursor = self.database.cursor()
        res = ""
        try:
            sql = "SELECT ownerID, email, password, fullName  FROM owner"
            cursor.execute(sql)
            res = cursor.fetchall()
        except Exception as e:
            logger.exception(str(e))
        cursor.close()
        return res

    def delete_user(self, id):
        cursor = self.database.cursor()
        try:
            sql = "DELETE FROM owner WHERE ownerID= '" + str(id) + "'"
            cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            logger.exception(str(e))
            return "ошибка"
        cursor.close()
        return 0

    def add_user(self, login, password, name):
        cursor = self.database.cursor()
        try:
            sql = "INSERT INTO owner(email, password, fullName) VALUES('" + password + "', '" + login + "', '" + name + "')"
            cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            logger.exception(str(e))
            return "Ошибка"
        cursor.close()
        return 0

    def update_user(self, id, login, password, user):
        cursor = self.database.cursor()
        try:
            sql = "UPDATE owner SET email = '" + login + "', password = '" + password + "', fullName = '" + user + "' WHERE ownerID = " + id
            cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            logger.exception(str(e))
            cursor.close()
            return "Ошибка"
        cursor.close()
        return 0

    # --------------------------ANSQUEST------------------------------------------

    def get_answer(self, question, botID):
        cursor = self.database.cursor()
        res = ""
        try:
            sql = "SELECT answer FROM ansquest WHERE question = '" + question + "' AND botID='" + str(botID) + "'"
            cursor.execute(sql)
            res = cursor.fetchone()
        except Exception as e:
            logger.exception(str(e))
        cursor.close()
        if str(res) != "None":
            return res[0]
        else:
            return "я не знаю ответа на этот вопрос"

    def get_ansquest(self, bot):
        cursor = self.database.cursor()
        res = ""
        try:
            sql = "SELECT ansquestID, question, answer  FROM ansquest WHERE botID='" + str(bot) + "'"
            cursor.execute(sql)
            res = cursor.fetchall()
        except Exception as e:
            logger.exception(str(e))
        cursor.close()
        return res

    def add_ansquest(self, answer, question, bot):
        cursor = self.database.cursor()
        try:
            sql = "INSERT INTO ansquest(botID, question, answer) VALUES('" + str(
                bot) + "', '" + question + "', '" + answer + "')"
            cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            logger.exception(str(e))
            return "Ошибка"
        cursor.close()
        return 0

    def update_ansquest(self, id, answer, question, bot):
        cursor = self.database.cursor()
        try:
            sql = "UPDATE ansquest SET botID='" + str(
                bot) + "', question = '" + question + "', answer = '" + answer + "' WHERE ansquestID = " + id
            cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            logger.exception(str(e))
            cursor.close()
            return "Ошибка"
        cursor.close()
        return 0

    def delete_ansquest(self, id, bot):
        cursor = self.database.cursor()
        try:
            sql = "DELETE FROM ansquest WHERE botID ='" + str(bot) + "' AND ansquestID = '" + str(id) + "'"
            cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            logger.exception(str(e))
            return "Ошибка"
        cursor.close()
        return 0

    # ----------------------------bot-------------------------------------

    def get_botid(self, owner):
        cursor = self.database.cursor()
        res = ""
        try:
            sql = "SELECT *  FROM bot WHERE ownerID='" + str(owner) + "'"
            cursor.execute(sql)
            res = cursor.fetchall()
            cursor.close()
            if len(res) == 0:
                return 0
            else:
                return res
        except Exception as e:
            logger.exception(str(e))
