from sqlite3 import Cursor, connect, IntegrityError
import random

def generate_random_letters(n):
    letters = []
    for _ in range(n):
        letter = chr(random.randint(ord('a'), ord('z')))
        letters.append(letter)
    return ''.join(letters)


class SQLite3Client:
    def __init__(self):
        self.connection, self.cursor = self.connect()
        self.create_table()

    @staticmethod
    def connect():
        connection = connect('tg.sql')
        return connection, connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(username TEXT, chat_id INT, uniq_code TEXT, is_invited BOOL, name TEXT, PRIMARY KEY(uniq_code))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS admins(username TEXT, chat_id INT, PRIMARY KEY(chat_id))""")

        self.cursor.execute("""SELECT * FROM admins""")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("""INSERT INTO admins(username) VALUES (?)""", ('CHT_VENDETTA', ))
            self.connection.commit()

        self.connection.commit()

    def add_user_into_table(self, chat_id: int, username: str, name: str):
        uniq_code = generate_random_letters(5)
        try:
            self.cursor.execute("""INSERT INTO users(chat_id, uniq_code, is_invited, username, name) VALUES(?, ?, ?, ?)""", (chat_id, uniq_code, 0, username, name))
        except IntegrityError:
            self.add_user_into_table(chat_id, username, name)

        self.connection.commit()

    def get_user(self, uniq_code: str) -> int:
        self.cursor.execute(f"""SELECT chat_id, name, username FROM users WHERE uniq_code = "{uniq_code}" """)
        return self.cursor.fetchall()[0]

    def get_uniq_code_of_user(self, chat_id: int) -> str:
        self.cursor.execute(f"""SELECT uniq_code FROM users WHERE chat_id = {chat_id}""")
        return self.cursor.fetchall()[0][0]

    def get_admins(self) -> list:
        self.cursor.execute("""SELECT username FROM admins""")
        return [username[0] for username in self.cursor.fetchall()]


client_sqlite3 = SQLite3Client()


