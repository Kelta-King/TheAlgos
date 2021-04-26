def createGrid(r, c, grid_at_previous_step):
    grid_at_next_step = [['O'] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            current_cell = grid_at_previous_step[i][j]
            if current_cell == 'O':
                grid_at_next_step[i][j] = '.'
                if i - 1 >= 0:
                    grid_at_next_step[i - 1][j] = '.'
                if i + 1 <= r - 1:
                    grid_at_next_step[i + 1][j] = '.'
                if j - 1 >= 0:
                    grid_at_next_step[i][j - 1] = '.'
                if j + 1 <= c - 1:
                    grid_at_next_step[i][j + 1] = '.'
    return grid_at_next_step


def bomberMan(n, r, c, initial_grid):

    grid_after_first_detonation = createGrid(r, c, initial_grid)

    if n % 2 == 0:
        return [['O'] * c for _ in range(r)]
    elif n < 4:
        return initial_grid if n == 1 else grid_after_first_detonation
    else:
        grid_after_second_detonation = createGrid(r, c, grid_after_first_detonation)
        grid_after_third_detonation = createGrid(r, c, grid_after_second_detonation)
        
    return grid_after_second_detonation if n % 4 == 1 else grid_after_third_detonation


n = 3
grid = ['.......', '...O...', '....O..','.......', 'OO.....', 'OO.....']
r = len(grid)
c = len(grid[0])
x = bomberMan(n, r, c, grid)

for y in x:
    print(y)