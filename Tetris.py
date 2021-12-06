import numpy as np
import time
import random
import threading

MAXHEIGHT = 24
MAXWIDTH = 10

pieces = [
         [[0,0], [0,1], [1,1], [1,2]], # Z
         [[0,0], [1,0], [2,0], [3,0]],  # straight line 
         [[0,1], [0,2], [1,0], [1,1]],  # inverted Z
         [[0,1], [1,0], [1,1], [1,2]],  # best piece
         [[0,0], [0,1], [1,0], [2,0]],  # inverted 7
         [[0,0], [0,1], [1,1], [2,1]],  #7
         [[0,0], [0,1], [1,0], [1,1]]   # square
         ]

pieces_1 = [
         [[-1,1], [0,1], [0,0], [1,0]], # Z
         [[0,-1], [0,0], [0,1], [0,2]],  # straight line 
         [[-1,1], [0,1], [0,2], [1,2]],  # inverted Z
         [[0,1], [1,1], [1,2], [2,1]],  # best piece
         [[1,-1], [1,0], [1,1], [2,1]],  # inverted 7
         [[1,0], [1,1], [1,2], [0,2]],  #7
         [[0,0], [0,1], [1,0], [1,1]]   # square
         ]

pieces_2 = [
         [[0,0], [0,1], [1,1], [1,2]], # Z
         [[0,0], [1,0], [2,0], [3,0]],  # straight line 
         [[0,1], [0,2], [1,0], [1,1]],  # inverted Z
         [[1,0], [1,1], [1,2], [2,1]],  # best piece
         [[0,0], [1,0], [2,0], [2,-1]],  # inverted 7
         [[0,1], [1,1], [2,1], [2,2]],  #7
         [[0,0], [0,1], [1,0], [1,1]]   # square
         ]

pieces_3 = [
         [[-1,1], [0,1], [0,0], [1,0]], # Z
         [[0,-1], [0,0], [0,1], [0,2]],  # straight line 
         [[-1,1], [0,1], [0,2], [1,2]],  # inverted Z
         [[0,1], [1,1], [1,0], [2,1]],  # best piece
         [[0,-1], [1,-1], [1,0], [1,1]],  # inverted 7
         [[1,0], [1,1], [1,2], [2,0]],  #7
         [[0,0], [0,1], [1,0], [1,1]]   # square
         ]

lock = threading.Lock()

class TetrisGame():
    
    def __init__(self):
        self.grid = [["_" for i in range(MAXWIDTH)] for i in range(MAXHEIGHT)]
        self.loci = []
        self.game_over = False
        self.rotation_loci = 0
        self.rotation_index = [pieces, pieces_1, pieces_2, pieces_3]
        self.piece = ""
   
    def CheckGame(self):
        lock.acquire()
        full_row = []
        count = 0
        
        for i in range(4, MAXHEIGHT):
            for j in range(MAXWIDTH):
                if self.grid[i][j] == "\033[4m0\033[0m":
                    count+=1
                else:
                    break
            
            if count == 10:              
                full_row.append(i)
                                          
            count = 0
               
        
        if full_row != []:
            new_full_row = np.array(full_row)
            
            for i in full_row:
                for j in range(MAXWIDTH):
                    self.grid[i][j] = '_'
            
            new_grid = np.array([[0 if self.grid[x][y] == "_" else 1 for y in range(len(self.grid[x][:]))] for x in range(len(self.grid))])            

            index = -1
           
            for i in range(len(full_row)):
                   
               new_grid[5:new_full_row[index]+1][:] = new_grid[4:new_full_row[index]][:]
               new_grid[4,:] = 0
               
               index-=1
               new_full_row[:]+=1

        
            new_grid = list(new_grid)
            self.grid = [["_" if new_grid[x][y] == 0 else "\033[4m0\033[0m" for y in range(len(new_grid[x][:]))] for x in range(len(new_grid))]
        
      
        lock.release()

    
    def UserInput(self):
        '''
        Handles user inputs
        '''
        no_space = False
        
        while True:
            if self.game_over == True:
                break
            x = input("")
            # move left
            if x.lower() == 'a':
                lock.acquire()
                array = np.array(self.loci)
                if min(array[:,1]) >= 1:
                    
                    for x, y in self.loci:
                        self.grid[x][y] = "_"
                        
                    new_loci = [[x, y-1] for x, y in array[:,:]]
                    
                    for x, y in new_loci:
                        if self.grid[x][y] != "_":
                            no_space = True
                            break
                   
                    if no_space:
                        for x, y in self.loci:
                            self.grid[x][y] = "\033[4m0\033[0m"
                        no_space = False
                        lock.release()
                        continue
                    
                    for x, y in self.loci:
                        self.grid[x][y] = "_"
                        
                    self.loci = new_loci
               
                    for x, y in self.loci:
                        self.grid[x][y] = "\033[4m0\033[0m"
                    self.display_grid()
                lock.release()
            
            # move right
            elif x.lower() == 'd':
                lock.acquire()
                array = np.array(self.loci)
                if max(array[:,1]) <= 8:
                    
                    for x, y in self.loci:
                        self.grid[x][y] = "_"
                        
                    new_loci = [[x, y+1] for x, y in array[:,:]]
                    
                    for x, y in new_loci:
                        if self.grid[x][y] != "_":
                            no_space = True
                            break
                   
                    if no_space:
                        for x, y in self.loci:
                            self.grid[x][y] = "\033[4m0\033[0m"
                        no_space = False
                        lock.release()
                        continue
                    
                    for x, y in self.loci:
                        self.grid[x][y] = "_"
                        
                    self.loci = new_loci
               
                    for x, y in self.loci:
                        self.grid[x][y] = "\033[4m0\033[0m"
                    self.display_grid()
                lock.release()

            # rotate piece
            elif x.lower() == 'w':
                lock.acquire()
                if self.rotation_loci == 3:
                    self.rotation_loci = 0
                else:
                    self.rotation_loci += 1
                    
                                  
                for x, y in self.loci:
                    self.grid[x][y] = '_'
                    
                new_loci = (np.array(self.loci) - np.array(self.rotation_index[3 if self.rotation_loci == 0 else self.rotation_loci-1][self.piece]) + np.array(self.rotation_index[self.rotation_loci][self.piece]))

                
                while max(new_loci[:,1]) > 9:
                    new_loci[:,1] = [x-1 for x in new_loci[:,1]]
                
                while max(new_loci[:,0]) > 23:
                    new_loci[:,1] = [x-1 for x in new_loci[:,0]]
                
                while min(new_loci[:,1]) < 0:
                    new_loci[:,1] = [x+1 for x in new_loci[:,1]]
                
                
                
                new_loci = list(new_loci)
                
                for x, y in new_loci:
                    if self.grid[x][y] != "_":
                        no_space = True
                        break
                   
                if no_space:
                    for x, y in self.loci:
                        self.grid[x][y] = "\033[4m0\033[0m"
                    
                    if self.rotation_loci == 0:
                        self.rotation_loci = 3
                    else:
                        self.rotation_loci -= 1
                    
                    no_space = False
                    lock.release()
                    continue
                    
                self.loci = new_loci
                
                for x, y in self.loci:
                    self.grid[x][y] = "\033[4m0\033[0m"
                self.display_grid()
                
                lock.release()
            
            # end game function
            elif x.lower() == 'f':
                self.game_over = True
                
                
            # quick move piece downwards
            elif x.lower() == "s":
                
                lock.acquire()
                for x, y in self.loci:
                    self.grid[x][y] = '_'

                
                self.display_grid()
                
                while True:
                    
                    if max(np.array(self.loci)[:,0]) == 23:
                        break

                    for x, y in self.loci:
                        if self.grid[x+1][y] == '\033[4m0\033[0m':
                            no_space = True
                            break
                    
                    if no_space:
                        no_space = False
                        break
                    else:                       
                        self.loci = [[x+1, y] for x, y in self.loci]
                    
                     
                
                for x, y in self.loci:
                    self.grid[x][y] = '\033[4m0\033[0m'
                self.display_grid()
                
                lock.release()
                
  
    def display_grid(self):
        '''
        Show the current status of the grid
        '''
        
        for i in range(MAXWIDTH):
            print(" "+"_", end="")
        print('')
    
        for i in range(4, MAXHEIGHT):
            for j in range(MAXWIDTH):
                print('|'+self.grid[i][j], end="")
            print('|')

    def reset_grid(self):
        '''
        Clears all items out of the grid by resetting instance variables
        '''
        self.grid = [["_" for i in range(MAXWIDTH)] for i in range(MAXHEIGHT)]
        self.loci = []
        self.game_over = False        

    def insert_piece(self):
        '''
        Handles the insertion of a piece into the tetris grid
        '''
        
        self.rotation_loci = 0
        self.loci.clear()
        
        self.piece = random.randint(0,6)
        
        for x, y in pieces[self.piece]:
            while self.grid[x+4][y+3] != "_":
                x-=1
            if x+4 == 1:
                self.loci.append([x+4,y+3])
                self.grid[x+4][y+3] = "\033[4m0\033[0m"
                self.game_over = True
                break
            
            self.loci.append([x+4,y+3])
            self.grid[x+4][y+3] = "\033[4m0\033[0m"

    def StartGame(self):
        '''
        Hangles tetris game logic
        '''
        
        self.reset_grid()
        self.insert_piece()
        self.display_grid()

        while not self.game_over:
            
            next_piece = False
            
            while True:
                
                if self.game_over == True: # check if user ends game
                    break
                
                self.display_grid()
                time.sleep(1)
                numpy_loci = np.array(self.loci)
                if max(numpy_loci[:,0]) == 23:
                    break
                
                if self.game_over == True: # check if user ends game
                    break
                
                
                for x,y in self.loci:
                    self.grid[x][y] = "_"
                
                if self.game_over == True: # check if user ends game
                    break    
                
                for x,y in self.loci:
                    if self.grid[x+1][y] != "_":                                            
                       for x,y in self.loci:
                           self.grid[x][y] = "\033[4m0\033[0m"
                       next_piece = True
                       break
                
                if self.game_over == True: # check if user ends game
                    break
                
                if next_piece:
                    next_piece = False
                    break
                
                for i in range(len(self.loci)):
                    self.grid[self.loci[i][0]+1][self.loci[i][1]] = "\033[4m0\033[0m"
                    self.loci[i][0]+=1
                
 
            if self.game_over == True: # check if user ends game
                break
            
            self.CheckGame()
            self.insert_piece()
            self.display_grid()
            time.sleep(1)    
          
def main():

    game = TetrisGame()
    
    thread1 = threading.Thread(target=TetrisGame.UserInput, args=[game])
    thread2 = threading.Thread(target=TetrisGame.StartGame, args=[game])
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
            
if __name__ == "__main__":
    main()