import random
class NimGame:
  
    def __init__(self):
     
        while(True):
     
            num=random.randint(1000,1000000)
            n=num
            tot=0
            while(n>0):
                dig=n%10
                tot=tot+dig
                n=n//10
            if tot%3==0:
                break
        self.n = num

    def startState(self):
       
        return self.n

    def isEnd(self, state):
       
        return True if game.sum_up(state)%3 != 0 or state== -1 else False

    def utility(self, state, player):
       
        if game.sum_up(state)%3 != 0:
            if player == 1:
               
                return float('+inf')
            else:
               
                return float('-inf')
        if state == -1:
            if player == 1:
               
                return float('-inf')
            else:
                
                return float('+inf')


    def actions(self, state):
 
        ll=[]
        s=str(state)
        for elem in s:
           ll.append(elem)
        return ll
    def successor(self, state, action):
         s=str(state)
         t=s.replace(str(action), '',1)
         if t=='':
            state=-1
         else:
            state=int(t)
            
         
         return state
     
    
    def sum_up(self,state):
        n=state
        tot=0
        while(n>0):
            dig=n%10
            tot=tot+dig
            n=n//10
        return tot
            
   

def minimaxPolicy(game, state, player):
  
    def recurse(state, player):
      
        if game.isEnd(state) == True:
          
            return (game.utility(state, player), None)
        if (state, player) in cache:
            return cache[(state, player)]

    
        choices = [(recurse(game.successor(state, action), -1*player)[0], action) for action in game.actions(state)]
       
     
        if player == +1:
            val = max(choices)
        else:
            val = min(choices)
        cache[(state, player)] = val
        return val

   
    value, action = recurse(state, player)
    return (value, action)

cache = {}

if __name__ == "__main__":

        print("Welcome to Turn of Three Game.Choose a digit from given number such that sum of remaining digits are divisable by 3 ")
        while(True):
            ready=input("Let's Play!! \"Press n/N for exit or anything else for continue\" ")
            if ready=='N' or ready=='n':
                break
        
            game = NimGame()
            
            state = game.startState()
            turn=''
            while (turn not in ['i','c']):
                  print("Decide who will be the first player")
                  turn=input("Press c for computer or i for human to start the game:")
                
            
            if(turn=='c'):
                    while (game.sum_up(state)%3==0) and state!=-1:
                        
                        print ("current state is: ", state)
                       
                        val, act = minimaxPolicy(game, state, 1)
                        s=str(state)
                        t=s.replace(str(act), '',1)
                        if t=='':
                            state=-1
                        else:
                            state=int(t)
                       
                        print("computer has chosen digit : "+act)
                        print ("computer moves state to: ", state)
                        if game.sum_up(state)%3 != 0:
                           print ("Congrats!! You won!")
                           break
                        if state== -1:
                            print ("Alas!! You lost!")
                            break
                        action = -2
                        while (str(action) not in str(state)):
                            action = int(input("Choose a digit from: "+ str(state)+":"))
                        s=str(state)
                        t=s.replace(str(action), '',1)
                        if t=='':
                            state=-1
                        else:
                            state=int(t)
                            
                        
                        
                        if game.sum_up(state)%3 != 0:
                            print ("Alas!! You lost!")
                            break
                        if state== -1:
                            print ("Congrats!! You won!")
                            break
            elif(turn=='i'):
                while (game.sum_up(state)%3==0) and state!=-1:
                        action = -2
                        print ("current state is: ", state)
                        while (str(action) not in str(state)):
                            action = int(input("Choose a digit from: "+ str(state)+":"))
                        s=str(state)
                        t=s.replace(str(action), '',1)
                        if t=='':
                            state=-1
                        else:
                            state=int(t)
                            
                        
                        
                        if game.sum_up(state)%3 != 0:
                            print ("Alas!! You lost!")
                            break
                        if state== -1:
                            print ("Congrats!! You won!")
                            break
                        print ("current state is: ", state)
                        val, act = minimaxPolicy(game, state, 1)
                        s=str(state)
                        t=s.replace(str(act), '',1)
                        if t=='':
                            state=-1
                        else:
                            state=int(t)
                        if(state==-1):
                            print("computer has chosen digit : "+act)
                            print ("computer moves state to final state")
                        else:
                            print("computer has chosen digit : "+act)
                            print ("computer moves state to: ", state)
                            
                        if game.sum_up(state)%3 != 0:
                           print ("Congrats!! You won!")
                           break
                        if state== -1:
                            print ("Alas!! You lost!")
                            break
        print("Good Bye")
                   
               
               