import re

# msg1 = '0909-756-966, 0939-475-197'
# phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
# phoneNum = phoneRule.search(msg1)
# phoneNum2 = phoneRule.findall(msg1)
# print(phoneNum)
# print(phoneNum2)

# msg1 = '0909-756-966, 0939-475-197'
# pattern1 = r'\d\d\d\d-\d\d\d-\d\d\d'
# pattern2 = r'(\d{4})-(\d{3})-(\d{3})'
# phoneNum = re.search(pattern2, msg1)
# print(phoneNum.group())
# print(phoneNum.group(0))
# print(phoneNum.group(1))
# print(phoneNum.group(2))
# print(phoneNum.group(3))
#
# msg2 = 'Arthur Artic tic ARTHUR'
# print(re.findall('Ar(thur|tic)', msg2, re.IGNORECASE))

# # 測試1將字串從句子分離
# msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
# pattern = '\w+'                    # 不限長度的單字
# txt = re.findall(pattern,msg)      # 傳回搜尋結果
# print(txt)
# # 測試2將John開始的字串分離
# msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
# pattern = 'John\w*'                # John開頭的單字
# txt = re.findall(pattern,msg)      # 傳回搜尋結果
# print(txt)

# # 使用隱藏文字執行取代
# msg = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
# pattern = r'CIA (\w)\w*'            # 欲搜尋FBI + 空一格後的名字
# newstr = r'\1*********'                   # 新字串使用隱藏文字
# txt = re.sub(pattern,newstr,msg)    # 執行取代
# print("取代成功: ", txt)            # 列出取代結果

