import requests
from bs4 import BeautifulSoup

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "xml")

for location in soup.find_all("location"):
    city = location.find("city").text
    data = location.find("data")

    print("도시:", city)
    print("날씨:", data.find("wf").text)
    print("최저기온:", data.find("tmn").text)
    print("최고기온:", data.find("tmx").text)
    print()