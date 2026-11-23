import pymysql


class Database:
    def __init__(self):
        # подключение к MySQL
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="flask_auth",
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.connection.cursor()

    def get_user(self, username):
        # ищем пользователя по имени, если нет - вернётся None
        self.cursor.execute(
            "SELECT * FROM users WHERE user_name = %s", (username,)
        )
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
