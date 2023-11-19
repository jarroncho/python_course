import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# 安裝Chrome驅動程式及建立Chrome物件
browser = webdriver.Chrome()
browser.get(
    "https://rent.591.com.tw/?region=1&section=3,8&searchtype=1&multiPrice=20000_30000")

time.sleep(5)
soup = BeautifulSoup(browser.page_source, "lxml")
content = soup.find("div", {"class": "list-container-content"})

content_1 = content.find("section", {"class": "vue-list-rent-content"})
content_2 = content_1.find("div", {"class": "switch-list-content"})
contents = content_2.find_all("section", {"class": "vue-list-rent-item"})

result = []
for content in contents:

    item = content.find("div", {"class": "rent-item-right"})

    # 價格
    price = item.find(
        "div", {"class": "item-price-text"}).getText().strip()

    # 格局
    # 樓層
    roomAndFloor = item.find("ul", {"class": "item-style"}).find_all("li")
    if len(roomAndFloor) == 4:
        room = roomAndFloor[1].getText().strip()
        floor = roomAndFloor[3].getText().strip()
    else:
        room = ""
        floor = roomAndFloor[2].getText().strip()

    # 說明
    title = item.find(
        "div", {"class": "item-title"}).getText().strip()

    result.append((price, room, floor, title))

df = pd.DataFrame(result, columns=["價格", "格局", "樓層", "說明"])

df.to_excel("C:\\Users\\吳任輝\\Download\\591_search.xlsx",
            sheet_name="台北",
            index=False)  # 匯出Excel檔案(不寫入資料索引值)

browser.quit()  # 關閉Chrome瀏覽器