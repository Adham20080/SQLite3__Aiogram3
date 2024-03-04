import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    username VARCHAR(255),
    user_id INTEGER
)''')


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, first_n, last_n, user_n, user_id):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO users (first_name, last_name, username, user_id) VALUES (?, ?, ?, ?)",
                (first_n, last_n, user_n, user_id))

    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM users").fetchall()


conn.commit()
conn.close()
