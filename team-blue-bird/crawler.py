import os
import urllib2
from bs4 import BeautifulSoup
import requests
import json
import calendar
from datetime import timedelta, date

nametonumber = dict((v,k) for k,v in enumerate(calendar.month_abbr))

def request_(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:33.0) Gecko/20100101 Firefox/33.0')
    response = urllib2.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(the_page, features="html.parser")
    return soup

def get_info(relative_link):
    script_front_url = BASE_URL + urllib2.quote(relative_link)
    print(script_front_url)
    ### for test ###
    # script_front_url = 'https://www.airportia.com/flights/ad4261/rio_de_janeiro/campinas/2019-08-09/'
    try:
        soup = request_(script_front_url)
    except urllib2.HTTPError:
        print(script_front_url)
        print('/n')
        print('404')
        return None
    res = [None, None, None, None, None, None, None, None, None,]
    ###    terminal, gate, depature, destination, departure date, scheduled departure time, actual departure time
    ###     scheduled arrival time, actual arrival time
    # try:
    ### Terminal & Gate ###
    misc = soup.find("div", "flightInfo-misc")
    # print(misc.text.split('|')[0].split(' ')[1])
    if misc is not None:
        try:
            res[0] = misc.text.split('|')[0].split(' ')[1]
        except IndexError:
            print("no terminal")

        try:
            res[1] = misc.text.split('|')[1].split(' ')[2]
        except IndexError:
            print("no gate")

    ### Depature & Destination
    cityinfo = soup.find_all("div", "flightInfo-city hidden-xs")
    if cityinfo is not None:
        try:
            res[2] = cityinfo[0].text
        except IndexError:
            res[2] = None

        try:
            res[3] = cityinfo[1].text
        except IndexError:
            res[3] = None


    ### depature date ###
    date = soup.find("div", "flightInfo-date")
    if date is not None:
        try:
            date = date.text.split(':')[1]
            date_list = date.split(' ')
            tmp=""
            tmp = tmp + date_list[3] + "-"
            tmp = tmp + str(nametonumber[str(date_list[2].strip(','))]) + "-"
            tmp = tmp + date_list[1]
            res[4] = tmp
        except IndexError:
            res[4] = None

    ### depature time###
    #[<div class="flightInfo-dateTime">17:10</div>, <div class="flightInfo-dateTime">17:07</div>, <div class=
    # "flightInfo-dateTime">20:40</div>, <div class="flightInfo-dateTime">20:22</div>]

    # time = soup.find_all("div", "flightInfo-dateTime")
    block = soup.find_all("div", "flightInfo-schedule")
    if len(block) == 2:
        flag = 0
        for b in block:
            time = b.find_all("div", "flightInfo-dateTime")
            label = b.find_all("div", "flightInfo-dateLabel")
            for i in range(0,len(label)):
                if label[i].text == "Scheduled:":
                    print(time[i].text)
                    res[5+flag] = time[i].text
                if label[i].text == "Actual:":
                    res[6+flag] = time[i].text
            flag = 2



    # print res

    # # scheduled depature time
    # if time is not None:
    #     try:
    #         res.append(time[0].text)
    #     except IndexError:
    #         res.append(None)
    #     # actual depature time
    #     try:
    #         res.append(time[1].text)
    #     except IndexError:
    #         res.append(None)
    #
    #     ### arrival time###
    #     try:
    #         res.append(time[3].text)
    #     except IndexError:
    #         res.append(None)
    # else:
    #     res.append(None)
    #     res.append(None)
    #     res.append(None)
    ###flight duration ###
    duration = soup.find_all("div", "flightInfo-footerItem")
    if duration is not None:
        try:
            res[8] = duration[2].text.split(' ')[2]
        except IndexError:
            res[8] = None

    return res
    # print res
    # except AttributeError:
    #     print('something missing!!!')
    #     return None

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


if __name__ == '__main__':
    with open('flight_info00.csv','w') as file:

        start_date = date(2019, 8, 1)
        end_date = date(2020, 8, 3)
        res = []
        BASE_URL = 'https://www.airportia.com'
        for single_date in daterange(start_date, end_date):
            print(single_date)
            url = 'https://www.airportia.com/brazil/gale%C3%A3o-_-ant%C3%B4nio-carlos-jobim-' \
                  'international-airport/departures/'+str(single_date.strftime("%Y%m%d"))+'/0000/2359/'
            soup = request_(url)
            td = soup.find_all("td", "flightsTable-track")
            for row in td:
                relative_link = row.a.get('href')
                data = get_info(relative_link)
                if data is not None:
                    tmp = ""
                    for i in range(0, len(data)):
                        if i < len(data) - 1:
                            tmp = tmp + str(data[i]) + ","
                        else:
                            tmp = tmp + str(data[i])
                    file.write(tmp)
                    file.write('\n')

# <div class="flightInfo-date">Departure: 8 Aug, 2019</div>
