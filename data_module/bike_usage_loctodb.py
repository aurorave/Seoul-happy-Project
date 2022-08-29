import sqlite3
import pandas as pd

conn = sqlite3.connect('s3_project.db') # db 생성 (해당 이름의 db 없을 시 생성하고 연결, 있으면 그냥 연결)

# 따릉이 활발히 이용하는 지역구 #
df = pd.read_csv('data/bike_usage_loc.csv')[:30]

df = df.astype({'stationLatitude':'str'})
df = df.astype({'stationLongitude': 'str'})

df['lat_long_str'] = df['stationLatitude'] + ',' + df['stationLongitude']

# 위도, 경도 좌표 -> 주소 변환 함수 정의
from geopy.geocoders import Nominatim

def geocoding_reverse(lat_lng_str): 
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(lat_lng_str)

    return address

location_list = []
for i in range(len(df)):
  lat = df['stationLatitude'][i]
  long = df['stationLongitude'][i]
  location = geocoding_reverse(f'{lat}, {long}')
  location_list.append(location[0])

df['주소'] = location_list
df = df.drop(labels='lat_long_str',axis=1)

gu_list = []
for i in range(len(df)):
  gu = df['주소'].str.split(" ")[i][-4]
  gu_list.append(gu)

df['지역구'] = gu_list
df['지역구'] = df['지역구'].str.replace(",","")

# DB 연결

df.to_sql('bike_usage_loc_30', conn)