import requests
import pprint

URL = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426?'
APP_ID = '1063506377423532236'

keyword = input('商品名を入力してください>>>')
params = {
  'applicationId': APP_ID,
  'format': 'json',
  'keyword': keyword,
}

res = requests.get(URL, params=params)
res_json = res.json()

for product in res_json['Products']:
  print(f"商品名：{product['Product']['productName']}")
  print(f"最低価格：{product['Product']['minPrice']}")
  print(f"最高価格：{product['Product']['maxPrice']}")