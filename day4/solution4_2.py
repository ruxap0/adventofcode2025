import numpy as np

with open('day4/input4.txt') as f:
    solution = 0
    changed = False
    grid = [list(line.strip()) for line in f.readlines()]
    grid = np.asarray(grid)
    grid = np.pad(grid, 1, mode='constant', constant_values='.')
    
    i = 1

    while i != grid.shape[0]:
        j = 1

        while j != grid.shape[1]:
            if grid[i, j] == '@':
                subgrid = grid[i-1:i+2, j-1:j+2]
                if np.sum(subgrid == '@') < 5:
                    solution += 1
                    grid[i, j] = '.'
                    changed = True
            j += 1
        if changed and i > 1:
            i -= 2
            changed = False
        else:
            i += 1
        
                    

    print(solution)