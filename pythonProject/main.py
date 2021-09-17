# import makefood
#
# makefood.make_icecream('草莓醬')
# makefood.make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
# makefood.make_drink('large', 'coke')
#
# print(makefood.__name__)

# import banks
#
# jamesbank = banks.Banks('James')  # 定義Banks類別物件
# print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
# jamesbank.save_money(500)  # 存錢
# jamesbank.get_balance()  # 列出存款金額
# hungbank = banks.Shilin_Banks('Hung')  # 定義Shilin_Banks類別物件
# print("Hung's banks  = ", hungbank.bank_title())  # 列

# import random
#
# alphabet = ['a', 'b', 'c', 'd', 'e']
# random.shuffle(alphabet)
# print(alphabet)

# import random
#
# random.seed(5)
# lotterys = random.sample(range(1,50),7)
# specialNum = lotterys.pop()
# print(sorted(lotterys), specialNum)

# import time
# time.process_time()
# alphabet = ['a', 'b', 'c', 'd', 'e']
# print(time.asctime())
# print(time.ctime())
# for a in alphabet:
#     print(a)
#     time.sleep(1)
# e_time = time.process_time()
# print(e_time)

# import sys
# print(sys.version,'\n',sys.version_info)
# msg = sys.stdin.readline(3)
# print(msg)
# sys.stdout.write('I love Python')
# print(sys.platform)
# for p in sys.path:
#     print(p)
# print(sys.getwindowsversion())
# print(sys.executable)
# print(sys.getrecursionlimit())

# import calendar
# print(calendar.isleap(2020))
# print(calendar.month(2022,5))
# print(calendar.calendar(2021))
# print(calendar.monthrange(2021,9))

# from collections import Counter
#
# al = ['a', 'b', 'c', 'd', 'a', 'a', 'a', 'b', 'b','c']
# ad = Counter(al)
# print(type(ad),ad)
# print(ad.most_common())

# import sys
# from pprint import pprint
# print(sys.path, '\n')
# pprint(sys.path)

# import itertools

# for i in itertools.accumulate((1,2,3,4,5),lambda x, y : x*y):
#     print(i)

# x = range(1000)
# print(type(x))
# for i in itertools.combinations(x,2):
    # print(i)

# import random
#
# trials = 8000000
# hits = 0
# for i in range(trials):
#     x = random.random()*2 - 1
#     y = random.random()*2 - 1
#     if(x * x + y * y <= 1):
#         hits += 1
# print(4*hits / trials)

# import string
#
# def encrypt(text, encryDict):  # 加密文件
#     cipher = []
#     for i in text:  # 執行每個字元加密
#         v = encryDict[i]  # 加密
#         cipher.append(v)  # 加密結果
#     return ''.join(cipher)  # 將串列轉成字串
#
# def decrypt(text, decryDict):
#     cipher = []
#     for i in text:
#         v = decryDict[i]
#         cipher.append(v)
#     return ''.join(cipher)
#
# abc = string.printable[:-5]  # 取消不可列印字元
# print(type(abc))
# subText = abc[-3:] + abc[:-3]  # 加密字串
# encry_dict = dict(zip(subText, abc))  # 建立字典
# print("列印編碼字典\n", encry_dict)  # 列印字典
# decryDict = dict(zip(abc,subText))
#
# msg = 'If the implementation is easy to explain, it may be a good idea.'
# ciphertext = encrypt(msg, encry_dict)
# decrytext = decrypt(ciphertext, decryDict)
#
# print("原始字串 ", msg)
# print("加密字串 ", ciphertext)
# print("解密字串 ", decrytext)

