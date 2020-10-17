import sqlite3 # импортируем базу
conn = sqlite3.connect("test_db.sqlite") #создаём базу данных
c = conn.cursor() #создаём курсор
c.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name='users';")
print(c.fetchone())

c.execute("""
CREATE TABLE IF NOT EXISTS
    users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE
    );
""")

c.execute("""
CREATE TABLE IF NOT EXISTS 
    cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT UNIQUE,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
""")

c.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(c.fetchall()) #опасный метод так как возвращает всё что есть в БД

c.execute("""INSERT INTO users (name, email) VALUES ('Dima', 'D2MACC@mail.ru')""")
c.execute("""INSERT INTO users (name, email) VALUES ('Valentina', 'dissolute_angel@mail.ru')""")
conn.commit #отправляет созданные транзакции в базу данных

c.execute("""SELECT * FROM users""")
print(c.fetchall())

c.execute("""SELECT * FROM users WHERE id=2""")
print(c.fetchall())

c.execute("""INSERT INTO cars (model, user_id) VALUES ('Фольцваген (поло)', 1)""")
c.execute("""INSERT INTO cars (model, user_id) VALUES ('Тайота (ярис)', 1)""")
c.execute("""INSERT INTO cars (model, user_id) VALUES ('Порш (Каен)', 2)""")
c.execute("""INSERT INTO users (name, email) VALUES ('Lera', 'lera_gepard@mail.ru')""")
conn.commit

c.execute("""SELECT * FROM cars""")
print(c.fetchall())

c.execute("""SELECT u.id, u.name, u.email, c.model FROM users u LEFT JOIN cars c ON u.id=c.user_id""")

print("id\t", "name\t", "email\t", "cars")
for row in c.fetchall():
    print(*row, sep="\t")


c.execute("""SELECT u.id, u.name, u.email, count(c.model) FROM users u LEFT JOIN cars c ON u.id=c.user_id GROUP BY u.email""")

print("id\t", "name\t", "email\t", "cars")
for row in c.fetchall():
    print(*row, sep="\t")