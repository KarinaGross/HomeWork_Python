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


# cur.execute("""CREATE TABLE IF NOT EXISTS numbers(
#    numberid INT PRIMARY KEY,
#    phone_number TEXT,
#    userid TEXT,
#    comment TEXT);
# """)
# db.commit()

def saving_username(user):
    cur.execute("INSERT INTO users(fname, lname, phone_number, comment) VALUES(?, ?, ?, ?)", user)
    db.commit()

def looking_data():
    cur.execute("SELECT * FROM users;")
    print(cur.fetchall())
