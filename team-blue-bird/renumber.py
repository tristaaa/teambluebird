import os
import sys
import pandas as pd
import csv
import json
from pyspark import SparkContext
from datetime import datetime
from itertools import groupby
def renumber(s):
    """
    After we filter all of the employer and arrival passengers, we need to renumber all of the macid, since 
    we need to treat even if the same macid as the different person in differernt days, since he/she may 
    take the differernt flight and may go to the different destination, so after filtering we need to renumber 
    all of the macid
    """
    res = []
    for i in range(len(s[1])):
        for j in s[1][i]:
            res.append([s[0]+":"+str(i)]+j)
    return res

def task(arg):

    sc= SparkContext('local[*]','task1')
    sc.setLogLevel("ERROR")

    lines0 = sc.textFile(arg)
    
    q0 = lines0.map(lambda s:json.loads(s))\
        .filter(lambda s:len(s[1])>0)\
        .map(lambda s:(s[0],s[1]))\
        .flatMap(lambda s:renumber(s))\
        .map(lambda s:(s[5],s[4],s[0],s[2],s[3],str(s[1])))\
        .collect()
    # print(q0)
    return q0

if __name__=='__main__':
    arg = sys.argv
    output = arg[2]
    a = task(arg[1])
    with open(output,"w") as f:
        for i in a:
            f.write(",".join(i)+"\n")  