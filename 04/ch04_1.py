numbers = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
sort = {}

for number in numbers:
  if number in sort:
    sort[number] = sort[number] + 1
  else:
    sort[number] = 1

print("""{}에서
사용된 숫자의 종류는 {}개 입니다.
참고: {}""".format(numbers, len(sort), sort))