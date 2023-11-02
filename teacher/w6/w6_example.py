from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# 安裝Chrome驅動程式及建立Chrome物件
browser = webdriver.Chrome()
browser.get(
    "https://rent.591.com.tw/?region=1&section=3,5&searchtype=1&multiPrice=5000_10000")

time.sleep(5)
soup = BeautifulSoup(browser.page_source, "lxml")
content = soup.find("div", {"class": "list-container-content"})

content_1 = content.find("section", {"class": "vue-list-rent-content"})
content_2 = content_1.find("div", {"class": "switch-list-content"})
contents = content_2.find_all("section", {"class": "vue-list-rent-item"})

result = []
for content in contents:
    
    item = content.find("div", {"class": "rent-item-right"})

    # 活動名稱
    title = item.find(
        "div", {"class": "item-title"}).getText().strip()

    # 價格
    price = item.find(
        "div", {"class": "item-price-text"}).getText().strip()

  
    result.append((title, price))

df = pd.DataFrame(result, columns=["活動名稱", "價格"])



df.to_excel("591_search.xlsx",
                 sheet_name="台北",
                 index=False)  # 匯出Excel檔案(不寫入資料索引值)

browser.quit()  # 關閉Chrome瀏覽器
