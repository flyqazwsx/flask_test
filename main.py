
from flask import Flask, render_template, request
import json
from date import get_date
from data import data
from pm25 import get_pm25
from weather_forecast import update_time, get_countys, get_weather

app = Flask(__name__)


Refresh = False


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


@app.route('/data')
def data_s():
    columns, values = data()
    date = values[0][3]
    return render_template('./data.html', **locals())


@app.route('/data-no2', methods=['GET', 'POST'])
def data_no2():
    columns, values = data()
    # sitename=測站名稱
    sitename = [value[0] for value in values]
    no2 = [value[2] for value in values]
    aqi = [value[1] for value in values]
    pm25 = [value[4] for value in values]
    return json.dumps({'aqi': aqi, 'sitename': sitename, 'no2': no2, 'pm25': pm25}, ensure_ascii=False)


@app.route('/data_2')
def data_2():
    columns, values = data()
    date = values[0][3]
    return render_template('./pm25.html', **locals())


@app.route('/data-pm25', methods=['GET', 'POST'])
def data_pm25():
    columns, values = data()
    # sitename=測站名稱
    sitename = [value[0] for value in values]
    pm25 = [value[4] for value in values]
    return json.dumps({'sitename': sitename, 'pm25': pm25}, ensure_ascii=False)


@app.route("/pm25_charts")
def pm25():

    return render_template('./pm25_charts.html')


@app.route("/pm25-json", methods=['GET', 'POST'])
def pm25_json():
    columns, values = get_pm25()
    site = [value[1] for value in values]
    pm25 = [value[2] for value in values]
    date = values[0][-1]

    return json.dumps({'site': site, 'pm25': pm25}, ensure_ascii=False)


if __name__ == '__main__':
    pm25_json()
    app.run(debug=True)
