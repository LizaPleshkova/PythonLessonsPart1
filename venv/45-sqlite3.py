import sqlite3

'''
для работы с бд используется метод c ursor : делать запросы sql и получать результат
execute - для создания запроса; так же готовит данные для вставки
commit - отправляет данные\ не от cursor, а от соединения db
'''


def dict_factory(cur, row):
    '''
    получить данные в виде словаря, а не кортежа
    dir.descriptioon
    '''
    d = {}
    for idx, col in enumerate(cur.description):
        # print(idx, col, sep=' - ')
        d[col[0]] = row[idx]
    return d




db = sqlite3.connect('test_db.sqlite')#открыть соедение с бд
db.row_factory = dict_factory
cursor = db.cursor()

# создание таблицы

#  IF NOT EXISTS  - если уже создана, не пытается создать заново
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE
    )
    ''')

# добавление данных : execute and executescript

# cursor.execute("INSERT INTO users (name, email) VALUES ('Ivanov Ivan', 'ivanov@gmail.com')")
# try:
#     cursor.execute("INSERT INTO users (name, email) VALUES ('Petrov Petr', 'petrov@gmail.com')")
# except sqlite3.IntegrityError:
#     print('Unique constraint failed: users.email')

# cursor.execute("INSERT INTO users (name, email) VALUES ('Sidorov Alex', 'sidorov@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Koshkin Gray', 'koshkin@gmail.com')")

# # добавление сразу нескольких записей
# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ('John Doe', 'doe@gmail.com');
# INSERT INTO users (name, email) VALUES ('Nick Sand', 'sand@gmail.com');
# ''')

# # вставить последовательность \ ? - это маркеры, которые будут заменяться перечисляемой последовательностью
# users = [
#     ('User 1', 'user1@dmail.com',),
#     ('User 2', 'user2@dmail.com',),
#     ('User 3', 'user3@dmail.com',),
# ]
# cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
# db.commit()# сохранить транзакцию
#

# выборка данных из таблицы
# fetchone and fetchall


email = 'petrov@gmail.com'
# #sql-инъекции - не рекомендуется - небезопастно
# # cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
# # res = cursor.fetchone()# (2, 'Petrov Petr', 'petrov@gmail.com')
# #
# # print(res)
# # print(res[1])
#
# cursor.execute(f"SELECT * FROM users WHERE email = ?", (email))# со списком
# cursor.execute(f"SELECT * FROM users WHERE email = ?", (email,))# с кортежем

# cursor.execute(f"SELECT * FROM users WHERE email = ? OR name = ?", (email,'John Doe'))# позиционные параметры
# cursor.execute(f"SELECT * FROM users WHERE email = :email OR name = :name ", {'email':email, 'name': 'John Doe'})# именнованные аргументы

# cursor.execute("SELECT * FROM users")
#
# # res = cursor.fetchone()# одны запись
# res = cursor.fetchall()# список кортежей
#
# print(res)

# for user in res:
#     print(user[1], user[2])

# for user in res:
#     print(user['name'], user['email'])

# db.total_changes() # возвращает кол-во результатов, которые затронет запрос

cursor.execute("INSERT INTO users (name, email) VALUES ('User 4', 'user4@gmail.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('User 5', 'user5@gmail.com')")
db.commit()

print(db.total_changes)
db.close()

# t = ('petrov@gmail.com')
# print(type(t))#<class 'str'>