import pymysql
import pandas as pd

dbConn = pymysql.connect(host = 'localhost', user = 'root', password = '12345', db = 'pydb')
sql = 'select * from lotto_tbl'

cur = dbConn.cursor()
cur.execute(sql)

rows = cur.fetchall()

lotto_df = pd.DataFrame(rows, columns = ['count','date','num1','num2','num3','num4','num5','num6','bonus'])
print(lotto_df)