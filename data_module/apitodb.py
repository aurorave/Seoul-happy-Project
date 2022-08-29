import sqlite3
import pandas as pd
import json
import requests
from datetime import date, timedelta
from collections import defaultdict

conn = sqlite3.connect('s3_project.db') # db 생성 (해당 이름의 db 없을 시 생성하고 연결, 있으면 그냥 연결)

# 따릉이 API 데이터 수집 및 DB 연결
for h in range(24):
    for i in range(1, 2002, 1000):
        dic = defaultdict(list)
        today = date.today()
        yesterday = date.today() - timedelta(1)

        if i == 2001:
            url = f'http://openapi.seoul.go.kr:8088/59576858527a70613730576941784e/json/bikeListHist/{2001}/{2872}/{yesterday.strftime("%Y%m%d")}{h}'

        else:
            url = f'http://openapi.seoul.go.kr:8088/59576858527a70613730576941784e/json/bikeListHist/{i}/{i + 999}/{yesterday.strftime("%Y%m%d")}{h}'

        response = requests.get(url)
        json_ob = json.loads(response.content)
        json_ar = json_ob.get('getStationListHist')
        json_ar1 = json_ar.get('row')

        for j in json_ar1:
            stationName = j.get('stationName')
            if stationName[0].isdigit():
                stationName = stationName[5:].lstrip().rstrip()
            dic['Date'].append(f'{yesterday.strftime("%Y-%m-%d")}" "{h}')
            dic['stationId'].append(j.get('stationId'))
            dic['stationName'].append(stationName)
            dic['parkingBike'].append(j.get('parkingBikeTotCnt'))
            dic['shared'].append(j.get('shared'))
            dic['rackTotCnt'].append(j.get('rackTotCnt'))
            dic['stationLatitude'].append(j.get('stationLatitude'))
            dic['stationLongitude'].append(j.get('stationLongitude'))
        dataf = pd.DataFrame(dic)
        dataf.to_sql(name='bike', con=conn, if_exists='append', index=False)
# end = time.time()
# print(f"{end - start:.5f} sec")