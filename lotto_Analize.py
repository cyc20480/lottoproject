import pymysql
import pandas as pd

dbConn = pymysql.connect(host = 'localhost', user = 'root', password = '12345', db = 'pydb')
sql = 'select * from lotto_tbl'

cur = dbConn.cursor()
cur.execute(sql)

rows = cur.fetchall()  #테이블에서 모두 가져오기

lotto_df = pd.DataFrame(rows, columns = ['count','date','num1','num2','num3','num4','num5','num6','bonus'])
print(lotto_df)

lottoNum_list = list(lotto_df['num1'])+list(lotto_df['num2'])+list(lotto_df['num3'])+list(lotto_df['num4'])+list(lotto_df['num5'])+list(lotto_df['num6'])+list(lotto_df['bonus'])
print(lottoNum_list)