'''
Created on 27.01.2017

@author: GERHARDY
'''
import time
import thread
import sys


class StateMachine:
    
    StateList = [0, 0, 0, 0, 0, 0, 0, 0]
    
    def __init__(self):
        print "Startklar"
    
    def setOutput(self, BoardOut, setTime):
        print str(BoardOut) + " Out is set " + str(time.clock()) +"\n"
        self.StateList[BoardOut-1] = 2
        deltastart = time.clock()
        time.sleep(setTime)
        print str(BoardOut) + " Finished " + str(time.clock() - deltastart) +"\n"
        self.StateList[BoardOut-1] = 3
        #print "Out is set"
    
    def resetState(self):
        self.StateList = [0, 0, 0, 0, 0, 0, 0, 0]   
            
    def run(self, ParaList):
        
        AllOutsReady = False 
         
        for i in xrange(len(ParaList)):
            thread.start_new_thread(self.setOutput, (i+1, ParaList[i]))
            
        while AllOutsReady == False:
            if self.StateList[0] == 3 and self.StateList[1] == 3 and self.StateList[2] == 3 and self.StateList[3] == 3 and self.StateList[4] == 3 and self.StateList[5] == 3 and self.StateList[6] == 3 and self.StateList[7] == 3:
                AllOutsReady = True
                    
        print"Fertig\n"        
        
        self.resetState()
                 

if __name__=="__main__":
    print str(sys.argv[0]) + "\n"
    
    if(len(sys.argv))>1:
        print str(sys.argv[1]) + "\n"    
        if int(sys.argv[1]) > 0 and int(sys.argv[1]) < 7:
            x = int(sys.argv[1])
    else:
        x = input("Welche Konfig 1-6 ? ")    
        
    setPara = [1,2,3,4,5,6,7,8]
    m = StateMachine()
    
    if x == 1:
        setPara = [1,2,3,4,5,6,7,8]
    elif x == 2:
        setPara = [2,2,2,2,2,2,2,2]
    elif x == 3:
        setPara = [8,7,6,5,4,3,2,1]
    elif x == 4:
        setPara = [4,4,4,4,4,4,4,4]
    elif x == 5:
        setPara = [1,2,3,4,5,6,7,8]
    elif x == 6:
        setPara = [1,2,3,4,5,6,7,8]
    else:
        setPara = [0,0,0,0,0,0,0,0]
        print"Nicht gueltig"

    m.run(setPara)
    