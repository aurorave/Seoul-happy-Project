# import sqlite3
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///s3_project.db')
df = pd.read_sql('SELECT * FROM data_happy', engine)
data = df.copy()

# 데이터 값 변경 원할 시 아래 코드 활용, 작성할 것#
# data.replace({'ptSexCd': {'f': 1, 'm': 2},
#             'statsTrgtNm': {'무직': 1, '회사원': 2}}
#             )


# 머신러닝 모델

# import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
# import requests
# import json

# 기존 내용 #
# df = pd.read_csv('./data/data.csv')
# data = df.copy()

data = data.iloc[:, 2:] # index, GU 삭제
target = 'wtb1'
features = data.drop(columns = [target]).columns

X = data[features]
y = data[target]

# 임시
print('Model Export Running')

# 학습 훈련 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# 랜덤 포레스트 객체 생성 및 학습
random_forest = RandomForestRegressor(max_features = 5, n_estimators = 10)
random_forest.fit(X_train, y_train)

# y_pred = random_forest.predict(X_test)


# pickle화 (1)
pickle.dump(random_forest, open('my_app/ML_Model/model.pkl','wb')) # model.pkl 생성

# pickle화 (2) 레퍼런스 코드
# with open('model.pkl', 'wb') as pickle_file:
#     pickle.dump(random_forest, pickle_file)


# 하이퍼파라미터 튜닝은??


# 참고

# dataset = pd.read_csv('data/Salary_Data.csv')
# X = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, 1].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 777)

# salary_model = LinearRegression()
# salary_model.fit(X_train, y_train)

# y_pred = salary_model.predict(X_test)

# pickle.dump(salary_model, open('model/salary_model.pkl','wb'))