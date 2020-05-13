def clean(file_name):
    with open(file_name) as json_file:
        lines = json_file.readlines()
        print(len(lines))
    basket = set()
    count = {}
    newlines = []
    for line in lines:
        if line.split(',')[0].split(':')[1] == '"Piersul"':
            break
        if line in basket:
            continue
        else:
            newlines.append(line)
            basket.add(line)
            tmp = line.split(',')[2]
            cnt = count.get(tmp, 0)+1
            count[tmp] = cnt
    del(lines)
    len(newlines)
    need = set()
    lines_ = []
    for key,val in count.items():
        if val>2:
            need.add(key)
    for line in newlines:
        if line.split(',')[2] in need:
            lines_.append(line)
    with open(file_name+'.csv','w') as file:
        for line in lines_:
            a = line.strip('{')
            a = a.strip('}')
            a = a.replace('"','')
            tmp = a.split(',')
            b = []
            b.append(tmp[2].split(":", 1)[1])
            b.append(tmp[0].split(":", 1)[1])
            b.append(tmp[1].split(":", 1)[1])
            b.append(tmp[3].split(":", 1)[1])
            b.append(tmp[4].split(":", 1)[1])
            b.append(tmp[5].split(":", 1)[1].split(" ")[0])
            b.append(tmp[5].split(":", 1)[1].split(" ")[1])
            res = ""
            for i in range(0, len(b)):
                if i<len(b)-1:
                    res = res + b[i] + ","
                else:
                    res = res + b[i]
            file.write(res)
            file.write('\n')