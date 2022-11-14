
from flask import Flask, render_template, request
import json
from date import get_date
from data import data

from weather_forecast import update_time, get_countys, get_weather

app = Flask(__name__)


Refresh = False


# 首頁
@app.route('/')
@app.route('/index')
def index1():
    return render_template('./index.html')


@app.route('/flask_test/', methods=['GET', 'POST'])
def index():
    global Refresh
    if request.method == 'POST':
        if request.form.get('county_btn'):
            Refresh = True

    date = get_date()
    values = get_weather()
    countys = get_countys()
    return render_template('./flask_test.html', **locals())


@app.route('/weather/<county>')
def weather(county):
    county = request.form.get('select_countys')
    values = get_weather(county)
    countys = get_countys()
    return json.dumps(values, ensure_ascii=False)

# no2


@app.route('/data')
def data_s():
    columns, values = data()
    date = values[0][3]
    return render_template('./data.html', **locals())

# no2


@app.route('/data-no2', methods=['GET', 'POST'])
def data_no2():
    columns, values = data()
    # sitename=測站名稱
    sitename = [value[0] for value in values]
    no2 = [value[2] for value in values]
    aqi = [value[1] for value in values]
    pm25 = [value[4] for value in values]
    return json.dumps({'aqi': aqi, 'sitename': sitename, 'no2': no2, 'pm25': pm25}, ensure_ascii=False)

# pm25


@app.route('/data_2')
def data_2():
    columns, values = data()
    date = values[0][3]
    return render_template('./pm25.html', **locals())

# pm25


@app.route('/data-pm25', methods=['GET', 'POST'])
def data_pm25():
    columns, values = data()
    # sitename=測站名稱
    sitename = [value[0] for value in values]
    pm25 = [value[4] for value in values]
    return json.dumps({'sitename': sitename, 'pm25': pm25}, ensure_ascii=False)


# so2
@app.route('/data_3')
def data_3():
    columns, values = data()
    date = values[0][3]
    return render_template('./so2.html', **locals())


# so2
@app.route('/data-so2', methods=['GET', 'POST'])
def data_so2():
    columns, values = data()
    # sitename=測站名稱
    sitename = [value[0] for value in values]
    so2 = [value[5] for value in values]
    return json.dumps({'sitename': sitename, 'so2': so2}, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
