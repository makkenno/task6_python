import requests
import pandas as pd
import pprint
from pathlib import Path

URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?'
APP_ID = '1063506377423532236'

genre_id = input('ジャンルIDを入力してください>>>')
params = {
  'applicationId': APP_ID,
  'format': 'json',
  'genreId': genre_id,
}

res = requests.get(URL, params=params)
res_json = res.json()
# pprint.pprint(res_json, depth=2)

data = []
for item in res_json['Items']:
  print(f"ランク：{item['Item']['rank']}")
  print(f"商品名：{item['Item']['itemName']}")
  data.append([item['Item']['rank'],item['Item']['itemName']])

df = pd.DataFrame(data, columns=['rank', 'item_name'])
df.to_csv(Path(__file__).resolve().parent/Path('ranking.csv'), index=False)