import webbrowser
import requests

# address = input()
# webbrowser.open('https://www.google.com.tw/maps/place/' + address)

# url = 'https://hahow.in/'
# htmlFile = requests.get(url)
# # print(type(htmlFile))
# if htmlFile.status_code == requests.codes.ok:
#     print('load success')
# else:
#     print('fail')
#
# print(htmlFile.text)

# url = 'http://aaa.24ht.com.tw/'
# htmlfile = requests.get(url)
# htmlfile.raise_for_status()

# headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
#             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
#             Safari/537.36', }
# url = 'https://www.nccu.edu.tw/app/home.php'
# htmlfile = requests.get(url, headers=headers)
# htmlfile.raise_for_status()
# print("偽裝瀏覽器擷取網路資料成功")

url = 'https://hahow.in/'       # 網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                                # err是系統自訂的錯誤訊息
    print(f"網頁下載失敗: {err}")
# 儲存網頁內容
fn = 'out23_11.txt'
with open(fn, 'wb') as file_Obj:                        # 以二進位儲存
    for diskStorage in htmlfile.iter_content(10240):    # Response物件處理
        size = file_Obj.write(diskStorage)              # Response物件寫入
        print(size)                                     # 列出每次寫入大小
    print(f"以 {fn} 儲存網頁HTML檔案成功")