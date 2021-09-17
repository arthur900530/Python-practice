import bs4
import requests

# htmlFile = requests.get('https://www.youtube.com/')
# print(type(htmlFile.text))
# htmlFile = open('myhtml.html',encoding='utf-8')
# objSoup = bs4.BeautifulSoup(htmlFile,'lxml')
# print(objSoup.title)
# print(objSoup.title.text)
# h1tag = objSoup.findAll('h1')
# print(type(h1tag))
# print(h1tag)
# for data in h1tag:
#     print(data.text)

htmlFile = open('myhtml.html',encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile,'lxml')
contents = objSoup.select('img')
print(len(contents))
for content in contents:
    print(content.get('src'))

# htmlFile = open('myhtml.html',encoding='utf-8')
# objSoup = bs4.BeautifulSoup(htmlFile,'lxml')
