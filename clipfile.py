pa="renum5.csv"
li=[]

with open(pa,'r') as f:
    line=f.readline()
    while line:
        li.append(line)
        line=f.readline()

with open("renum_test.csv",'w') as f:
    for i in li[:100000]:
        f.write(i)