import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1"
html = requests.get(url).text
print(html)
soup = BeautifulSoup(html, 'lxml')
# 추첨일자 (Datetime 형으로 변환
date = datetime.strptime(soup.find('p', class_ = 'desc').text, '(%Y년 %m월 %d일 추첨)')
print(date)