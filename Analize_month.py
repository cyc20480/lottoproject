import pymysql
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

dbConn = pymysql.connect(host='localhost', user='root', password='12345', db='pydb')

sql = "select * from lotto_tbl"

cur = dbConn.cursor()
cur.execute(sql)

rows = cur.fetchall()  # 테이블에서 모두 가져오기

lotto_df = pd.DataFrame(rows, columns=['count', 'date', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'bonus'])

lotto_df['date'] = pd.to_datetime(lotto_df['date'])