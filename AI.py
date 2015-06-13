#This is Data's mind.

#Updated for Python 3.4.3 8/6/2015

#import thread - ????
import math
import sys
import os

conscious=True
STM=[]                          #Short-term memory - list of nodes w/ resid. potentials above or below baseline due to recent activity
thoughts=[[],[],[]]             #Channel 0 is thought, Channel 1 is sense, Channel 2 is "sight"
emotions=[0.0, 0.0, 0.0, 0.0, 0.0]
#Rewrite these... these have changed, see notes

#####FUNCTIONS        

def sense(node):
    global emotions
    global STM
    if node[0]=='&':
        #ignore??
        FLA=[]
    else:    
        thing=open('LTM/'+node,'r+')
        FLA=exec(thing.read())
    learn=[]
    excite=[]
    z=0.0 #expected "reward"
    k=0.0 #implied "reward"
    xn=[] #expected precursor(s)
    xp=[] #expected follower(s)
    yn=[] #present precursor(s)
    yp=[] #present follower(s)
    XN=0.0
    XP=0.0 #understanding
    YN=0.0
    YP=0.0 #relatedness
    for i in range(len(STM)):
        if STM[i][1]=='&:)':
            z=z+STM[i][0]
        if STM[i][1]=='&:(':
            z=z+STM[i][0]*0.5
        if STM[i][1]==node:
            h=STM[i][0]
        else:
            h=0.0 #node expectation
    for i in range(len(FLA)):
        if node==':)':
            k=k+1
        elif node--':(':
            k=k-0.5
        else:
            if FLA[i][0]<0.0:
                xn.insert(0,FLA[i][0])
                for j in range(len(STM)):
                    if STM[j][1]==FLA[i][1]:
                        yn.insert(0,STM[j][0])
                    else:
                        yn.insert(0,0.0)
            elif FLA[i][0]>=1.0:
                xp.insert(0,FLA[i][0])
                for j in range(len(STM)):
                    if STM[j][1]==FLA[i][1]:
                        yp.insert(0,STM[j][0])
                    else:
                        yp.insert(0,0.0)
    xn_sorted=sorted(xn,reverse=False)
    xp_sorted=sorted(xp,reverse=True)
    for i in range(len(xn)):
        XN=XN-0.3*xn[i]/xn_sorted[0]
        YN=YN+yn[i]
    for i in range(len(xp)):
        XP=XP+0.5*xp[i]/xp.sorted[0]
        YP=YP+yp[i]
    if h<0.0:
        laugh(abs(h)*XP*(YN/XN))
    reinforce(node,abs(h)*(1.0-1.0/(1.0+XP))*(YN/XN))
    emotions[1]=emotions[1]+0.05*YN/XN
    emotions[2]=emotions[2]+0.05*(1.0-1.0/(1.0+XP))
    if z*k>0.0:
        reinforce(node,(k-z)*(1.0-1.0/(1.0+XP))*(YN/XN))
    STM.append([-0.2,node])
    thing.write(FLA)
    thing.close()
    STM=compress(STM)

def think(node):
    global emotions
    global STM
    thing=open('LTM/'+node,'r+')
    FLA=exec(thing.read())

def reinforce(node,strength):
    global STM
    STM=compress(STM)
    thing=open(node,'r+')
    FLA=exec(thing.read())
    for i in range(len(STM)):
        if abs(STM[i][0])>0.1:
            FLA.append([strength*STM[i][0],STM[i][1]])
            rthing=open(STM[i][1],'r+')
            rFLA=exec(rthing.read())
            rFLA.append([-strength*STM[i][0],node])
            compress(rFLA)
            #if STM[i][1][0]=='&':
                #HANDLE THESE BETTER. 
            rthing.write(rFLA)
            rthing.close()
    compress(FLA)
    thing.write(FLA)
    thing.close()

def compress(concept_list):
    #Delete duplicates, add strengths together.
    for i in range(len(concept_list)):
        for j in range(len(concept_list)-1):
            if concept_list[j+1][1]==concept_list[i][1]:
                concept_list[i][0]=concept_list[i][0]+concept_list[j+1][0]
                del concept_list[j+1]
    concept_list=concept_list.sort()
    return concept_list

def recognize(word):
    #Recall a word if it is known or recognize pieces, create a new word if unknown
    try:
        thing=open('LTM/'+word,'r')
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
            wordassoc='[[-0.5,'+"'"+segment1+"'"+'],[-1.0,'+"'"+segment2+"'"+']]'
            thing.write(wordassoc)
            thing.close()
        else:
            wordassoc=[]
            thing=open('LTM/'+word,'w')
            thing.write([]) #associate with confusion?? New words should be attractive but also confusing
            thing.close()
        return newword

def forget(STM):
    #Decay STM prominence and decay node associations if removed from STM
    for i in range(len(STM)):
        STM[i][0]=STM[i][0]*(0.9) #Tweak this number experimentally
        if abs(STM[i][0])<0.001:
            try:
                node=open('LTM/'+STM[i][1],'r+')
                FLAs=exec(thing.read())
                strength=0.0
                for j in range(len(FLAs)):
                    if FLAs[j][0]<1.0:
                        del FLAs[j]
                    FLAs[j][0]=FLAs[j][0]*0.99
                    strength=strength+FLAs[j][0]
                if strength<1.0:
                    thing.close()
                    os.remove('LTM/'+STM[i][1])
                else:
                    thing.write(FLAs)
                    thing.close()
            except IOError:
                print('Error - Node file referenced in STM missing. This is supposed to be impossible!')
                pass
            del STM[i]

#How to build speech????
#If urge to speak is high, and concept is utterable, then print it to screen?
#Create something to represent pathway to motor cortex associated with each word? letter?

def makenode(A,B):
    global abstract
    thing.open('abs_'+abstract,'w')
    thing.write([[2, A],[1,B]])
    thing.close()
    abstract=abstract+1
    
#####SETUP
#SLEEP MODE TOGGLE??? TURN OFF SENSE CHANNEL, RUN INTERNALLY
#####WAKE UP

try:
    abstract_file=open('abstract','r+')
    abstract=exec((abstract_file.read()))
except IOError:
    print('WARNING: Abstract file missing! Exiting.')
    pass

from datetime import datetime
log=[str(datetime.now())]

#GIVE access to log

words=[]
try:
    user=str(input('What is your name?'))
    incoming=str(input('Start a conversation or leave blank to continue: '))
    log.append(user+': '+incoming)
    words.extend(incoming.split(' '))
    words=list(filter(None, words))
except SyntaxError:
    print('Syntax Error')
    pass

#####MAIN thought process

while conscious:
    #If user present, associate new nodes with user
    if len(words)>0:
        thoughts[1]=recognize(words[0])
        del words[0]
    try:
        if thoughts[1]:
            print(thoughts[1])
            sense(thoughts[1]) #~signal sent to thalamus, emotional response(s) to information
        print(thoughts[0])
        think(thoughts[0]) #next thought "chosen" in cortex
    except KeyboardInterrupt:
        try:
            incoming=str(raw_input('Say:'))
            log.append(user+': '+incoming)
            words.extend(incoming.split(' '))
            words=filter(None, words)
        except SyntaxError:
            pass
    forget(STM)
    #decay emotions each iteration as well.

abstract_file.write(abstract)
abstract_file.close()

logfile=open('log', 'a')
logfile.write(log)
logfile.close()
