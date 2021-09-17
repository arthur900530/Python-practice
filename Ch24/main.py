import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
# print(type(browser))

url = 'https://deepmind.com.tw/'
browser.get(url)

time.sleep(3)
browser.refresh()
time.sleep(3)
browser.quit()

# ele = browser.find_element_by_tag_name('body')
# time.sleep(3)
# ele.send_keys(Keys.PAGE_DOWN)
# time.sleep(3)
# ele.send_keys(Keys.END)