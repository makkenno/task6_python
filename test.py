from ichiba_item_search import item_search
from productsearch import product_search
from ichibaitemranking import ranking

def test_item_search():
  keyword = 'iPad'
  res = item_search(keyword)

  assert res["Items"]
  assert res["Items"][0]["Item"]

def test_product_search():
  keyword = 'iPad'
  res = product_search(keyword)

  assert len(res['Products']) >= 1
  assert res["Products"][0]["Product"]["minPrice"]
  assert res["Products"][0]["Product"]["maxPrice"]

def test_ranking():
  genre_id = '100227'
  res = ranking(genre_id)

  assert res["Items"][0]["Item"]["itemName"]
  assert res["Items"][0]["Item"]["itemPrice"]
