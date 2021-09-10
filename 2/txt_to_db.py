#https://www.pythonforthelab.com/blog/storing-data-with-sqlite/
import csv
import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

#cur.execute('CREATE TABLE experiments (id INT, title VARCHAR, amount FLOAT, created_at VARCHAR, tags VARCHAR)')



#


# # Primer instruncion correra siempre al inicio y leera db.txt y lo guarda en mi class expense_tracker
# with open('db.txt', 'r', encoding="utf8") as f: # alinicar programa lee db.txt y excribe en mi objeto
#     reader = csv.reader(f)
#     for idx, row in enumerate(reader): #itera sbre cada linea de db.txt
#         if idx == 0:#Si el a linea 0 no hace nada porque solo tiene titulos
#             continue
#         if row == []: # si la linea esta vacia no hace nada
#             continue
#         #print(row[0], row[1], row[2],row[3],row[4])
#         #sqlite no acep variables po eso se ocupa ? y despues las variables
#         cur.execute('INSERT INTO experiments (id, title, amount,created_at, tags) values (?,?,?,?,?)',(row[0], row[1], row[2],row[3],row[4]))
# # si tienen informacion añade cada row[n] es un elemento de 6,cacahuates,5.0,2020-12-03,['chatarra']
# """ id,title,amount,created_at,tags
# 2,papas,12.2,2020-12-03,"['comida', 'snack']" """

cur.execute('SELECT * FROM experiments')
data = cur.fetchall()
print(data)

conn.commit()
conn.close()