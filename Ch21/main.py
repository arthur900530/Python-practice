import json

# listNumbers = [5, 10, 20, 1]            # 串列資料
# tupleNumbers = (1, 5, 10, 9)            # 元組資料
# jsonData1 = json.dumps(listNumbers)     # 將串列資料轉成json資料
# jsonData2 = json.dumps(tupleNumbers)    # 將串列資料轉成json資料
# print("串列轉換成json的陣列", jsonData1)
# print("元組轉換成json的陣列", jsonData2)
# print("json陣列在Python的資料類型 ", type(jsonData1))

# jObj = '{"b":80,"a":25,"c":60}'
# dObj = json.loads(jObj)
# print(dObj)
# print(type(dObj))

# fn = 'worldpopulation.json'
# with open(fn) as fobj:
#     datas = json.load(fobj)
# for data in datas:
#     rank = data['Rank']
#     country = data['country']
#     population = data['population']
#     percent = float(data['World'])*100
#     print('Rank: ',rank,
#           'Country: ',country,
#           'Population: ',population,
#           'Percent: ',percent,'%')

import pygal.maps.world
# print(pygal.maps.__path__)

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Some countries'
worldmap_chart.add('F countries', ['fr', 'fi'])
worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                                   'mk', 'ml', 'mm', 'mn', 'mo',
                                   'mr', 'mt', 'mu', 'mv', 'mw',
                                   'mx', 'my', 'mz'])
worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
worldmap_chart.render()