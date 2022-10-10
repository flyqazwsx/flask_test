import pandas as pd
import requests
import json
from pandas import json_normalize
from flask import Flask, render_template, request


url = requests.get(
    "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON")
text = url.text
data = json.loads(text)
dataset = data['cwbopendata']['dataset']['datasetInfo']
location = data['cwbopendata']['dataset']['location']
df = json_normalize(data['cwbopendata']['dataset']['location'])
df = df[df['locationName'] == '臺北市']
dfs = json_normalize(df['weatherElement'][0])


def update_time():
    global url, text, data, dataset
    date = dataset['update']
    return date


def get_countys():
    global url, text, data, dataset, location
    countys = []
    for i in location[0:22]:
        countys.append(i['locationName'])
    return countys


def get_weather(Refresh=False):
    global url, text, data, dataset
    county_11 = []
    county_1 = []
    county = request.form.get('select_county')

    # if county in df['locationName'][0]:
    #    dfs = json_normalize(df['weatherElement'][0])
    #    for idx, row in dfs.iterrows():
    #        a = json_normalize(row['time'])
    #        county_1.append(a.values.tolist())
    #    for value in county_1:
    #        for td in value:
    #            county_11.append(td)

    for idx, row in dfs.iterrows():
        a = json_normalize(row['time'])
        county_1.append(a.values.tolist())
    for value in county_1:
        for td in value:
            county_11.append(td)

    return county_11


def get_county(county):
    global url, text, data, dataset
    county_22 = []
    county_2 = []
    county = request.form.get('select_county')
    if county in df['locationName'][0]:
        dfs = json_normalize(df['weatherElement'][0])
    elif county in df['locationName'][1]:
        dfs = json_normalize(df['weatherElement'][1])
    elif county in df['locationName'][2]:
        dfs = json_normalize(df['weatherElement'][2])
    elif county in df['locationName'][3]:
        dfs = json_normalize(df['weatherElement'][3])
    elif county in df['locationName'][4]:
        dfs = json_normalize(df['weatherElement'][4])
    elif county in df['locationName'][5]:
        dfs = json_normalize(df['weatherElement'][5])
    elif county in df['locationName'][6]:
        dfs = json_normalize(df['weatherElement'][6])
    elif county in df['locationName'][7]:
        dfs = json_normalize(df['weatherElement'][7])
    elif county in df['locationName'][8]:
        dfs = json_normalize(df['weatherElement'][8])
    elif county in df['locationName'][9]:
        dfs = json_normalize(df['weatherElement'][9])
    elif county in df['locationName'][10]:
        dfs = json_normalize(df['weatherElement'][10])
    elif county in df['locationName'][11]:
        dfs = json_normalize(df['weatherElement'][11])
    elif county in df['locationName'][12]:
        dfs = json_normalize(df['weatherElement'][12])
    elif county in df['locationName'][13]:
        dfs = json_normalize(df['weatherElement'][13])
    elif county in df['locationName'][14]:
        dfs = json_normalize(df['weatherElement'][14])
    elif county in df['locationName'][15]:
        dfs = json_normalize(df['weatherElement'][15])
    elif county in df['locationName'][16]:
        dfs = json_normalize(df['weatherElement'][16])
    elif county in df['locationName'][17]:
        dfs = json_normalize(df['weatherElement'][17])
    elif county in df['locationName'][18]:
        dfs = json_normalize(df['weatherElement'][18])
    elif county in df['locationName'][19]:
        dfs = json_normalize(df['weatherElement'][19])
    elif county in df['locationName'][20]:
        dfs = json_normalize(df['weatherElement'][20])
    elif county in df['locationName'][21]:
        dfs = json_normalize(df['weatherElement'][21])
    for idx, row in dfs.iterrows():
        a = json_normalize(row['time'])
        county_2.append(a.values.tolist())
    for value in county_2:
        for td in value:
            county_22.append(td)


if __name__ == '__main__':

    print(get_weather())
