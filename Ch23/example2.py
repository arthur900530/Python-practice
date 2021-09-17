import requests
import json

# url = 'https://data.epa.gov.tw/api/v1/aqx_p_432?format=json&limit=1000&api_key=226eee43-69e8-4cd0-8ccc-1e9aa22df408'
# try:
#     aqiJsons = requests.get(url)
#     print('Successed')
# except Exception as err:
#     print('Failed')
#
# print(aqiJsons.text)
#
# with open('aqi.json','w') as f:
#     json.dump(aqiJsons.json(),f,indent=2)

with open('aqi.json') as f:
    datas = json.load(f)

for data in datas:
    county = data['County']
    siteName = data['SiteName']
    pm25 = data['PM2.5']
    date = data['ImportDate']
    print(f'城市 :{county:^5s}, 站名 :{siteName:^5s}, PM2.5值 :{pm25:^5s}, 數據日期 :{date:^5s}')