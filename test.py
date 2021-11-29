import numpy as np
import random
pieces = [
         [[0,0], [0,1], [1,1], [1,2]], # Z
         [[0,0], [1,0], [2,0], [3,0]],  # straight line 
         [[0,1], [0,2], [1,0], [1,1]],  # inverted Z
         [[0,1], [1,0], [1,1], [1,2]],  # best piece
         [[0,0], [0,1], [1,0], [2,0]],  # inverted 7
         [[0,0], [0,1], [1,1], [2,1]],  #7
         [[0,0], [0,1], [1,1], [1,2]]   # square
         ]

x = np.array(pieces[0])
x1 = np.array(pieces[1])

x = 3

while True:
    if x == 2:
        break
    
    x = random.randint(0,6)
    print(x)