import sqlite3
import pandas as pd

conn = sqlite3.connect('s3_project.db') # db 생성 (해당 이름의 db 없을 시 생성하고 연결, 있으면 그냥 연결)


# 공원 녹지 CSV 파일 DB 연결
deco = pd.read_csv('data/eco_park.csv')
deco.to_sql('eco', conn)