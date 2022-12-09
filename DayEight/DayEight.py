import numpy as np

with open('DayEight/input.txt', 'r') as f:
    lines = f.readlines()
    
    trees = np.array([[int(length) for length in line.strip()] for line in lines])
    shape = np.zeros(trees.shape)
    size = trees.shape[0]
    scenic = []
    for i in range(1, size-1):
        for j in range(1, size-1):
            sides = [trees[i, 0:j], trees[i, (j+1):size], trees[0:i, j], trees[(i+1):size, j]]
            if any([np.max(side) < trees[i,j] for side in sides]):
                continue
            else:
                shape[i,j] += 1

    print('Solution part 1 : ', np.size(trees) - np.sum(shape))
    
    for i in range(1, size-1):
        for j in range(1, size-1):
            sides = [np.flip(trees[i, 0:j]), trees[i, (j+1):size], np.flip(trees[0:i, j]), trees[(i+1):size, j]]
            liste = [np.where(side >= trees[i, j])[0][0] + 1 if np.any(side >= trees[i, j]) else side.size for side in sides]
            scenic.append(np.prod(np.array(liste)))
            
    print('Solution part 2 : ', max(scenic))
            
            

            
        
