import pickle
import numpy as np
from flask import Flask, request, render_template #, Blueprint 
import joblib
# import sqlite3
# from dotenv import load_dotenv

# main_bp = Blueprint('main', __name__) #  url_prefix = '/main'

# conn = sqlite3.connect("section3.db")
# cur = conn.cursor()
# def sqliteconn():
#     conn = sqlite3.connect("section3.db")
#     cur = conn.cursor()
#     return conn, cur

# def postgreconn():

#     load_dotenv()

app = Flask(__name__) # initialize flask application
model = pickle.load(open('my_app/ML_Model/model.pkl', 'rb'))

# # ML Model path
# model_path = "ML_Model/model.pkl"

@app.route('/', methods = ['GET']) #=> 127.0.0.1:5000 + / => 127.0.0.1:5000/
def index():
    return render_template('index.html'), 200

# 데이터 예측 처리
@app.route('/predict', methods = ['POST'])
def make_prediction():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
    data14 = request.form['n']
    data15 = request.form['o']
    data16 = request.form['p']
    data17 = request.form['q']
    data18 = request.form['r']
    data19 = request.form['s']
    data20 = request.form['t']
    data21 = request.form['u']
    data22 = request.form['v']
    data23 = request.form['w']
    data24 = request.form['x']
    data25 = request.form['y']
    data26 = request.form['z']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24, data25, data26]])
    
    # conn, cur = sqlite3()

    # temp_list=[]
    # hum_list=[]
    # date = None

    # if request.method == 'POST':
    #     date = request.form['select']
    # cur.execute(f"""select date, round(avg(temperature),2), round(avg(humidity),2)
    #                from climate 
    #                group by date
    #                having date < '{date}' and date >= '{date}'::date -'3 day' ::interval
    #                order by date desc;""")
    # temps = cur.fetchall()

    # for t_value in temps:
    #         temp_list.append(float(t_value[1]))
    #         hum_list.append(float(t_value[2]))

    # 학습한 모델 가져오기
    # with open('my_app/ML_Model/model.pkl', 'rb') as model_file:
    #     model = pickle.load(model_file)
    pred = model.predict(arr)
    # conn.close()
    return render_template('result.html', data = pred), 200

    # # 참고 예시. 
    # if request.method == 'POST':
    #     # 업로드 파일 처리 분기
    #     file = request.files['image']
    #     if not file: return render_template('index.html', label = "No Files")
    # # 혹은 (http://aispiration.com/nlp2/nlp-ml-deployment.html)
    # def predict():
    #     data = request.get_json(force=True)
    #     prediction = model.predict([[np.array(data['exp'])]])
    #     output = prediction[0]
    #     return jsonify(output)

if __name__ == '__main__':
    # 모델 로드
    # ML_Model/model.py 선 실행 후 생성
    model = joblib.load('my_app/ML_Model/model.pkl')
    # flask 서비스 스타트
    
    app.run(debug = True) # automatically reloading enabled


# https://community.alteryx.com/t5/Alteryx-Designer-Discussions/how-to-resolve-sklearn-version-mismatch/td-p/515042
# import warnings

# with warnings.catch_warnings():
#       warnings.simplefilter("ignore", category=UserWarning)
#       estimator = joblib.load('model.pkl')