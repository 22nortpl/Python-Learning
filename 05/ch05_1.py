count = 0
def hanoi(disc, a, b, c):
  global count
  if disc == 1:
    count += 1
  else:
    hanoi(disc-1, a, c, b)
    count += 1
    hanoi(disc-1, b, c, a)
  return count

n = int(input("옮길 원판의 갯수를 입력해주세요 : "))
hanoi(n, "A탑", "B탑", "C탑")
print(f"이동 횟수는 {count}회 입니다.")