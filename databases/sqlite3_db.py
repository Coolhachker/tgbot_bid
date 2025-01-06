from sqlite3 import connect, IntegrityError
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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(username TEXT, chat_id INT, uniq_code TEXT, is_invited BOOL, name TEXT, bio TEXT, PRIMARY KEY(chat_id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS admins(username TEXT, chat_id INT, PRIMARY KEY(chat_id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS url_of_chat(url TEXT)""")

        self.cursor.execute("""SELECT * FROM admins""")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("""INSERT INTO admins(username) VALUES (?)""", ('Fantomq0', ))
            self.connection.commit()

        self.cursor.execute("""SELECT * FROM url_of_chat""")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("""INSERT INTO url_of_chat(url) VALUES(?)""", (None, ))
            self.connection.commit()

        self.connection.commit()

    def add_user_into_table(self, chat_id: int, username: str, name: str):
        uniq_code = generate_random_letters(7)
        try:
            self.cursor.execute("""INSERT INTO users(chat_id, uniq_code, is_invited, username, name) VALUES(?, ?, ?, ?, ?)""", (chat_id, uniq_code, 0, username, name))
        except IntegrityError:
            pass

        self.connection.commit()

    def get_user(self, uniq_code: str) -> list:
        self.cursor.execute(f"""SELECT chat_id, name, username, bio, is_invited FROM users WHERE uniq_code = "{uniq_code}" """)
        return self.cursor.fetchall()[0]

    def get_uniq_code_of_user(self, chat_id: int) -> str:
        self.cursor.execute(f"""SELECT uniq_code FROM users WHERE chat_id = {chat_id}""")
        return self.cursor.fetchall()[0][0]

    def get_admins(self) -> tuple[list[str], list[int]]:
        self.cursor.execute("""SELECT username, chat_id FROM admins""")
        response = self.cursor.fetchall()

        result = [admin[0] for admin in response], [admin[1] for admin in response]
        return result

    def update_admin(self, username: str, chat_id: int):
        self.cursor.execute(f"""UPDATE admins SET chat_id = {chat_id} WHERE username = "{username}" """)
        self.connection.commit()

    def get_url_of_chat(self):
        self.cursor.execute("""SELECT url FROM url_of_chat""")
        return self.cursor.fetchall()[0][0]

    def update_url_of_chat(self, url: str):
        self.cursor.execute(f"""UPDATE url_of_chat SET url = "{url}" """)
        self.connection.commit()

    def update_bio_of_user(self, bio: str, chat_id: int):
        self.cursor.execute(f"""UPDATE users SET bio =  "{bio}" WHERE chat_id = {chat_id} """)
        self.connection.commit()

    def update_invited_of_user(self, chat_id: int):
        self.cursor.execute(f"""UPDATE users SET is_invited = 1 WHERE chat_id = {chat_id} """)
        self.connection.commit()

    def invited_of_user(self, chat_id: int):
        self.cursor.execute(f"""SELECT is_invited FROM users WHERE chat_id = {chat_id} """)
        return self.cursor.fetchall()


client_sqlite3 = SQLite3Client()


