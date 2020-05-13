
import sys
from pyspark import SparkContext
from datetime import datetime


def inPoly(aLat, aLon, pointList):
    '''
    Decide if the gelocation of one point is within the polygon 
    defined by a list of its boundary points

    :param aLat: double 
    :param aLon: double 
    :param pointList: list [(lat, lon)...] must be in clockwise/anticlockwise order
    '''
    iSum = 0
    n = len(pointList) 
    
    for i in range(n):
        pLat1,pLon1 = pointList[i]
        if(i == n - 1):
            pLat2,pLon2 = pointList[0]
        else:
            pLat2,pLon2 = pointList[i+1]
        if ((aLat >= pLat1) and (aLat < pLat2)) or ((aLat>=pLat2) and (aLat < pLat1)):
            if (abs(pLat1 - pLat2) > 0):
                pLon = pLon1 - ((pLon1 - pLon2) * (pLat1 - aLat)) / (pLat1 - pLat2);
                if(pLon < aLon):
                    iSum += 1
 
    return iSum % 2


def task(argv):
    # input file: renum*.csv
    # output file: fltdeparture*.csv
    infile, outfile = argv[1], argv[2]

    sc = SparkContext('local[*]','task1')
    sc.setLogLevel("ERROR")

    # geolocation of shopping zone boundaries in Piersul [(lat,lng),...]
    zone1=[(-22.816345, -43.242180),(-22.816408, -43.242248),(-22.816611, -43.241728),(-22.816554, -43.241821)]
    zone2=[(-22.816983, -43.241595),(-22.816761,-43.241934),(-22.816959, -43.242099),(-22.817186, -43.241753)]
    zone3=[(-22.816509,-43.242279),(-22.816475, -43.242334),(-22.816500, -43.242365),(-22.816546, -43.242292)]
    zone4=[(-22.818613, -43.243567),(-22.818672, -43.243619),(-22.818552, -43.243800),(-22.818495, -43.243750)]
    zone5=[(-22.818418, -43.243482),(-22.818206, -43.243460),(-22.818195, -43.243488),(-22.818339, -43.243615)]
    zones=[zone1,zone2,zone3,zone4,zone5]

    rdd = sc.textFile(infile)

    # generate the list of macid which has at least one record
    # within at least one shopping zone 
    fltdepart = rdd.map(lambda x: x.split(',')).filter(lambda x: x[1]=='Level 3').map(lambda x: (x[2],(float(x[3]),float(x[4]))))\
        .groupByKey().mapValues(lambda x: any([any([inPoly(lat,lng,zone) for lat,lng in x]) for zone in zones]))\
        .filter(lambda x: x[1]).keys().collect()

    # filter out some departure passengers who doesn't appear in the above list
    # and generate the new records file
    flt_result = rdd.map(lambda x: x.split(',')).filter(lambda x: x[1]=='Level 3').filter(lambda x: x[2] in fltdepart).collect()

    with open(outfile,'w') as outf:
        for i in flt_result:
            outf.write(','.join(i)+"\n")
            

if __name__ == '__main__':
    task(sys.argv)




