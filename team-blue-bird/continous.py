import os
import sys
import pandas as pd
import csv
from pyspark import SparkContext
from datetime import datetime
from itertools import groupby

def judgeContinous(date_strs):
    """
    Judge the continous day that one macid has
    """
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in date_strs]
    date_ints = set([d.toordinal() for d in dates])
    fun = lambda x: x[1] - x[0]
    lst = []
    for k, g in groupby(enumerate(sorted(date_ints)), fun):
        lst.append([v for i,v in g])
    print(lst)
    cnt = 0
    for i in lst:
        if len(i) >= 4:
            cnt += 1
    if cnt >= 1:
        return True
    else:
        return False

def task():
    """
    Calculate the continous days that one macid have, if one macid appears in the airport 
    more than 4 days continous, we will assert him/she has high possibility that belongs 
    to the employer list
    """
    # indir= "ndata/before_concat" #dir of input data

    sc= SparkContext('local[*]','task1')
    sc.setLogLevel("ERROR")

    # a,b,c=list(os.walk(indir))[0]
    # infiles = [os.path.join(a,f) for f in c]
    # rdd0=sc.textFile(infiles[0])

    lines0 = sc.textFile("instance.csv")
    # lines1 = sc.textFile(infiles[1])
    # lines2 = sc.textFile(infiles[2])
    # lines3 = sc.textFile(infiles[3])
    # lines4 = sc.textFile(infiles[4])
    # lines5 = sc.textFile(infiles[5])
    # lines6 = sc.textFile(infiles[6])

    # lines = lines0.union(lines1).union(lines2).union(lines3).union(lines4).union(lines5).union(lines6)

    
    q0 = lines0.map(lambda s:s.split(','))\
        .map(lambda s:(s[3],s[6]))\
        .groupByKey()\
        .map(lambda s:(s[0],sorted(list(set(s[1])))))\
        .collect()

    res = []
    for i in q0:
        if judgeContinous(i[1]):
            res.append(i[0])
    return res
    
    # print(rdd0.take(5))

if __name__=='__main__':
    a = task()
    with open("emplpyer_list_1st.csv","w") as f:
        for i in a:
            f.write(i+"\n")
