import csv

# with open('report.csv',encoding='UTF-8-sig') as csf:
#     csvReader = csv.reader(csf)
#     listReport = list(csvReader)
#     # for row in csvReader:
#     #     print('Row %s = '%csvReader.line_num,row)
# for row in listReport:
#     print(row)
# print(listReport[3][0],listReport[3][2])

# with open('out1.csv','w',newline='') as csvf:
#     csvWriter = csv.writer(csvf)
#     csvWriter.writerow(['Name','Age','City'])
#     csvWriter.writerow(['Arthur', '20', 'Taichung'])

import pickle
# game_info = {
#     "position_X":"100",
#     "position_Y":"200",
#     "money":300,
#     "pocket":["黃金", "鑰匙", "小刀"]
# }
#
# fn = "ch22_23.dat"
# fn_obj = open(fn, 'wb')         # 二進位開啟
# pickle.dump(game_info, fn_obj)
# fn_obj.close()

# fn = "ch22_23.dat"
# fnObj = open(fn,'rb')
# info = pickle.load(fnObj)
# fnObj.close()
# print(info)

# import shelve
#
# phone = shelve.open('phonebook')
# # phone['Arthur'] = ('Arthur','0909756966','台中市')
# # phone['Jeneya'] = ('Jeneya','0905059591','台中市')
# # phone.close()
# for i in phone:
#     print(phone[i])
# phone.close()

# import xlwt
#
# n = 'out.xls'
# header = ['Phone','TV','Notebook']
# price = ['35000','18000','28000']
# wb = xlwt.Workbook()# sh = wb.add_sheet('s1',cell_overwrite_ok=True)
# for i in range(len(header)):
#     sh.write(0,i,header[i])
# for i in range(len(price)):
#     sh.write(1,i,price[i])
# wb.save(n)

import xlrd

n = 'out.xls'
wb = xlrd.open_workbook(n)
sh = wb.sheets()[0]
rows = sh.nrows
for row in range(rows):
    print(sh.row_values(row))