import requests
import pprint

URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = '1063506377423532236'

def item_search(keyword):
  params = {
    'applicationId': APP_ID,
    'format': 'json',
    'keyword': keyword
  }

  res = requests.get(URL, params=params)
  res_json = res.json()

  for item in res_json['Items']:
    print(f"商品名：{item['Item']['itemName']}")
    print(f"価格：{item['Item']['itemPrice']}")

  return res_json

if __name__ == "__main__":
    keyword = input('商品名を入力してください>>>')
    item_search(keyword)