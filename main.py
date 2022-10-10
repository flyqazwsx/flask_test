
from flask import Flask, render_template, request
import json
from date import get_date
from weather_forecast import update_time, get_countys, get_weather
app = Flask(__name__)


Refresh = False


@app.route('/')
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


if __name__ == '__main__':

    app.run(debug=True)
