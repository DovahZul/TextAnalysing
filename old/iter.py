import re


def getCountWords(text):
    #Убирает лишние символы и сдвигает индексы соответственно
    def temp(tp):
        r = re.finditer('\w+',tp[2])
        s = next(r)
        return (tp[0]+s.start(0), tp[0]+s.start(0)+(s.end(0)-s.start(0)), s.group(0))

    tmp ={}
    for m in re.finditer('[\W|\s]?(\w+)[\W|\s]?', text):
        w = temp((m.start(0), m.end(0), m.group(0)))
        if w[2] in tmp.keys():
            tmp[w[2]].append((w[0],w[1]))
        else:
            tmp[w[2]]=[(w[0],w[1])]

    return {k:len(x) for k,x in tmp.items()}

def getWordsFromString2(text):
    #Убирает лишние символы и сдвигает индексы соответственно
    def temp(tp):
        r = re.finditer('\w+',tp[2])
        s = next(r)
        return (tp[0]+s.start(0), tp[0]+s.start(0)+(s.end(0)-s.start(0)), s.group(0))

    tmp ={}
    list = []
    for m in re.finditer('[\W|\s]?(\w+)[\W|\s]?', text):
        list.append(m)
    return list

print("Hello World")
print(getCountWords("ПРИВЕт ыва...собака собака.  Собака"))
#print(getWordsFromString2("ПРИВЕт ыва...собака собака.  Собака"))