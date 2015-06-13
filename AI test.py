#This is Data's mind.

import thread
import math
import sys

conscious=True
STM=[]                          #Short-term memory - list of recent thoughts
thoughts=[]                     #Channel 0 is thought, Channel 1 is sense, Channel 2 is "sight"
emotions=[0.25, 0.0, 1.0, 0.0, 0.0, 0.0]
#EMOTIONS:
#    up to +1:  speak   self    confidence   understanding   good    future     overall mood = sum(emotions)?
#           0:  think   idea    -                            -       present
#  down to -1:  listen  user    confusion                    evil    past
incoming=''
word=''

#####FUNCTIONS

def expect(word):
    global emotions
    global STM
    expectation=0.0
    understanding=0.0
    thing=open(word,'r+')
    FLAs=eval(thing.read())
    for i in range(len(STM)):
        for j in range(len(FLAs)):
            if FLAs[j][1]==STM[i]:
                
        if word==STM[i][1]:
            expectation=STM[i][0]
    if expectation>1.0:
        
    thing.close()

def fire(thought):
    global emotions
    global STM
    thing=open(thought,'r+')
    associations=eval(thing.read())
    for i in range(len(associations)):
        if associations[i][1][0:4]=='abs_':
            #Emtional effects
        else:
            added=False
            for x in range(len(STM)):
                if associations[i][1]==STM[x][1] and #pot diff over crit:
                    STM[x][0]=STM[x][0]+#F'n of str? if over critical level?
                    if STM[x][0]>1:
                        associations[i][0]=associations[i][0]-STM[x][0]
                        newlink_node_file=open(STM[x][1],'r+')
                        newlink_node=eval(newlink_node_file.read())
                        for y in range(len(newlink_node):
                            before=newlink_node[y][0]
                            #add strength to link or make new one
                            #make a new node if this puts a link over critical strength
                        newlink_node_file.close()
                    added=True
            if not added:
                STM.append([SOME FUNCTION OF STR,associations[i][1]])
    thing.close()

def compress(concept_list)
    #Delete duplicates, add strengths together.
    for i in range(len(concept_list)):
        for j in range(len(concept_list)-1)
            if concept_list[j+1][1]=concept_list[i][1]:
                concept_list[i][0]=concept_list[i][0]+concept_list[j+1][0]
                del concept_list[j+1]
    return concept_list

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

#How to build speech????
#While urge to talk is high, choose utterable concepts to voice, then compile a list until 
def say(speech):
    str(raw_input(speech))

#####SETUP
#SLEEP MODE TOGGLE??? TURN OFF SENSE CHANNEL, RUN INTERNALLY
#####WAKE UP

user=str(raw_input('User name:'))

try:
    abstract_file=open('abstract','r+')
    abstract=eval((abstract_file.read())
except IOError:
    print('WARNING: Abstract file missing! Exiting.')
    pass

from datetime import datetime
log=[str(datetime.now())]

#GIVE access to log

try:
    user=str(raw_input('What is your name?'))
    incoming=str(raw_input('Start a conversation or leave blank to continue: '))
    words.append(incoming.split(' '))
    words=filter(None, words)
except SyntaxError:
    print('Syntax Error')
    pass

#####MAIN thought process

while conscious:
    if incoming:
        words.append(incoming.split(' '))
        words=filter(None, words)
    if words[0]:
        word=words[0]
        del words[0]    #Feed next word if any into thought channel
        thoughts[1]=recognize(word)
    try:
        if thoughts[1]:
            recognize(thoughts[1])
            expect(thoughts[1],emotions)
            fire(thoughts[1],STM,emotions)
        fire(thoughts[0])
        
    except KeyboardInterrupt:
        try:
            incoming=str(raw_input('Say:'))
            log.append(user,': ',incoming)
        except: SyntaxError
            pass
    for i in range(len(STM)-1):
        STM[i+1][0]=STM[i+1][0]*(0.75) #Decay rate in STM - Tweak experimentally
        if fabs(STM[i][0])<0.001:
            del STM[i]
    #PARE
    #decay emotions as well.

abstract_file.write(abstract)

logfile=open('log', 'a')
logfile.write(log)
logfile.close()
