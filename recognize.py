def recognize(word):
    try:
        thing=open('LTM/'+word,'r')
        #ACTIVATE associations of hearing word (including emotions).
        thing.close()
        return word
    except IOError:
        recognized=False
        if len(word)>4:
            segment1=word[0:len(word)-1]
            segment2=word[len(word)-1]
            try:
                thing=open('LTM/'+segment1,'r+')
                thing.close()
                recognized=True
            except IOError:
                segment1=word[0]
                segment2=word[1:]
                try:
                    thing=open('LTM/'+segment2,'r+')
                    thing.close()
                    recognized=True
                except IOError:
                    while not recognized:
                        segment1=segment1+segment2[0]
                        segment2=segment2[1:]
                        if len(segment2)<3:
                            recognized=True
                        try:
                            thing=open('LTM/'+segment1,'r+')
                            thing.close()
                            try:
                                thing=open('LTM/'+segment2,'r+')
                                thing.close()
                                recognized=True
                            except IOError:
                                recognize(segment2)
                                recognized=True
                        except IOError:
                            try:
                                thing=open('LTM/'+segment2,'r+')
                                thing.close()
                                recognize(segment1)
                                recognized=True
                            except IOError:
                                pass
                        if recognized:
                            i=len(segment2)
        if recognized:
            newword=segment1+segment2
            thing=open('LTM/'+newword,'w')
            wordassoc='[[1,'+segment1+'],[1,'+segment2+']]'
            thing.write(wordassoc)
            thing.close()
        else:
            wordassoc=[]
            thing=open('LTM/'+word,'w')
            for i in range(len(word)):
                wordassoc.append([1,word[i]])
            thing.write(str(wordassoc))
            thing.close()
        return newword
            
#incoming=str(raw_input('words: '))
incoming='I have a so deck decked jewel bejewel bejeweled lute love lovely absolute absolutely joke joking jokingly joked decking backing backed dunking fuck absofuckinglutely'
words=incoming.split(' ')
words=filter(None, words)
#do this outside function    
thing={}
while words:
    word=words[0]
    del words[0]
    #IF word starts with &, next two letters are command: if-elif instinctive communique
    recognize(word)
