import sqlite3
import pandas as pd

conn = sqlite3.connect('s3_project.db') # db 생성 (해당 이름의 db 없을 시 생성하고 연결, 있으면 그냥 연결)


# 행복 수준 CSV 파일 DB 연결
dt = pd.read_csv('my_app/data/data1.csv')
dt.to_sql('data_happy', conn)
# cur = conn.cursor() # cursor 객체 생성
