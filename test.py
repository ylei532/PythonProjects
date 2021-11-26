import numpy as np
list1 = [[2,3], [2,4]]
array = np.array(list1)
list2 = [[y, x+1] for y, x in array[:,:]]
print(list2)

for i in range(5,0):
    print(i)