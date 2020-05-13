
import sys
from pyspark import SparkContext
from datetime import datetime
from math import radians, cos, sin, asin, sqrt

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

def haversine(lat1, lon1, lat2, lon2): 
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
 
    # haversine公式
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 
    return c * r * 1000 #return unit is meter

def inSegment(p,line1,line2):
    """ check if the point p is on the line"""
    if line1[0][0] == line1[1][0]:# line1 is vertical
        if  p[1] > min(line1[0][1],line1[1][1]) and p[1] < max(line1[0][1],line1[1][1]):
            if p[0] >= min(line2[0][0],line2[1][0]) and p[0] <= max(line2[0][0],line2[1][0]):
                return True
    elif line1[0][1] == line1[1][1]:# line1 is horizontal
        if p[0] > min(line1[0][0],line1[1][0]) and p[0] < max(line1[0][0],line1[1][0]):
            if p[1] >= min(line2[0][1],line2[1][1]) and p[1] <= max(line2[0][1],line2[1][1]):
                return True
    else:
        if p[0] > min(line1[0][0],line1[1][0])-1e-6 and p[0] < max(line1[0][0],line1[1][0])+1e-6:
            if p[1] >= min(line2[0][1],line2[1][1]) and p[1] <= max(line2[0][1],line2[1][1])+1e-6 and p[0] >= min(line2[0][0],line2[1][0]) and p[0] <= max(line2[0][0],line2[1][0])+1e-6:
                return True
    return False

def getIntersection(ps,pe,bs,be):
    """return the intersection point(lat,lng) of two paths, line p and line b"""
    xp,xb,yp,yb=ps[1]-pe[1],bs[1]-be[1],ps[0]-pe[0],bs[0]-be[0]
    denominator = xp*yb - yp*xb
    if denominator==0.0: return (0,0)
    p,b = ps[1]*pe[0] - ps[0]*pe[1], bs[1]*be[0] - bs[0]*be[1]
    intersectionx = (p*xb - b*xp)/denominator
    intersectiony = (p*yb - b*yp)/denominator

    if inSegment((intersectiony,intersectionx),(ps,pe),(bs,be)):
        return (intersectiony,intersectionx)
    else: 
        return (0,0)

def calculateTimeIncre(zone,xi,xii,timedelta):
    percent,incre=0.0,0
    for bs,be in zip(zone,zone[1:]+[zone[0]]):
        ipoint = getIntersection((xi[0],xi[1]),(xii[0],xii[1]),bs,be)
        if not any(ipoint): continue
        else: 
            curpercent = haversine(ipoint[0],ipoint[1],xii[0],xii[1])/haversine(xi[0],xi[1],xii[0],xii[1])
            if curpercent<1e-3 :continue
            else: percent=curpercent
    if percent==0.0:
        if timedelta.seconds<240:percent=1
        else: percent = 240/timedelta.seconds
    incre=round(timedelta.seconds*percent)
    if incre<60: incre = timedelta.seconds
    return incre
    

def calculatetst(x,zones):
    alltst=0
    x=list(x)
    
    # passengers need to have at least 3 records to compute the total shopping time
    if len(x)<3: return 0

    for zone in zones:
        li = [(inPoly(lat,lng,zone), datetime.strptime(t,"%Y-%m-%d %H:%M:%S")) for lat,lng,t in x]
        # if the passenger didn't even appear in the zone, try next zone
        if not any(map(lambda x:x[0],li)): continue

        flag=0
        zipli = list(zip(li[1:],li))
        for i in range(len(zipli)):
            inout, timedelta = zipli[i][0][0]-zipli[i][1][0], zipli[i][0][1]-zipli[i][1][1]
            if inout==1: # passenger enters into the shopping zone
                incre = calculateTimeIncre(zone,x[i],x[i+1],timedelta)
                alltst+=incre
                flag=1
            elif (inout==0 and flag) or (inout==0 and not flag and zipli[i][0][0]): # passenger stays in the shopping zone
                alltst+=timedelta.seconds
            elif inout==-1: # passenger goes out of the shopping zone
                incre = calculateTimeIncre(zone,x[i],x[i+1],timedelta)
                alltst+=incre
                flag=0
    return alltst


def task(argv):
    # input file: renum*.csv
    # output file: tst*.csv
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

    # calculate the total shopping time for each passenger
    # and sum up the total shopping time in each shopping zone for each passenger  

    # we also output the passengers whose total shopping time is zero to give us a general view of 
    # how many passengers are in one flight rather than how many passengers who have shopped are
    # in each flight
    result = rdd.map(lambda x: x.split(',')).map(lambda x: (x[2],(float(x[3]),float(x[4]),x[5])))\
        .groupByKey().mapValues(lambda x: calculatetst(x,zones))\
        .mapValues(lambda x:str(x)).collect()

    with open(outfile,'w') as outf:
        for i in result:
            outf.write(','.join(i)+"\n")
            

if __name__ == '__main__':
    task(sys.argv)

