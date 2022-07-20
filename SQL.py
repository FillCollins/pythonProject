import sqlite3

db = sqlite3.connect('Luckypas.db')
# создаем курсор
curs = db.cursor()
# обращение к методу execute для прописания и сразу выполнения команд
# сделали шапку
'''curs.execute("""
CREATE TABLE articles (title text, full_text text, views integer, avtor text)
""")'''
# заполнили поля !!!каждый раз они дублируются в запись
'''curs.execute("""
INSERT INTO articles VALUES
('Google', 'Google is a cool company...', 10, 'admin'),
('Facebook', 'Facebook is a Big company...', 15, 'danila')
""")'''
# удаление данных
'''curs.execute("""
DELETE FROM articles WHERE ROWID > 3
""")'''
# обновление данных
curs.execute("""
UPDATE articles SET avtor = 'Paskin' WHERE ROWID > 1
""")

# выборка из таблицы всех полей
'''curs.execute("""
SELECT * FROM articles
""")'''
# выборка из таблицы отдельного поля
'''curs.execute("""
SELECT title FROM articles
""")'''
# выборка из таблицы отдельного поля И ROWID!!!
'''curs.execute("""
SELECT ROWID, title FROM articles
""")'''
# выборка из таблицы отдельного поля И ROWID!!!
curs.execute("""
SELECT ROWID, title FROM articles WHERE ROWID >= 2 ORDER BY avtor DESC 
""")

# для вывода всего! обращаемся к методу fetchall
print(curs.fetchall())
# для вывода некоторых записей! обращаемся к методу
#print(curs.fetchmany(2))
# для вывода некоторых записей! НО НЕ В ФОРМАТЕ СПИСКА БЕЗ [ ] обращаемся к методу
#print(curs.fetchone())
# для вывода некоторых записей! БЕЗ [ ] И ИНДЕКСА, НО ПО ИНДЕКСУ
#print(curs.fetchone()[3])

#ПЕРЕБЕРЕМ ЦИКЛОМ ВСЮ ТАБЛИЦУ
'''inf = curs.fetchall()
for i in inf:
    print(i[1] + '\n' + i[3])'''



# обновление базы данных
db.commit()
db.close()

