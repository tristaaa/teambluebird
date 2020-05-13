

import json
def convertInput(inputJson):
    days = inputJson['Date'].split('-')
    newDate = days[1] + '/' + days[2] + '/' + days[0]
    inputJson['Date'] = newDate
    for row in inputJson['rows']:
        if(row['Schedule_Depart_Time'][0] != '0'):
            row['Schedule_Depart_Time'] = row['Schedule_Depart_Time'][:5]
        else:
            row['Schedule_Depart_Time'] = row['Schedule_Depart_Time'][1:5]
    

if __name__ == "__main__":
    dummy = {'Date':'2020-05-27', 'rows':[{'Arrival':'Bogota', 'Schedule_Depart_Time':'05:25:00'},
        {'Arrival':'Bogota', 'Schedule_Depart_Time':'15:20:00'},
        {'Arrival':'Bogota', 'Schedule_Depart_Time':'15:10:00'},
        {'Arrival':'Bogota', 'Schedule_Depart_Time':'15:30:00'}]}
    convertInput(dummy)
    print('data = ', dummy)