# 변수를 선언합니다.
number = int(input("정수 입력> "))

if number % 2 == 0:
  print("""\
      입력한 문자열은 {}입니다.
      {}는(은) 짝수입니다.""".format(number, number))
else:
  print("""\
      입력한 문자열은 {}입니다.
      {}는(은) 짝수입니다.""".format(number, number))