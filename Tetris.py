import numpy as np
import time
import random
import threading

MAXHEIGHT = 24
VISIBLEHEIGHT = 20
MAXWIDTH = 10

pieces = [
         [[0,0], [0,1], [1,1], [1,2]], # Z
         [[0,0], [1,0], [2,0], [3,0]],  # straight line 
         [[0,1], [0,2], [1,0], [1,1]],  # inverted Z
         [[0,1], [1,0], [1,1], [1,2]],  # best piece
         [[0,0], [0,1], [1,0], [2,0]],  # inverted 7
         [[0,0], [0,1], [1,1], [2,1]],  #7
         [[0,0], [0,1], [1,1], [1,2]]   # square
         ]


lock = threading.Lock()

class TetrisGame():
    
    def __init__(self):
        self.grid = [["_" for i in range(MAXWIDTH)] for i in range(MAXHEIGHT)]
        self.loci = []
        self.game_over = False
   
    def CheckGame(self):
        count = 0
        for i in range(4, MAXHEIGHT):
            for j in range(MAXWIDTH):
                if self.grid[i][j] == "\033[4m0\033[0m":
                    count+=1
                else:
                    break
            # if count == 10:
                
            #     for k in range(MAXWIDTH):
            #         self.grid[i][k] = "_"
                    
                
                
                
                
                
                        
            # count = 0
    
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
            
            elif x.lower() == 'f':
                self.game_over = True                
    
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
        
        self.loci.clear()
        for x, y in pieces[random.randint(0, 6)]:
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
                time.sleep(0.25)
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
                
                self.display_grid()
 
            if self.game_over == True: # check if user ends game
                break
            
            self.insert_piece()
            self.display_grid()
            
    
            time.sleep(0.25)    
          
def main():

    game = TetrisGame()
    
    thread1 = threading.Thread(target=TetrisGame.UserInput, args=[game])
    thread2 = threading.Thread(target=TetrisGame.StartGame, args=[game])
    thread1.start()
    thread2.start()
    
    # game = TetrisGame()
    # game.start()
    
    # game.join()
    thread1.join()
    thread2.join()
            
    # game = TetrisGame()
    # game.StartGame() 
    # y = [[0,0], [0,1], [2,2], [3,1]]
    # print(y[:,0:1])
if __name__ == "__main__":
    main()