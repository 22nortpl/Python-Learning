from urllib import request
target = request.urlopen("https://google.com")

target = request.urlopen("https://google.com")
output = target.read()

print(output)