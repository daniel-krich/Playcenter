import json
import os
import sqlite3 as sqlite


def connect_sqlite_users(path):
    if os.path.exists(path):
        return sqlite.connect(path)
    else:
        con = sqlite.connect(path)
        con.execute("""
        CREATE TABLE Users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT unique NOT NULL,
          pswd TEXT NOT NULL,
          admin INTEGER,
          points INTEGER
        );
        """)
        return con


class User:
    def __init__(self, db, user_id, username, password, is_admin, points):
        self.db_con = db
        self.id = user_id
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.points = points

    def save(self):
        self.db_con.execute("UPDATE Users SET points = ?, pswd = ? WHERE id = ?", (self.points, self.password, self.id))
        self.db_con.commit()


class Accounts:
    def __init__(self, path_to_db):
        self.current = None
        self.db_con = connect_sqlite_users(path_to_db)
        self.db_cursor = self.db_con.cursor()

    def login(self, username, password):
        self.db_cursor.execute("SELECT * FROM Users WHERE username = ? AND pswd = ?", (username, password))
        account = self.db_cursor.fetchone()
        if account is not None:
            self.current = User(self.db_con, int(account[0]), account[1], account[2],
                                int(account[3]), int(account[4]))  # id, user, pass, is_adm, points
            return True

        return False

    def logout(self):
        if self.current is not None:
            self.current.save()
            self.current = None
            return True
        else:
            return False

    def change_pass(self, new_password, repeat_password):
        if self.current is not None and len(new_password) >= 5 and new_password == repeat_password:
            self.current.password = new_password
            self.current.save()
            return True
        else:
            return False

    def insert_user(self, username, password, repeat_password):
        try:
            if len(username) >= 5 and len(password) >= 5 and password == repeat_password:
                self.db_cursor.execute("INSERT INTO Users('username', 'pswd', 'admin', 'points') VALUES(?, ?, 0, 0)",
                                       (username, password))
                self.db_con.commit()
                self.db_cursor.execute("SELECT * FROM Users WHERE username = ? AND pswd = ?", (username, password))
                account = self.db_cursor.fetchone()
                if account is not None:
                    self.current = User(self.db_con, int(account[0]), account[1], account[2],
                                        int(account[3]), int(account[4]))
                    return True

            return False

        except sqlite.Error:
            return False

    def delete_user(self, username):
        if self.current is not None:
            if self.current.username != username:
                self.db_cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
                account = self.db_cursor.fetchone()
                if account is not None:
                    self.db_cursor.execute("DELETE FROM Users WHERE username = ?", (username,))
                    self.db_con.commit()
                    return True
                return False
            else:
                return False
        else:
            return False

    def all_users(self):
        self.db_cursor.execute("SELECT * FROM Users")
        accounts = self.db_cursor.fetchall()
        return accounts


