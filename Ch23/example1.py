import bs4
import requests

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'
html = requests.get(url)
print('Downloading...')
html.raise_for_status()
print('Finish download !')

objSoup = bs4.BeautifulSoup(html.text,'lxml')
dataTag = objSoup.select('.contents_box02')
print('Length:',len(dataTag))
# for i in dataTag:
#     print(i)
balls = dataTag[0].find_all('div',{'class':'ball_tx ball_green'})
redBall = dataTag[0].find_all('div',{'class':'ball_red'})
for i in range(6):
    print(balls[i].text, end=' ')
print('\n',redBall[0].text)