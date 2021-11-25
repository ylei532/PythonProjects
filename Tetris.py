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




class TetrisGame():
    
    def __init__(self):
        self.grid = [["_" for i in range(MAXWIDTH)] for i in range(MAXHEIGHT)]
        self.loci = []
        self.game_over = False
    
    def UserInput(self):
        while True:
            x = input("hi")
            break
    
    def display_grid(self):
        for i in range(MAXWIDTH):
            print(" "+"_", end="")
        print('')
    
        for i in range(4, MAXHEIGHT):
            for j in range(MAXWIDTH):
                print('|'+self.grid[i][j], end="")
            print('|')

    def reset_grid(self):
        self.grid = [["_" for i in range(MAXWIDTH)] for i in range(MAXHEIGHT)]
        self.loci = []
        self.game_over = False        

    def insert_piece(self):
        self.loci.clear()
        for x, y in pieces[1]:
            while self.grid[x+4][y+3] != "_":
                x-=1
            if x+4 == 1:
                self.loci.append([x+4,y+3])
                self.grid[x+4][y+3] = "\033[4m0\033[0m"
                self.game_over = True
                break
            
            self.loci.append([x+4,y+3])
            self.grid[x+4][y+3] = "\033[4m0\033[0m"

    @staticmethod
    def StartGame(self):
        
        self.reset_grid()
        self.insert_piece()
        self.display_grid()

        while not self.game_over:
            
            next_piece = False
            
            while True:
                time.sleep(0.5)
                numpy_loci = np.array(self.loci)
                if max(numpy_loci[:,0]) == 23:
                    break
                
                for x,y in self.loci:
                    self.grid[x][y] = "_"
                    
                for x,y in self.loci:
                    if self.grid[x+1][y] != "_":                                            
                       for x,y in self.loci:
                           self.grid[x][y] = "\033[4m0\033[0m"
                       next_piece = True
                       break
                
                if next_piece:
                    next_piece = False
                    break
                        
                for i in range(len(self.loci)):
                    self.grid[self.loci[i][0]+1][self.loci[i][1]] = "\033[4m0\033[0m"
                    self.loci[i][0]+=1
                
                self.display_grid()

          
            self.insert_piece()
            self.display_grid()
            time.sleep(0.5)
         
          
def main():

    game = TetrisGame()
    
    thread = threading.Thread(target=TetrisGame.UserInput, args=[game])
    thread2 = threading.Thread(target=TetrisGame.StartGame, args=[game])
    thread.start()
    thread2.start()
    
    # game = TetrisGame()
    # game.start()
    
    # game.join()
    thread.join()
    thread2.join()
            
    # game = TetrisGame()
    # game.StartGame() 
    # y = [[0,0], [0,1], [2,2], [3,1]]
    # print(y[:,0:1])
if __name__ == "__main__":
    main()