import pymysql
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

dbConn = pymysql.connect(host='localhost', user='root', password='12345', db='pydb')

sql = "select * from lotto_tbl"

cur = dbConn.cursor()
cur.execute(sql)

rows = cur.fetchall()  # 테이블에서 모두 가져오기

lotto_df = pd.DataFrame(rows, columns=['count', 'date', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'bonus'])

lotto_df['date'] = pd.to_datetime(lotto_df['date'])
print(lotto_df['date'].dt.month) # 날짜 필드에서 월만 추출

lotto_df['month'] = lotto_df['date'].dt.month # 새로운 month column생성
print(lotto_df)

lotto_jan = lotto_df[lotto_df['month']==1]
numlist_01 = list(lotto_jan['num1'])+list(lotto_jan['num2'])+list(lotto_jan['num3'])+list(lotto_jan['num4'])+list(lotto_jan['num5'])+list(lotto_jan['num6'])+list(lotto_jan['bonus'])
print(Counter(numlist_01))

for i in range(1,13):  # 1 ~ 12 월 까지
    lotto_month_df = lotto_df[lotto_df['month'] == i]  #월별 lotto번호df
    # print(lotto_month_df)
    lotto_month_list = list(lotto_month_df['num1']) + list(lotto_month_df['num2']) + list(lotto_month_df['num3']) + list(lotto_month_df['num4']) + list(lotto_month_df['num5']) + list(lotto_month_df['num6']) + list(lotto_month_df['bonus'])
    lotto_month_data = pd.Series(Counter(lotto_month_list))
    lotto_month_data = lotto_month_data.sort_values(ascending = False) #빈도수의 내림차순으로 정렬
    lotto_month_top6 = lotto_month_data.head(6)
    # print(lotto_month_top6)
    plt.subplot(4,3,i)
    plt.subplots_adjust(left = 0.125, bottom = 0.1, right = 0.9, top = 0.9, wspace = 0.3, hspace = 0.5)
    lotto_month_top6.plot(figsize = (10,30), kind = 'bar', grid = True, title = '월별 로또당첨번호 빈도수')
    plt.title(f"{i} 월")
    plt.xlabel("번호")
    plt.ylabel("빈도수")

plt.show()

cur.close()
dbConn.close()