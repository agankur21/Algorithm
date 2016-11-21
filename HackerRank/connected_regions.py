def update_connected_neighbours(grid, i, j, search_grid, list_connected_neighbours):
    if grid[i][j] == 0:
        return list_connected_neighbours
    # Consider 8 neighbours for this :
    m = len(grid)
    n = len(grid[0])
    if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == 1 and search_grid[i - 1][j - 1] == False:
        list_connected_neighbours.append((i - 1, j - 1))
        search_grid[i - 1][j - 1] = True
        update_connected_neighbours(grid, i - 1, j - 1, search_grid, list_connected_neighbours)
    if i - 1 >= 0 and grid[i - 1][j] == 1 and search_grid[i - 1][j] == False:
        list_connected_neighbours.append((i - 1, j))
        search_grid[i - 1][j] = True
        update_connected_neighbours(grid, i - 1, j, search_grid, list_connected_neighbours)
    if i - 1 >= 0 and j + 1 < n and grid[i - 1][j + 1] == 1 and search_grid[i - 1][j + 1] == False:
        list_connected_neighbours.append((i - 1, j + 1))
        search_grid[i - 1][j + 1] = True
        update_connected_neighbours(grid, i - 1, j + 1, search_grid, list_connected_neighbours)
    if j - 1 >= 0 and grid[i][j - 1] == 1 and search_grid[i][j - 1] == False:
        list_connected_neighbours.append((i, j - 1))
        search_grid[i][j - 1] = True
        update_connected_neighbours(grid, i, j - 1, search_grid, list_connected_neighbours)
    if j + 1 < n and grid[i][j + 1] == 1 and search_grid[i][j + 1] == False:
        list_connected_neighbours.append((i, j + 1))
        search_grid[i][j + 1] = True
        update_connected_neighbours(grid, i, j + 1, search_grid, list_connected_neighbours)
    if i + 1 < m and j - 1 >= 0 and grid[i + 1][j - 1] == 1 and search_grid[i + 1][j - 1] == False:
        list_connected_neighbours.append((i + 1, j - 1))
        search_grid[i + 1][j - 1] = True
        update_connected_neighbours(grid, i + 1, j - 1, search_grid, list_connected_neighbours)
    if i + 1 < m and grid[i + 1][j] == 1 and search_grid[i + 1][j] == False:
        list_connected_neighbours.append((i + 1, j))
        search_grid[i + 1][j] = True
        update_connected_neighbours(grid, i + 1, j, search_grid, list_connected_neighbours)
    if i + 1 < m and j + 1 < n and grid[i + 1][j + 1] == 1 and search_grid[i + 1][j + 1] == False:
        list_connected_neighbours.append((i + 1, j + 1))
        search_grid[i + 1][j + 1] = True
        update_connected_neighbours(grid, i + 1, j + 1, search_grid, list_connected_neighbours)
    return list_connected_neighbours


def get_biggest_region(grid):
    m = len(grid)
    n = len(grid[0])
    search_grid = [[False] * n for i in range(m)]
    max_length = 0
    for i in range(m):
        for j in range(n):
            if search_grid[i][j] == False:
                search_grid[i][j] = True
                list_connected_neighbours = update_connected_neighbours(grid, i, j, search_grid, [])
                if (max_length < len(list_connected_neighbours)):
                    max_length = len(list_connected_neighbours)
    return max_length


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)

