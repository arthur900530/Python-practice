import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib
import numpy as np
from pylab import mpl
# from random import randint

# squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
# data1 = [0, 1, 3, 6, 10, 15, 21, 28, 36]
# plt.plot(squares, lw=5, c='m',ls='-.',label='square')
# plt.plot(data1, lw=5, label='data1')
# plt.legend(loc='lower left',bbox_to_anchor=(1,0))
# # plt.plot(range(len(squares)),squares,'g.',range(len(squares)),data1,'r-o')
# plt.axis([0,len(squares),0,max(squares)])
# plt.title('Test', fontsize=20)
# plt.xlabel('Value', fontsize=16)
# plt.ylabel('Square', fontsize=16)
# plt.tick_params(axis='both',labelsize=12,color='red')
# plt.tight_layout(pad=10)
# plt.grid()
# plt.savefig('out1.jpg',bbox_inches='tight')
# plt.show()

# fig = img.imread('out1.jpg')
# plt.imshow(fig)
# plt.show()

# x1 = np.linspace(0,10,num=12)
# print(type(x1), x1)
# x2 = np.arange(1,12,2)
# print(type(x2), x2)

# x = np.linspace(0,10,500)
# y = np.sin(x)
# plt.scatter(x,y,c='m')
# plt.show()

# left = -2 * np.pi
# right = 2 * np.pi
# x = np.linspace(left, right, 100)
#
# f1 = 2 * np.sin(x)
# f2 = np.sin(2*x)
# f3 = 0.5 * np.sin(x)
#
# plt.plot(x, f1)
# plt.plot(x, f2)
# plt.plot(x, f3)
# plt.show()

# x = np.linspace(0,5,500)
# y = 1 - 0.5*np.abs(x-2)
# lwidth = (1+x)**2
# plt.scatter(x,y,s=lwidth,c='g')
# plt.show()

# x = np.linspace(0,5,500)
# y = 1 - 0.5*np.abs(x-2)
# t = y
# plt.scatter(x,y,s=50,c=t,cmap='binary')
# plt.fill_between(x,0,y,color='g',alpha=0.4)
# plt.colorbar()
# plt.show()

# while True:
#     x = np.random.random(100)
#     y = np.random.random(100)
#     t = x
#     plt.scatter(x,y,c=t,cmap='brg')
#     plt.show()
#     yn = input('Continue? y/n')
#     if yn == 'n' or yn == 'N':
#         break

# data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
# data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
# seq = [1, 2, 3, 4, 5, 6, 7, 8]
# plt.figure(1)                                   # 建立圖表1
# plt.plot(seq, data1, '-*')                      # 繪製圖表1
# plt.figure(2)                                   # 建立圖表2
# plt.plot(seq, data2, '-o')                      # 以下皆是繪製圖表2
# plt.title("Test Chart 2", fontsize=24)
# plt.xlabel("x-Value", fontsize=14)
# plt.ylabel("y-Value", fontsize=14)
# plt.show()

# data1 = [1, 2, 3, 4, 5, 6, 7, 8]
# data2 = [1, 4, 9, 16, 25, 36, 49, 64]
# seq = [1, 2, 3, 4, 5, 6, 7, 8]
# plt.subplot(1,2,1)
# plt.plot(seq,data1,'-*')
# plt.subplot(1,2,2)
# plt.plot(seq,data2,'-o')
# # plt.title("Test Chart 2", fontsize=24)
# # plt.xlabel("x-Value", fontsize=14)
# # plt.ylabel("y-Value", fontsize=14)
# plt.show()

# votes = [135, 412, 397]
# x = np.arange(len(votes))
# plt.bar(x,votes,0.35)
# plt.title('Election Results')
# plt.xticks(x,('James','Peter','Norton'),fontsize=20)
# plt.yticks(np.arange(0,450,30))
# plt.ylabel('Number of votes')
# plt.show()

# sorts = ["Travel", "Entertainment", "Education", "Transporation", "Food"]
# fee = [8000, 2000, 3000, 5000, 6000]
#
# plt.pie(fee, labels=sorts, explode=(0.1, 0.2, 0.3, 0.4, 0.5),
#         autopct="%2.2f%%")
# plt.show()

mpl.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]  # 使用黑體
mpl.rcParams["axes.unicode_minus"] = False  # 讓可以顯示負號

sorts = [u"交通", u"娛樂", u"教育", u"交通", u"餐費"]
fee = [8000, 2000, 3000, 5000, 6000]

plt.pie(fee, labels=sorts, explode=(0, 0.2, 0, 0, 0),
        autopct="%1.2f%%")  # 繪製圓餅圖
plt.show()

# print(matplotlib.__file__)
#
# import matplotlib.font_manager
#
# a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
#
# for i in a:
#     print(i)