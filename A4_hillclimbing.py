#use hibernate fn, use severe hillclimbing
import copy
import time
from collections import deque
open_stack=[]
closed_list=[]
class puzzle(object):
    def __init__(self,initial,goal):
        self.parent=None
        self.curr=initial
        self.empty=self.getemptyindex()
        self.goal=goal
    def getemptyindex(self):
        for i in range(0,9):
            if (self.curr[i]==0):
                return i
    def compare(self,p2):
        for i in range(0,9,1):
            if self.curr[i]!=p2.curr[i]:
                return False
        return True
    #this is used while checking the closed list
    def display_state(self):
        for i in range(0,9,3):
            print(self.curr[i],"\t",self.curr[i+1],"\t",self.curr[i+2])
        print("\n")
    def isgoalreached(self):
        for i in range(0,9,1):
            if (self.curr[i]!=self.goal[i]):
                return False
        return True
    def displaysolution(self):
        print("------SOLUTION------")

        while (self.parent!=None):
            self.display_state()
            self=self.parent
        self.display_state()

    def heuristic(self):
        count=0
        for i in range(3):
            for j in range(3):
                if self.curr[i]!=self.goal[i]:
                    count= count+1
        return count

        
    #actions
    #if has logic created for rules -- up,down,left and right here the (order)work on the empty spaces
    def up(self):
        if (self.empty-3>=0):
            
            self.curr[self.empty],self.curr[self.empty-3]=self.curr[self.empty-3],self.curr[self.empty]
            self.empty=self.empty-3
            if(self.isgoalreached()):
                print("Goal is reached")
            return True


        else:
            #print("Invalid Move")
            return False
        
    def down(self):
        if (self.empty+3<=8):
            self.curr[self.empty],self.curr[self.empty+3]=self.curr[self.empty+3],self.curr[self.empty]
            self.empty=self.empty+3
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            #print("Invalid Move")
            return False
    

    def left(self):
        if(self.empty%3!=0):
            self.curr[self.empty],self.curr[self.empty-1]=self.curr[self.empty-1],self.curr[self.empty]
            self.empty=self.empty-1
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            
            #print("Invalid Move")
            return False
        
    def right(self):
        if(self.empty%3!=2):
            self.curr[self.empty],self.curr[self.empty+1]=self.curr[self.empty+1],self.curr[self.empty]
            self.empty=self.empty+1
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            #print("Invalid Move")
            return False
def CheckClosedList(p1):
    for node in closed_list:
        if p1.compare(node):
            # print("INSIDE CLOSED")
            return True
        
    return False           
def hillclimbing(p1):
    
    open_stack.append(p1)
    startTime=time.time()

    while open_stack!=[]:
        current=open_stack.pop(0)#for bfs open_stack.pop(0)
        closed_list.append(current)
        #current.display_state()
        if(current.isgoalreached()):
            current.display_state()
            current.displaysolution()
            currentTime=time.time()
            print("Time is : ",currentTime- startTime )
            break
        newpuzzles=deque()    
        new_state=copy.deepcopy(current)
        if (new_state.up() and CheckClosedList(new_state)==False):
            newpuzzles.append(new_state)
            new_state.parent=current
            # new_state.display_state()
        else:
            del new_state
                
        new_state=copy.deepcopy(current)
        if (new_state.down() and CheckClosedList(new_state)==False):
            newpuzzles.append(new_state)
            new_state.parent=current
            # new_state.display_state()
        else:
            del new_state
            
        new_state=copy.deepcopy(current)
        if (new_state.left() and CheckClosedList(new_state)==False):
            newpuzzles.append(new_state)
            new_state.parent=current
            # new_state.display_state()
        else:
            del new_state
                
        new_state=copy.deepcopy(current)
        if (new_state.right() and CheckClosedList(new_state)==False):
            newpuzzles.append(new_state)
            new_state.parent=current
            # new_state.display_state()
        else:
            del new_state
        
        newpuzzles=deque(sorted(newpuzzles,key=lambda X: X.heuristic()))
        if not newpuzzles:
            print("Local maxima reached ")
            break
        
        open_stack.append(newpuzzles.popleft())

        
        
                
            



def main():
    #can be 1D or 2D Array
    initial=[2,8,1,0,4,3,7,6,5]
    goal=[1,2,3,8,0,4,7,6,5]
    open_stack=[]
    closed_list=[]
    p=puzzle(initial,goal)
    hillclimbing(p)
    #Testing all moves and constraints
    
main()
