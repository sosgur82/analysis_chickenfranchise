import time
from selenium import webdriver

wd = webdriver.Chrome('D:/Python/webdriver/chromedriver.exe')
wd.get("http://guide.ff14.co.kr/lodestone/db/item/e7ab75486d7/")
time.sleep(5)

html = wd.page_source
wd.quit()

print(html)
