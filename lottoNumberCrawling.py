# packages설치 :requests, bs4, lxml
#
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# 최신회차 크롤링 함수
def get_recent_count():
    url = "https://dhlottery.co.kr/common.do?method=main"
    html = requests.get(url).text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    recent_count = soup.find('strong', id='lottoDrwNo').text # lotto 최신회차 가져오기
    # print(recent_count)
    recent_count = int(recent_count) #최신회차값을 정수로 변경
    return recent_count

#회차별  추첨일, lotto번호, 보너스 번호를 조회하는 함수
def get_lottonumber(count):
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}"
    html = requests.get(url).text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # 추첨일자 (Datetime 형으로 변환
    date = datetime.strptime(soup.find('p', class_='desc').text, '(%Y년 %m월 %d일 추첨)')
    # print(date)
    lottoNum_list = soup.find('div', class_='num win').find('p').text.strip().split('\n')  # 1회 당첨번호 6개를 List로 변환
    # 문자열을 정수열로 변환
    lottoNum_list_int = []
    for i in lottoNum_list:
        lottoNum_list_int.append(int(i))
    # print(lottoNum_list_int)
    bonus_num = int(soup.find('div', class_='num bonus').find('p').text.strip())  # 보너스번호ㅡ
    # print(bonus_num)

    # Data Frame 형태로 변환
    lotto_dic = {'date': date, 'lottoNumber': lottoNum_list_int, 'bonusNumber': bonus_num}
    return lotto_dic

recent_count = get_recent_count()

for i in range(1, recent_count+1):
