import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance TEXT NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#Создание 10 записей
for i in range (1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",(f"User{i}", f"example{i}@gmail.com", f"{i}0", f"1000"))
#Конец создания


#Востановление баланса
#cursor.execute("SELECT * FROM Users ")
#users = cursor.fetchall()
#for i in range(1, len(users)+1,2):
#    cursor.execute("SELECT id, username, balance FROM Users WHERE id = ?", (f"{i}",))
#    users_balans_down = cursor.fetchall()
#    for user in users_balans_down:
#        new_balans = int(user[2]) + 500
#        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (f"{new_balans}", f"{user[0]}"))
#Конец востановления

#Снижение баланса
cursor.execute("SELECT * FROM Users ")
users = cursor.fetchall()
for i in range(1, len(users)+1,2):
    cursor.execute("SELECT id, username, balance FROM Users WHERE id = ?", (f"{i}",))
    users_balans_down = cursor.fetchall()
    for user in users_balans_down:
        new_balans = int(user[2]) - 500
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (f"{new_balans}", f"{user[0]}"))
#Конец снижения


#Удаление каждого третьего начело с первого
cursor.execute("SELECT * FROM Users ")
users = cursor.fetchall()
for i in range(1, len(users)+1,3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))
#Конец удаления третьих



#Оцистка таблицы
#cursor.execute("SELECT * FROM Users ")
#users = cursor.fetchall()
#for i in users:
#    cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i[0]}",))
#Конец оцистки

#Вывод записей в консоль
cursor.execute("SELECT * FROM Users ")
users = cursor.fetchall()
for user in users:
    print(user)
#Конец вывода

connection.commit()
connection.close()