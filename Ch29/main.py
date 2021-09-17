import sqlite3

conn = sqlite3.connect('myData.db')
# sql = '''Create table students(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name text,
#             gender text)'''
# x = ('Arthur Chien','m')
# sql = '''insert into students(name,gender)values(?,?)'''
sql = 'SELECT*FROM students'
results = conn.execute(sql)
allStudents = results.fetchall()
# conn.commit()
for s in allStudents:
    print(s)
conn.close()