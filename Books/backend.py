import sqlite3


class Database:
    """This class contain all the function through which we can add,insert,delete,update,view,search
    in database"""

    def __init__(self):
        self.conn = sqlite3.connect("Books.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",
                    (title.strip().lower().replace(" ", ""), author.strip().lower().replace(" ", ""), year, isbn))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id = ?", (id,))
        self.conn.commit()


    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title=?,author = ?,year=?,isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()


    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title = ? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

# print(search("godan"))
# insert("Gaban","prem chand",1885,23456789874)
# delete(1)
# update(1,"godan","premchand",1945,987654345678)
# print(view())
