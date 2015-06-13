find concept if in STM
If not, potential = 0
either way, add + or - potential from previous concept, whatever it was (0.75 standard?)



def makelink(A,B,signal):   #signal is excitatory (+1,2) or inhibitory (-1,-2)
    open A
    look for B
    otherwise create new link, add signal to str.
    add signal to str.

def makenode(A,B,abstract):
    write new file called 'a_'+abstract  #this number should easily go into the trillions
    link AB from A.
    link A (2) and B (1) from a_###
    B should already be a choice for A (makelink runs before this)
    if B is then expectd, then C happens, then add C to AB, also make AC. reinforce - keep AB --> C, delete AC.
    
def checklink()?

recognize word

build word

def findnext():
    #Choose next thought, or predict next node/few nodes/word

A in thought channel, B in sense channel (A was in sense channel, then thought about), D in image channel
STM:A,...
findnext(A)
if B...
if AB does not exist (how to tell?) should be primary prediction, should link to B
makenode(A,B)
if B, then reinforce?
if prediction is C, then add B as link from AC if confidence is high. if confidence is low, then negatively reinforce C from AC also
makelink(A,B)

reinforce
add 2 to most recent pattern, 1 to 2nd and 3rd? (or subtract)


A signals B
B's e-neg is changed depending on whether A's link is + or -.
A's link to B can be reinforced under certain conditions (what exactly? when?)

at end of program, delete all connections in active thoughts that are realy weak.
