def run(path):
    senti={}
    posLex=set()
    lex_conn=open('positive-words.txt')
    for line in lex_conn:
        posLex.add(line.strip())
    lex_conn.close()
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        posList=set() #list of positive words in the review
        line=line.lower().strip()   
        words=line.split(' ') # slit on the space to get list of words
        for word in words: #for every word in the review
            if word in posLex: # if the word is in the positive lexicon
                posList.add(word) #update the positive list for this review
            my_list=list(posList)
            print(my_list)
        for word in my_list:
            if word in senti:
                senti[word] +=1
            else:   
                senti[word] = 1
    return senti        
    fin.close()
    
print (run('textfile'))

"""
if __name__ == "__main__": 
    reviews,decisions=run('textfile')
    for i in range(len(reviews)):
        print(reviews[i], decisions[i])
   """    





