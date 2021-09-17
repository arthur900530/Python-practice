import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('TaipeiWeatherJan.csv') as csvf:
    csvReader = csv.reader(csvf)
    headerRow = next(csvReader)
    dataList = list(csvReader)
# print(dataList[0])
# print(type(headerRow))
highTemp, lowTemp,dates = [],[],[]

for row in dataList:
    highTemp.append(float(row[1]))
    lowTemp.append(float(row[3]))
    currentDate = datetime.strptime(row[0],'%Y/%m/%d')
    dates.append(currentDate)
# print(highTemp)
# print(lowTemp)
fig = plt.figure(dpi=80,figsize=(12,8))
plt.plot(dates,highTemp,dates,lowTemp)
fig.autofmt_xdate(rotation=50)
plt.fill_between(dates, highTemp, lowTemp, color='y',alpha=0.2)
plt.show()