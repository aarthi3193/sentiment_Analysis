
def posneg(path):
    list=set()
    file=open(path)
    for line in file:
        words=line.lower().strip()
        list.add(words)
    return list

def senti(path):
    reviews=[]
    poslist=posneg("positive-words.txt")
    neglist=posneg("negative-words.txt")
    fin=open(path)
    for line in fin:
        lines=line.lower().strip()
        reviews.append(lines)
        words=lines.split(' ')
        pos=[]
        neg=[]
              
        for word in words:
            if word in poslist:
                pos.append(words)
            if word in neglist:
                neg.append(words)
        decision=0  
        if (len(pos)>len(neg)):
            decision=1
        if (len(pos)<len(neg)):
            decision=-1
        print (lines,decision)

senti("textfile")