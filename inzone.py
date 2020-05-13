import sys
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

zone1=[(-22.816345, -43.242180),(-22.816408, -43.242248),(-22.816611, -43.241728),(-22.816554, -43.241821)]
zone2=[(-22.816983, -43.241595),(-22.816761,-43.241934),(-22.816959, -43.242099),(-22.817186, -43.241753)]
zone3=[(-22.816509,-43.242279),(-22.816475, -43.242334),(-22.816500, -43.242365),(-22.816546, -43.242292)]
zone4=[(-22.818613, -43.243567),(-22.818672, -43.243619),(-22.818552, -43.243800),(-22.818495, -43.243750)]
zone5=[(-22.818418, -43.243482),(-22.818206, -43.243460),(-22.818195, -43.243488),(-22.818339, -43.243615)]
zones=[zone1,zone2,zone3,zone4,zone5]

# from standard input
# point, zone id
argv = sys.argv
lat,lng,zoneid = float(argv[2].strip(",")),float(argv[3]),int(argv[1])
print(lat,lng,zoneid)
isin = inPoly(lat,lng,zones[zoneid-1])
print("the point is in zone",zoneid,"or not:",isin)


