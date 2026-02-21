min_sit = 2
max_sit = 10
total_people = 100
memo = {}

def question(remain, seated):
  key = str([remain, seated])

  if key in memo:
    return memo[key]
  if remain < 0:
    return 0
  if remain == 0:
    return 1
  count = 0

  for i in range(seated, max_sit+1):
    count += question(remain-i, i)

  memo[key] = count
  return count

print(question(total_people, min_sit))