import numpy as np

MAXHEIGHT = 20
MAXWIDTH = 10


# a ="\033[4m0\033[0m"

pieces = [
         [[0,0], [0,1], [1,1], [1,2]], # Z
         [[0,0], [1,0], [2,0], [3,0]],  # straight line 
         [[0,1], [0,2], [1,0], [1,1]],  # inverted Z
         [[0,1], [1,0], [1,1], [1,2]],  # best piece
         [[0,0], [0,1], [1,0], [2,0]],  # inverted 7
         [[0,0], [0,1], [1,1], [2,1]],  #7
         [[0,0], [0,1], [1,1], [1,2]]   # square
         ]

class TetrisGame:
    
    def __init__(self):
        self.grid = [["_" for i in range(MAXWIDTH)] for i in range(MAXHEIGHT)]
        self.loci = []
        
    def display_grid(self):
        for i in range(MAXWIDTH):
            print(" "+"_", end="")
        print('')
    
        for i in range(MAXHEIGHT):
            for j in range(MAXWIDTH):
                print('|'+self.grid[i][j], end="")
            print('|')


    def insert_piece(self):
        self.loci.clear()
        for x, y in pieces[5]:
            self.loci.append([x,y+3])
            self.grid[x][y+3] = "\033[4m0\033[0m"

    def start(self):
        
        game_over = False
        self.display_grid()
        self.insert_piece()
        self.display_grid()

        while not game_over:
            
            numpy_loci = np.array(self.loci)
            if max(numpy_loci[:,0]) == 19:
                break
            
            for x, y in self.loci:
                self.grid[x][y] = "_"
            for i in range(len(self.loci)):
                self.grid[self.loci[i][0]+1][self.loci[i][1]] = "\033[4m0\033[0m"
                self.loci[i][0]+=1
            
            self.display_grid()
           
         

          
def main():            
    game = TetrisGame()
    game.start()


    
    
    # y = [[0,0], [0,1], [2,2], [3,1]]
    # print(y[:,0:1])
if __name__ == "__main__":
    main()