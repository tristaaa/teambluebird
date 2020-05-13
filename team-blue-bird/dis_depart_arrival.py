import csv
from pyspark import SparkContext
import os
import sys
import json
import pandas as pd
from datetime import datetime
from itertools import groupby 
from dateutil.parser import parse
from math import radians, cos, sin, asin, sqrt
 
def haversine(lat1, lon1, lat2, lon2): # Latitude 1, longitude 1, latitude 2, longitude 2 (decimal degree)
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
 
    # haversine
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 #The average radius of the earth in kilometers
    return c * r * 1000 #return unit is meter

def checkTime(i,distance_threshold):
    """
    calculate the nearby timestamp's differences is within 12 hours
    """
    res = []
    cnt = 1
    temp = []   
    temp.append([i[1][0]])
    for j in range(0,len(i[1])-1): 
        if (datetime.strptime(i[1][j+1][0],'%Y-%m-%d %H:%M:%S') - datetime.strptime(i[1][j][0],'%Y-%m-%d %H:%M:%S')).days*24*3600+(datetime.strptime(i[1][j+1][0],'%Y-%m-%d %H:%M:%S')-datetime.strptime(i[1][j][0],'%Y-%m-%d %H:%M:%S')).seconds < 12*3600:
            cnt += 1
            temp[-1].append(i[1][j+1])
        else:  
            if cnt < 3 and i[1][j] in temp[-1]:
                temp.remove(temp[-1])
            cnt = 1
            temp.append([i[1][j+1]])
    if cnt < 3:
        temp.remove(temp[-1])
    if len(temp) != 0:
        res=(i[0],temp)
        for i in temp[:]:
            if haversine(float(i[-1][1]),float(i[-1][2]),-22.815118, -43.244192) < distance_threshold:
                temp.remove(i)
        
    return res
def renumber(s):
    # print(s)
    res = []
    for i in range(len(s[1])):
        for j in s[1][i]:
            res.append((s[0]+":"+str(i),)+j)
    return res

def task():
    """
    After the mapreduce we leave all the macid that satisfied the 
    requirement that the time difference within 12 hours
    :param distance_threshold:Based on the geolocation on the google map, we choose two points to set up the threshold
                
                
    Conjunction point(T2-Piersul)
    22°48'54.4"S 43°14'39.1"W
    -22.815118, -43.244192

    T central:
    22°48'58.5"S 43°14'33.0"W
    -22.816261, -43.242490
    """
    indir= "ddata" #dir of input data

    sc= SparkContext('local[*]','task1')
    sc.setLogLevel("ERROR")

    a,b,c=list(os.walk(indir))[0]
    infiles = [os.path.join(a,f) for f in c]

    lines0 = sc.textFile(infiles[0])
    # lines1 = sc.textFile(infiles[1])
    # lines2 = sc.textFile(infiles[2])
    # lines3 = sc.textFile(infiles[3])
    # lines4 = sc.textFile(infiles[4])

    # lines = lines0.union(lines1).union(lines2).union(lines3).union(lines4)

    distance_threshold = haversine(-22.815118, -43.244192,-22.816261, -43.242490)

   
    q0 = lines0.map(lambda s:s.split(','))\
        .map(lambda s:(s[3],(s[6]+" "+s[7],s[4],s[5],s[2],s[0])))\
        .groupByKey()\
        .map(lambda s:[s[0],list(s[1])])\
        .sortBy(lambda s:(s[1][0]))\
        .map(lambda s:checkTime(s,distance_threshold))\
        .filter(lambda s:len(s)!=0)\
        .collect()

        # .flatMap(lambda s:renumber(s))\
        # .map(lambda s:(s[5],s[4],s[0],s[2],s[3],str(s[1])))\
        # .collect()
    return q0
        
if __name__=='__main__':
    a = task()
    with open("dis_depart_arrival.json","w") as f:
        # f.write("[")
        for i in range(len(a)):
            f.write(json.dumps(a[i])+"\n")
        



        
                


                
       


