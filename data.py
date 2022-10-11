import pandas as pd
import json

# Create your views here.
url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=CSV'
df = pd.read_csv(url).dropna()


def data():
    global df
    df1 = df['sitename	aqi	no2	publishtime pm2.5'.split()]

    return df1.columns.tolist(), df1.values.tolist()
