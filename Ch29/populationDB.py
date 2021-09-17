import sqlite3
import csv
import matplotlib.pyplot as plt

# conn = sqlite3.connect('populations.db')
# sql = '''Create table population(
#             area text,
#             male int,
#             female int,
#             total int)'''
# conn.execute(sql)

# with open('Taipei_Population.csv')as csvFile:
#     csvReader = csv.reader(csvFile)
#     listCsv = list(csvReader)
#     csvData = listCsv[4:]
#     for row in csvData:
#         area = row[0]
#         male = int(row[7])
#         female = int(row[8])
#         total = int(row[6])
#         x = (area,male,female,total)
#         sql = 'INSERT INTO population values(?,?,?,?)'
#         conn.execute(sql,x)
#         conn.commit()
#     results = conn.execute('SELECT*FROM population')
#     for r in results:
#         print('area  : ',r[0])
#         print('male  : ', r[1])
#         print('female: ', r[2])
#         print('total : ', r[3])
#     conn.close()

# 以上讀CSV後寫入，以下讀資料庫

conn = sqlite3.connect('populations.db')
results = conn.execute('SELECT*FROM population')

area, male, female, total = [],[],[],[]
for r in results:
    area.append(r[0])
    male.append(r[1])
    female.append(r[2])
    total.append(r[3])
conn.close()

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
seq = area
m = plt.plot(seq, male,'-*',label='男性人口數')
f = plt.plot(seq, female,'-o',label='女性人口數')
t = plt.plot(seq, total,'-^',label='總人口數')

plt.legend(loc='best')
plt.title(u"台北市", fontsize=24)
plt.xlabel("2019年", fontsize=14)
plt.ylabel("人口數", fontsize=14)

plt.show()

