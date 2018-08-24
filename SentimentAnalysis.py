def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()
    return newLex

def run(path):
    posLex=loadLexicon('positive-words.txt')
    words=[]
    SentAnalysis={}
    fin=open(path)
    for line in fin:
        wrd=set()
        words=(line.lower().strip().split(' '))
        for word in words:
            if word in posLex:
                wrd.add(word)
            wrdlist=list(wrd)
            #print(wrdlist)
        for word in wrdlist:
            if word in SentAnalysis:
                SentAnalysis[word]+=1
            else:
                SentAnalysis[word]=1
    return SentAnalysis
    fin.close()

print(run("textfile")) 



def count(path):
    dictt={}
    fin=open(path)
    for line in fin:
        words=line.lower().strip().split(' ')
        #print(words)
        for word in words:
            if word in dictt:
                dictt[word]+=1
            else:
                dictt[word]=1
    ddc=sorted(dictt.values())
    print (ddc)
    
count("textfile")