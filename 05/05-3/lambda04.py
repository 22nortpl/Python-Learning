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

print("# 가격 오름차순 정렬")
books.sort(key=lambda book: book["price"])
for book in books:
  print(book)