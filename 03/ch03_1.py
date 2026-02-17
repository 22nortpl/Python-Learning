import datetime

now = datetime.datetime.now()
message = input("입력 : ")

if "안녕" in message:
  print("> 안녕하세요.")
elif "지금 몇 시" in message:
  print("> 지금은 {}시 {}분 {}초입니다.".format(now.hour, now.minute, now.second))
else:
  print("> " + message)