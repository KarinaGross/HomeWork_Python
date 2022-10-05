import sqlite3

with sqlite3.connect("phone_book.db") as db:
    # Create Cursor
    cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT,
    lname TEXT,
    phone_number TEXT,
    comment TEXT
   )
""")
db.commit()


def saving_username(user):
    cur.execute("INSERT INTO users(fname, lname, phone_number, comment) VALUES(?, ?, ?, ?)", user)
    db.commit()

def looking_data(second_name):
    cur.execute("SELECT * FROM users WHERE lname = ?", (second_name,))
    records = cur.fetchall()
    for row in records:
        print('ID:', row[0])
        print('Имя:', row[1])
        print('Номер', row[3])
        print('Комментарий: ', row[4], end='\n\n')

def looking_all():
    cur.execute("SELECT * FROM users")
    records = cur.fetchall()
    for row in records:
        print(row[2], row[1])

def delete_data(name, surname):
    cur.execute("DELETE FROM users WHERE (fname, lname) = (?, ?)", (name, surname))
    db.commit()
    print(f"Контакт '{surname} {name}' удален")
            


