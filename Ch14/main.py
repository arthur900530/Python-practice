import os

# print(os.getcwd())
# print(os.path.abspath('.'))
# print(os.path.abspath('..'))
# print(os.path.abspath('main.py'))

# print(os.path.relpath('D:\\'))
# print(os.path.relpath('D:\\pycharm\\pythonProject'))

# os.mkdir('testch14')
# os.rmdir('testch14')

# os.chdir('D:\\pycharm')
# os.chdir('D:\\pycharm\\Ch14')

# print(os.path.getsize('main.py'))

# print(os.listdir('.'))

# for f in os.listdir('.'):
    # print(f, os.path.getsize(f))

# import glob
# for f in glob.glob('D:\\pycharm\\Ch14\*.py'):
#     print(f)

# for dirName, sub_dirNames, fileNames in os.walk('..'):
#     print("目前工作目錄名稱:   ", dirName)
#     print("目前子目錄名稱串列: ", sub_dirNames)
#     print("目前檔案名稱串列:   ", fileNames, "\n")

# f = open('ch14_15.txt')
# data = f.read()
# f.close()
# print(data)

# f = 'ch14_15.txt'
# with open(f) as file:
#     data = file.read()
#     print(data.rstrip())
# l = [d for d in data.split('\n')]
# print(l)

# with open('ch14_15.txt') as f:
#     for line in f:
#         print(line.rstrip())

# with open('ch14_15.txt') as f:
#         flist = f.readlines()
# print(flist)
# print(globals())

# f = 'out.txt'
# with open(f, 'a') as file:
#     file.write('AAAAAAAA' + '\n')
#     file.write('BBBBBBBB' + '\n')

import shutil

# shutil.copy('out.txt','D:\\pycharm')
# shutil.copytree('D:\\pycharm\\Ch14','D:\\newCh14')

with open('D:\\pycharm\\Ch14\\ch14_15.txt', encoding='utf-8') as f:
    o = f.readlines()
print(o)