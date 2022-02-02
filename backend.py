import sqlite3

# sqlite kniznica


def connect():
    conn = sqlite3.connect("shopdata.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, uzivatel, knihy)")
    conn.commit()
    conn.close()


def insert(uzivatel, knihy):
    conn = sqlite3.connect("shopdata.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)", (uzivatel, knihy))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("shopdata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(uzivatel="", knihy=""):
    conn = sqlite3.connect("shopdata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE uzivatel=? OR knihy=?",
                (uzivatel, knihy))
    row = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("shopdata.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id))
    conn.commit()
    conn.close()


def update(id, uzivatel, knihy):
    conn = sqlite3.connect("shopdata.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET uzivatel=?m knihy=?"(uzivatel, knihy))
    conn.commit()
    conn.close()


connect()
