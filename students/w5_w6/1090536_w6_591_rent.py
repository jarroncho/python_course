from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# 定義網頁URL
url = "https://rent.591.com.tw/?region=1&section=3,5&searchtype=1&multiPrice=5000_10000"

# 使用with語句確保webdriver正確關閉
with webdriver.Chrome() as browser:
    browser.get(url)
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
        price = item.find("div", {"class": "item-price-text"}).getText().strip()

        style = item.find("ul", {"class": "item-style"}).find_all("li")
        layout = style[0].getText().strip()
        floor = style[2].getText().strip()

        title = item.find("div", {"class": "item-title"}).getText().strip()

        result.append((price, layout, floor, title))

# 創建DataFrame
df = pd.DataFrame(result, columns=["價格", "格局", "樓層", "說明"])

# 匯出Excel檔案
df.to_excel("591_search_test.xlsx", sheet_name="台北", index=False)