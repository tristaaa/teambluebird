import os
import sys
import csv
from pyspark import SparkContext

def task():

    """  Since we get the continous day for one macid, we need to double check that one macid should at 
    least appear in the airport more than 40 days, if he/she satisfied both continous day and total frequency, 
    we can assert him/she can be a depearture passenger."""
    
    indir= "ddata" #dir of input data

    sc= SparkContext('local[*]','task1')
    sc.setLogLevel("ERROR")

    a,b,c=list(os.walk(indir))[0]
    infiles = [os.path.join(a,f) for f in c]

    lines0 = sc.textFile(infiles[0])
    lines1 = sc.textFile(infiles[1])
    lines2 = sc.textFile(infiles[2])
    lines3 = sc.textFile(infiles[3])
    lines4 = sc.textFile(infiles[4])
    lines5 = sc.textFile(infiles[5])

    lines = lines0.union(lines1).union(lines2).union(lines3).union(lines4).union(lines5)


    q0 = lines.map(lambda s:s.split(','))\
        .map(lambda s:(s[3],s[6]))\
        .groupByKey()\
        .map(lambda s:(s[0],len(set(s[1]))))\
        .sortBy(lambda s:s[1],ascending=False)\
        .take(1000)
    # print(q0)

    return q0

if __name__=='__main__':
    a = task()
    with open("frequency_lst.csv","w") as f:
        for i in a:
            f.write(i[0]+","+str(i[1])+"\n")
        
