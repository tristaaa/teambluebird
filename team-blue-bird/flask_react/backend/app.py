from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import pickle
import numpy as np
import pandas as pd
import heapq

app = Flask(__name__)
CORS(app)
model = pickle.load(open('xgb_reg.pkl', 'rb'))

@app.route('/newPredict', methods=['GET', 'POST'])
def assgin_gate():
    content = request.json
    gates = ['C44', 'C45', 'C46', 'C47',
             'C48', 'C49', 'C50', 'C51', 'C52', 'C53',
             'C54', 'C55', 'C56', 'C57', 'C58', 'C59',
             'C60', 'C61', 'C62', 'C63', 'C64', 'C65',
             'C66', 'C67', 'C69']
    dummy = content
    print('dummy = ', dummy)
    convertInput(dummy)
    # dummy =  {'Date': '05/18/2020', 'rows': [{'Arrival': 'Lima', 'Schedule_Depart_Time': '5:00', 'flight_number': 'CA231'},
    #                                         {'Arrival': 'Miami', 'Schedule_Depart_Time': '12:00', 'flight_number': 'FF2341'}]}
    print('converted data = ', dummy)

    res = {}
    res['top5']={}
    res['gate_assign'] = []
    res['map']={}
    dummy['rows'] = sorted(dummy['rows'], key=lambda x:x['Schedule_Depart_Time'])
    date_helper = []
    gate_assign = []
    with open('dest2flyinghr.json', 'r') as file:
        dest2flyinghr = json.load(file)

    for row in dummy['rows']:
        test = []
        top5 = []
        for gate in gates:
            tmp=[]
            tmp.append(gate)
            tmp.append(row['Arrival'])
            tmp.append(dummy['Date'])
            tmp.append(row['Schedule_Depart_Time'])
            tmp.append(dest2flyinghr[row['Arrival']])
            test.append(tmp)
        set_gate = set()

        '''

        {'top5':{flight_No:[{'gate':, 'dest':, 'ScheduledDT':,'shopTime':},]},
        'gate_assign':[{'flight_No':, 'dest':, 'ScheduledDT', 'gate':}]
        '''

        for i in range(len(date_helper)-1, -1, -1):
            if date_diff(date_helper[i], row['Schedule_Depart_Time'])<=120:
                set_gate.add(gate_assign[i])
            else:
                break

        test = pd.DataFrame(test, columns=['Gate', 'Arrival', 'Date', 'Schedule_Depart_Time', 'Flying_Hours'])
        print(test)
        test = transformation(test)
        prediction = model.predict(test)
        gate_pred = []
        for i in range(0, len(prediction)):
            gate_pred.append([gates[i], prediction[i]])
        gate_pred = sorted(gate_pred, key=lambda x:x[1], reverse=True)
        for i in range(0,5):
            tmp_dict = {}
            tmp_dict['gate'] = gate_pred[i][0]
            tmp_dict['dest'] = row['Arrival']
            tmp_dict['ScheduledDT'] = row['Schedule_Depart_Time']
            tmp_dict['shopTime'] = str(gate_pred[i][1])
            top5.append(tmp_dict)

        for pre in gate_pred:
            if pre[0] in set_gate:
                continue
            else:
                date_helper.append(row['Schedule_Depart_Time'])
                gate_assign.append(pre[0])
                print(pre[0])
                break

        res['top5'][row['flight_number']] = top5
        tmp_assgin = {}
        tmp_assgin['flight_No'] = row['flight_number']
        tmp_assgin['dest'] = row['Arrival']
        tmp_assgin['ScheduledDT'] = row['Schedule_Depart_Time']
        tmp_assgin['gate'] = pre[0]
        res['gate_assign'].append(tmp_assgin)
        res['map'][pre[0]] = res['map'].get(pre[0], [])
        #{'map':{Gate:[{'flight number', 'dest', 'ScheduledDT'}]}}
        res['map'][pre[0]].append({'number':row['flight_number'], 'dest':row['Arrival'], 'ScheduledDT':row['Schedule_Depart_Time']})
    print('result = ', res)

    return res

@app.route('/predict',methods=['POST'])
def predict():
    test = []
    gates = ['C44', 'C45', 'C46', 'C47',
             'C48', 'C49', 'C50', 'C51', 'C52', 'C53',
             'C54', 'C55', 'C56', 'C57', 'C58', 'C59',
             'C60', 'C61', 'C62', 'C63', 'C64', 'C65',
             'C66', 'C67', 'C69']

    dummy = {'Date':'10/18/2019', 'rows':[{'Arrival':'Bogota', 'Schedule_Depart_Time':'5:25'},
                                          {'Arrival':'Bogota', 'Schedule_Depart_Time':'5:20'},
                                          {'Arrival':'Bogota', 'Schedule_Depart_Time':'5:10'},
                                          {'Arrival':'Bogota', 'Schedule_Depart_Time':'5:30'}]}
    
    for gate in gates:
        tmp=[]
        tmp.append(gate)
        # for x in request.form.values():
        for x in dummy:
            tmp.append(x)
        test.append(tmp)
    #['Gate','Arrival', 'Date', 'Schedule_Depart_Time', 'Flying_Hours', ]
    test = pd.DataFrame(test, columns=['Gate','Arrival', 'Date', 'Schedule_Depart_Time', 'Flying_Hours'])
    test = transformation(test)
    print("test data=", test)
    prediction = model.predict(test)

    output = round(prediction[0], 2)
    print(prediction)
    h = []
    for i in range(0, len(prediction)):
        heapq.heappush(h,(prediction[i], gates[i]))
    res = []
    for j in range(0,5):
        res.append(heapq.heappop(h)[1])
    print('result = ', res)
    return jsonify(res)
        # return render_template()
'''
result =  {
'top5': {
            'TT342': [
                        {'gate': 'C54', 'dest': 'Miami', 'ScheduledDT': '23:00', 'shopTime': '96.26887'}, 
                        {'gate': 'C60', 'dest': 'Miami', 'ScheduledDT': '23:00', 'shopTime': '95.82474'}, {'gate': 'C49', 'dest': 'Miami', 'ScheduledDT': '23:00', 'shopTime': '92.54008'}, {'gate': 'C62', 'dest': 'Miami', 'ScheduledDT': '23:00', 'shopTime': '90.91548'}, {'gate': 'C59', 'dest': 'Miami', 'ScheduledDT': '23:00', 'shopTime': '88.23476'}], 'RE342': [{'gate': 'C60', 'dest': 'Lima', 'ScheduledDT': '6:00', 'shopTime': '78.07'}, {'gate': 'C53', 'dest': 'Lima', 'ScheduledDT': '6:00', 'shopTime': '67.271576'}, {'gate': 'C55', 'dest': 'Lima', 'ScheduledDT': '6:00', 'shopTime': '65.58564'}, {'gate': 'C59', 'dest': 'Lima', 'ScheduledDT': '6:00', 'shopTime': '65.24095'}, {'gate': 'C46', 'dest': 'Lima', 'ScheduledDT': '6:00', 'shopTime': '64.90601'}]}, 'gate_assign': [{'flight_No': 'TT342', 'dest': 'Miami', 'ScheduledDT': '23:00', 'gate': 'C54'}, {'flight_No': 'RE342', 'dest': 'Lima', 'ScheduledDT': '6:00', 'gate': 'C60'}], 'map': {'C54': [{'flight number': 'TT342', 'dest': 'Miami', 'ScheduledDT': '23:00'}], 'C60': [{'flight number': 'RE342', 'dest': 'Lima', 'ScheduledDT': '6:00'}]}}
127.0.0.1 - - [09/May/2020 00:56:44]
'''

def transformation(test):
    # missing_values = ["n/a", "na", "--", "None", "nan"]
    # flight_shopping = pd.read_csv("flight_shopping_10_percent.csv", na_values=missing_values)
    # et_low = flight_shopping['sum(estimated_time)'].quantile(0.2)
    # et_high = flight_shopping['sum(estimated_time)'].quantile(0.75)
    # flight_shopping = flight_shopping[
    #     (flight_shopping['sum(estimated_time)'] < et_high) & (flight_shopping['sum(estimated_time)'] > et_low)]
    # train_x = flight_shopping[['Gate', 'Arrival', 'Date', 'Schedule_Depart_Time', 'Flying_Hours']]
    # train_x.Flying_Hours = train_x.Flying_Hours.fillna('0:0')
    # train_x.Flying_Hours = train_x.Flying_Hours.apply(fill_0)
    # train_x['train'] = 1
    # test['train'] = 0
    # combined = pd.concat([train_x, test])
    # print(combined.tail())
    # combined.Flying_Hours = train_x.Flying_Hours.apply(hour_convert)
    # combined.Schedule_Depart_Time = train_x.Schedule_Depart_Time.apply(hr_min)
    # combined.Schedule_Depart_Time = train_x.Schedule_Depart_Time.apply(hr_min)
    # combined['Date'] = pd.to_datetime(train_x['Date'], errors='coerce')
    # combined = aggregate_nmt(combined)
    # test_df = combined[combined['train'] == 0]
    # test_df.drop(["train"], axis=1, inplace=True)
    # return test_df
    missing_values = ["n/a", "na", "--", "None", "nan"]
    flight_shopping = pd.read_csv("flight_shopping_10_percent.csv", na_values=missing_values)
    et_low = flight_shopping['sum(estimated_time)'].quantile(0.2)
    et_high = flight_shopping['sum(estimated_time)'].quantile(0.75)
    flight_shopping = flight_shopping[
        (flight_shopping['sum(estimated_time)'] < et_high) & (flight_shopping['sum(estimated_time)'] > et_low)]
    train_x = flight_shopping[['Gate', 'Arrival', 'Date', 'Schedule_Depart_Time', 'Flying_Hours']]
    train_x.Flying_Hours = train_x.Flying_Hours.fillna('0:0')
    train_x.Flying_Hours = train_x.Flying_Hours.apply(fill_0)
    train_x.Flying_Hours = train_x.Flying_Hours.apply(hour_convert)
    train_x.Schedule_Depart_Time = train_x.Schedule_Depart_Time.apply(hr_min)
    train_x['train'] = 1
    test['train'] = 0
    test.Schedule_Depart_Time = test.Schedule_Depart_Time.apply(hour_convert)

    combined = pd.concat([train_x, test])
    combined['Date'] = pd.to_datetime(combined['Date'], errors='coerce')
    combined = aggregate_nmt(combined)
    test_df = combined[combined['train'] == 0]
    test_df.drop(["train"], axis=1, inplace=True)
    return test_df

def hour_convert(x):
    if type(x) == str:
        h, m = map(int, x.split(':'))
        return (h * 60 + m)
    else:
        print(type(x))
        print(x)
        return x

def date_diff(date1, date2):
    date1 = date1.split(':')
    date2 = date2.split(':')
    a = int(date2[0]) - int(date1[0])
    b = int(date2[1]) - int(date1[1])
    return a*60+b

def fill_0(x):
    if x == 0:
        x = 445.63260525617636

    return x


def hr_min(x):
    return x * 60

def sec_min(x):
    return x/60

def time_convert(x):
    h,m = map(int,x.split(':'))
    return (h*60+m)

def aggregate_nmt(train):
    train['year'] = train['Date'].dt.year
    train['weekofyear'] = train['Date'].dt.weekofyear
    train['month'] = train['Date'].dt.month
    train['dayofweek'] = train['Date'].dt.dayofweek

    train.loc[:, 'Date'] = pd.DatetimeIndex(train['Date']).astype(np.int64) * 1e-9

    train = pd.get_dummies(train, columns=['Gate', 'Arrival'])

    return train

def convertInput(inputJson):
    days = inputJson['Date'].split('-')
    newDate = days[1] + '/' + days[2] + '/' + days[0]
    inputJson['Date'] = newDate
    for row in inputJson['rows']:
        if(row['Schedule_Depart_Time'][0] != '0'):
            row['Schedule_Depart_Time'] = row['Schedule_Depart_Time'][:5]
        else:
            row['Schedule_Depart_Time'] = row['Schedule_Depart_Time'][1:5]

if __name__ == '__main__':
    app.run(port="5001")