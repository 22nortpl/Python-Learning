books = [{
  "title": "혼자 공부하는 파이썬",
  "price": 18000
},{
  "title": "혼자 공부하는 머신러닝 + 딥러닝",
  "price": 26000
},{
  "title": "혼자 공부하는 자바스크립트",
  "price": 24000
}]

def price_print(book):
  return book["price"]

print("# 가장 저렴한 책")
print(min(books, key = price_print))
print()

print("# 가장 비싼 책")
print(max(books, key = price_print))