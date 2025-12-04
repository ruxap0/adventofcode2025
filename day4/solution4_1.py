import numpy as np

with open('day4/input4.txt') as f:
    solution = 0
    grid = [list(line.strip()) for line in f.readlines()]
    grid = np.asarray(grid)
    grid = np.pad(grid, 1, mode='constant', constant_values='.')
    
    for i in range(1, grid.shape[0]):
        for j in range(1, grid.shape[1]):
            if grid[i, j] == '@':
                subgrid = grid[i-1:i+2, j-1:j+2]
                if np.sum(subgrid == '@') < 5: # 4 around + center
                    solution += 1

    print(solution)