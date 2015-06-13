STM={}
iq=[]
fq=[]
n1000000000={}
n1000000001={}
n1000000002={}
n1000000003={}
n1000000004={}
n1000000005={}
n1000000006={}
n1000000007={}
n1000000008={}
n1000000009={}
n1000000010={}
n1000000011={}
n1000000012={}
n1000000013={}
n1000000014={}
n1000000015={}
n1000000016={}
n1000000017={}
n1000000018={}
n1000000019={}
n1000000020={}
n1000000021={}
n1000000022={}
n1000000023={}
n1000000024={}
n1000000025={}
n1000000026={}

LTMf = open('LT.mem','w')
#Number of nodes
LTMf.write('4\n')
#Input nodes
LTMf.write('n1000000001={"n2000000001": 0.8,"n2000000002": 0.6}\n')
LTMf.write('n1000000001={}\n')
LTMf.write('n1000000002={}\n')
LTMf.write('n1000000003={}\n')
LTMf.write('n1000000004={}\n')
LTMf.write('n1000000005={}\n')
LTMf.write('n1000000006={}\n')
LTMf.write('n1000000007={}\n')
LTMf.write('n1000000008={}\n')
#Memory nodes
LTMf.write('n2000000001={"n1000000002": 0.5}\n')
LTMf.write('n2000000002={"n1000000003": 0.3}\n')
LTMf.write('n2000000003={"n1000000003": 0.5}\n')
LTMf.write('n2000000004={"n1000000005": 0.3}\n')
LTMf.close()

#Load Long-term memory into node dictionaries

LTMf = open('LT.mem','r')
LTM = list(LTMf)

for line in range(len(LTM)):
    exec(LTM[line])
numNodes=eval(LTM[0][:-1])
del LTM[0]

#Input
    
rawInput=input('Say: ')

#Node activation

def fire(node):
    #list nodes receiving signal from node
    nodeAffs = list(eval(node).keys())
    
    #list nodes in STM
    stmNodes = list(STM.keys())

    #evolve synapses
    for n in range(len(stmNodes)):
        #Should nodes be able to connect to themselves??
        if (STM[stmNodes[n]]<0) & (stmNodes[n] != node):
            try:
                eval(stmNodes[n])[node]=(eval(stmNodes[n])[node]*9+1)/10
                
                #Strong connections develop into new node
                
                #ONLY IF IT'S NEW!!!!????
                
                if (eval(stmNodes[n])[node]>0.9) & (eval(stmNodes[n])[node]<1):
                    eval(stmNodes[n])[node]=1
                    print('new node!')
                    global numNodes
                    numNodes += 1
                    print(stmNodes[n]+'["n'+str(2000000000+numNodes)+'"]=0.3')
                    exec(stmNodes[n]+'["n'+str(2000000000+numNodes)+'"]=0.3',globals())  #Default connection value for new node
                    exec('n'+str(2000000000+numNodes)+'={}',globals())
                    exec('n'+str(2000000000+numNodes)+'["'+node+'"]=0.3')
            except KeyError:
                eval(stmNodes[n])[node]=0.1
    
    #send signals to afferent nodes    
    for aff in range(len(nodeAffs)):
        try:
            STM[nodeAffs[aff]]+=0.5*eval(node)[nodeAffs[aff]] #####change this depending on connection type
            if STM[nodeAffs[aff]]>1:
                global fq
                fq+=[nodeAffs[aff]]
        except KeyError:
            STM[nodeAffs[aff]]=0.5
    STM[node] = -0.5
    return

    try:
        print('before aff'+str(STM['n1000000003']))
    except KeyError:
        pass

    #intrinsic/emotional connections

#Create input queue, add to fire queue.

for i in range(len(rawInput)):
    rawInput=rawInput.upper()
    try:
        if rawInput[i]==':':
            if rawInput[i+1]==')':
                iq+=[':)']
                rawInput=rawInput[:i]+rawInput[i+2:]
            elif rawInput[i+1]=='(':
                iq+=[':(']
                rawInput=rawInput[:i]+rawInput[i+2:]
            else:
                iq+=rawInput[i]
        elif rawInput[i]==' ':
            iq+=[' ']
        else:
            if rawInput[i]=='A':
                iq+=['n1000000001']
            elif rawInput[i]=='B':
                iq+=['n1000000002']
            elif rawInput[i]=='C':
                iq+=['n1000000003']
            elif rawInput[i]=='D':
                iq+=['n1000000004']
            elif rawInput[i]=='E':
                iq+=['n1000000005']
            elif rawInput[i]=='F':
                iq+=['n1000000006']
            elif rawInput[i]=='G':
                iq+=['n1000000007']
            elif rawInput[i]=='H':
                iq+=['n1000000008']
            elif rawInput[i]=='I':
                iq+=['n1000000009']
            elif rawInput[i]=='J':
                iq+=['n1000000010']
            elif rawInput[i]=='K':
                iq+=['n1000000011']
            elif rawInput[i]=='L':
                iq+=['n1000000012']
            elif rawInput[i]=='M':
                iq+=['n1000000013']
            elif rawInput[i]=='N':
                iq+=['n1000000014']
            elif rawInput[i]=='O':
                iq+=['n1000000015']
            elif rawInput[i]=='P':
                iq+=['n1000000016']
            elif rawInput[i]=='Q':
                iq+=['n1000000017']
            elif rawInput[i]=='R':
                iq+=['n1000000018']
            elif rawInput[i]=='S':
                iq+=['n1000000019']
            elif rawInput[i]=='T':
                iq+=['n1000000020']
            elif rawInput[i]=='U':
                iq+=['n1000000021']
            elif rawInput[i]=='V':
                iq+=['n1000000022']
            elif rawInput[i]=='W':
                iq+=['n1000000023']
            elif rawInput[i]=='X':
                iq+=['n1000000024']
            elif rawInput[i]=='Y':
                iq+=['n1000000025']
            elif rawInput[i]=='Z':
                iq+=['n1000000026']
            else:
                print('unrecognized character')
    except IndexError:
        pass

#Cascade node fire queue

fq+=(iq[0],)
del iq[0]

while len(fq)>0:
    node = fq[0]
    if node == ' ':
        print('wait')
    elif node==':)':
        print('dope')
    elif node==':(':
        print('stress')

        #ADD A "CLEAR STM" CHARACTER
        
    else:
        print('Activate node '+node)
        exec('global '+node)
        fire(node)
    for j in range(len(list(STM.keys()))):
        try:
            
            #Decay the residual ion concentration
            
            STM[list(STM.keys())[j]]=STM[list(STM.keys())[j]]*0.9
            
            #Drop old memories from STM
            
            if abs(STM[list(STM.keys())[j]])<0.01:
                del STM[list(STM.keys())[j]]
        except IndexError:
            pass
    del fq[0]
    if len(iq)>0:
        fq+=(iq[0],)
        del iq[0]
LTMf.close()

#Save LTM to file

#Input nodes
LTMf=open('LT.mem','w')
LTMf.write(str(numNodes)+'\n')

nodeBase = 1000000001
for num in range(26):
    LTMf.write('n'+str(nodeBase+num)+'='+str(eval('n'+str(nodeBase+num)))+'\n')

#Memory nodes
nodeBase = 2000000001
for num in range(numNodes):
    exec('global n'+str(nodeBase+num))
    LTMf.write('n'+str(nodeBase+num)+'='+str(eval('n'+str(nodeBase+num)))+'\n')

LTMf.close()
