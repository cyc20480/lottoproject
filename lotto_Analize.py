import pymysql
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

dbConn = pymysql.connect(host = 'localhost', user = 'root', password = '12345', db = 'pydb')
sql = 'select * from lotto_tbl'

cur = dbConn.cursor()
cur.execute(sql)

rows = cur.fetchall()  #테이블에서 모두 가져오기

lotto_df = pd.DataFrame(rows, columns = ['count','date','num1','num2','num3','num4','num5','num6','bonus'])
print(lotto_df)

lottoNum_list = list(lotto_df['num1'])+list(lotto_df['num2'])+list(lotto_df['num3'])+list(lotto_df['num4'])+list(lotto_df['num5'])+list(lotto_df['num6'])+list(lotto_df['bonus'])
print(lottoNum_list)

lottoNum_counter = Counter(lottoNum_list)  #각 숫자의 당첨 빈도수를 내림차순으로 Count
print(lottoNum_counter)

lotto_series = pd.Series(lottoNum_counter)  # 인덱스와 값을 자동생성
print(lotto_series)

lotto_data = lotto_series.sort_index()  # 1 ~ 45 까지 오름차순 정리
print(lotto_data)

lotto_data.plot(figsize=(20,30), kind = 'barh', grid = True, title = 'Korea Lotto' )
plt.show()

cur.close()
dbConn.close()