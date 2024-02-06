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
lottoNum_list = soup.find('div', class_='num win').find('p').text.strip().split('\n') #1회 당첨번호 6개를 List로 변환
# 문자열을 정수열로 변환
lottoNum_list_int = []
for i in lottoNum_list:
    lottoNum_list_int.append(int(i))
print(lottoNum_list_int)
bonus_num = int(soup.find('div', class_='num bonus').find('p').text.strip())#보너스번호ㅡ
print(bonus_num)

# Data Frame 형태로 변환..
lotto_dic = {'date': date, 'lottoNumber':lottoNum_list_int, 'bonusNumber':bonus_num }
print(lotto_dic)
