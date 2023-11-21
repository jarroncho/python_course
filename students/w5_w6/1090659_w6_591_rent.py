# pip install gspread oauth2client

import time
import random
import requests
from bs4 import BeautifulSoup

class House591Spider():
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
        }

    def search(self, filter_params=None, sort_params=None, want_page=1):
        """執行搜尋房屋

        Args:
            filter_params (dict): 篩選參數。
            sort_params (dict): 排序參數。
            want_page (int): 想要抓取的頁數。

        Returns:
            int: requests 房屋總數。
            list: requests 搜尋結果房屋資料。
        """
        total_count = 0
        house_list = []
        page = 0

        # 紀錄 Cookie 取得 X-CSRF-TOKEN
        session = requests.Session()
        url = 'https://rent.591.com.tw/'
        response = session.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        token_item = soup.select_one('meta[name="csrf-token"]')

        headers = self.headers.copy()
        if token_item is not None:
            headers['X-CSRF-TOKEN'] = str(token_item.get('content'))

        # 搜尋房屋
        url = 'https://rent.591.com.tw/home/search/rsList'
        params = 'is_format_data=1&is_new_list=1&type=1'
        if filter_params:
            params += ''.join([f'&{key}={value}' for key, value in filter_params.items()])
        else:
            params += '&region=1&kind=0'
        
        print(f"params={params}")
        while page < want_page:
            params += f'&firstRow={page * 30}'
            response = session.get(url, params=params, headers=headers)
            if response.status_code != requests.codes.ok:
                print('請求失敗', response.status_code)
                break
            page += 1

            response_data = response.json()
            total_count = response_data['records']
            house_list.extend(response_data['data']['data'])
            # 隨機 delay 一段時間
            time.sleep(random.uniform(2, 5))

        return total_count, house_list

    def get_house_detail(self, house_id):
        """取得房屋詳細資訊。

        Args:
            house_id (int): 房屋ID。

        Returns:
            dict: requests 房屋詳細資料。
        """
        session = requests.Session()
        url = f'https://rent.591.com.tw/home/{house_id}'
        response = session.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        token_item = soup.select_one('meta[name="csrf-token"]')

        headers = self.headers.copy()
        if token_item is not None:
            headers['X-CSRF-TOKEN'] = str(token_item.get('content'))
        headers['deviceid'] = str(session.cookies.get_dict().get('T591_TOKEN'))
        headers['token'] = str(session.cookies.get_dict().get('PHPSESSID'))
        headers['device'] = 'pc'

        url = f'https://bff.591.com.tw/v1/house/rent/detail?id={house_id}'
        response = session.get(url, headers=headers)
        if response.status_code != requests.codes.ok:
            print('請求失敗', response.status_code)
            return
        house_detail = response.json()['data']
        return house_detail


if __name__ == "__main__":
    house591_spider = House591Spider()

    # 篩選條件
    filter_params = {
        'region': '1',  # 台北
        'searchtype': '4',  # 按捷運
        'mrtline': '125',  # (位置2) 淡水信義線
        'mrtcoods': '4198,4163',  # (位置3) 新北投 & 淡水
        'multiPrice': '30000_40000',  # 租金 30000-40000
        'multiRoom': '2',  # (格局) 2房
    }

    # 排序依據
    sort_params = {
        'order': 'money',  # 租金由小到大
        'orderType': 'desc'  # 由大到小
    }

    total_count, houses = house591_spider.search(filter_params, sort_params, want_page=1)
    print('\n\n搜尋結果房屋總數：', total_count)
    print('價格\t格局\t樓層\t\t說明')

    for house in houses:
        print(f"{house['price']}{house['price_unit']}\t{house['room_str']}\t{house['floor_str']}\t{house['title']}")
