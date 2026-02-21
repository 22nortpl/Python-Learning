def mul(*values):
  i = 1
  for value in values:
    i = i * value
  return i

print(mul(5, 7, 9, 10))