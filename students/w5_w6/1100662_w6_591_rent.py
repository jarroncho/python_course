from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# 安裝Chrome驅動程式及建立Chrome物件
browser = webdriver.Chrome()
browser.get(
    'https://rent.591.com.tw/?section=3,8&searchtype=1&multiPrice=20000_30000')

time.sleep(5)
soup = BeautifulSoup(browser.page_source, "lxml")
content = soup.find("div", {"class": "list-container-content"})

content_1 = content.find("section", {"class": "vue-list-rent-content"}) # type: ignore
content_2 = content_1.find("div", {"class": "switch-list-content"})# type: ignore
contents = content_2.find_all("section", {"class": "vue-list-rent-item"})# type: ignore

result = []
for content in contents:

    #說明
    item = content.find("div", {"class": "rent-item-right"})

    #格局/樓層
    abc = item.find("ul", {"class": "item-style"})
    kind =abc.find_all("li")
    if len(kind)==4:
        style=kind[1].getText().strip()
    else:
        style=' '
    floor=kind[-1].getText().strip()

    # 活動名稱
    title = item.find(
        "div", {"class": "item-title"}).getText().strip()

    # 價格
    price = item.find(
        "div", {"class": "item-price-text"}).getText().strip()
    
    result.append((price,style,floor,title,))

df = pd.DataFrame(result, columns=["價格","格局","樓層","說明"])



df.to_excel("591_search.xlsx",
                 sheet_name="台北",
                 index=False)  # 匯出Excel檔案(不寫入資料索引值)

browser.quit()  # 關閉Chrome瀏覽器