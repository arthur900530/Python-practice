import twstock
import  matplotlib.pyplot as plt

# s2330 = twstock.Stock('2330')
# plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
# plt.plot(s2330.price)
# plt.title('台積電',fontsize=24)
# plt.show()

# s2330 = twstock.Stock('2330')
# s2330.fetch(2018, 1)
# av5 = s2330.moving_average(s2330.price,5)
# plt.plot(s2330.price)
# plt.plot(av5)
# plt.show()

s2330 = twstock.realtime.get('2330')
print(s2330)