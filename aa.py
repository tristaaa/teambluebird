li,la=[],[]
pa="new4.csv"
c,mid=0,4390314
with open(pa,'r') as f:
    line=f.readline()
    while line:
        if c<mid:li.append(line)
        else:la.append(line)
        line=f.readline()
        c+=1

with open("new40.csv",'w') as f:
    for i in li:
        f.write(i)
with open("new5.csv",'w') as f:
    for i in la:
        f.write(i)
