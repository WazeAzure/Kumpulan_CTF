import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO 'pwncollege-web10' (user, password, flag, leak) VALUES (?, ?, ?, ?)",
            ('flag', 'flag', 'flag{fake_flag}', False)
            )

connection.commit()
connection.close()
