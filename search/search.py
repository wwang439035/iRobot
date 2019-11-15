import numpy as np
from copy import deepcopy

grid_map = [['.', '#', '.', '.', '#', '.'],
            ['.', '#', '.', '.', '.', '.'],
            ['.', '#', '.', '#', '#', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '.', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '.', '.', '#', '#', '.']]

startPos = [0, 0]
endPos = [14, 5]
cost = 1
delta_name = ['^', '<', 'v', '>']
delta = [[-1, 0],
         [0, -1],
         [1, 0],
         [0, 1]]


def search(grid, start_pos, end_pos):
    h_grid = get_heuristic_grid(grid)
    # print np.array(h_grid)
    shortest_path = get_a_star_search_path(grid, start_pos, end_pos, h_grid)
    # print np.array(shortest_path)
    smooth_shortest_path = smooth(shortest_path)
    # smooth_shortest_path = refine(smooth_shortest_path)
    return smooth_shortest_path


def refine(path):
    width = 2
    height = len(path)

    for h in range(height):
        for w in range(width):
            path[h][w] = float("{0:.2f}".format(path[h][w]))

    return path


def get_heuristic_grid(grid):
    height = len(grid)
    width = 0 if height is 0 else len(grid[0])
    max = height + width - 2
    h_grid = [[max-w-h for w in range(width)] for h in range(height)]
    return h_grid


def get_a_star_search_path(grid, start_pos, end_pos, h_grid):
    path = [end_pos]
    height = len(grid)
    width = 0 if height is 0 else len(grid[0])

    closed = [[0 for col in range(width)] for row in range(height)]
    closed[start_pos[0]][start_pos[1]] = 1

    # policy = [[' ' for row in range(width)] for col in range(height)]
    # policy[height - 1][width - 1] = '*'

    expand = [[-1 for col in range(width)] for row in range(height)]
    action = [[-1 for col in range(width)] for row in range(height)]

    x = start_pos[0]
    y = start_pos[1]
    g = 0
    f = g + h_grid[x][y]

    open = [[f, g, x, y]]

    found = False
    resign = False
    count = 0

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[2]
            y = next[3]
            g = next[1]
            expand[x][y] = count
            count += 1

            if x == end_pos[0] and y == end_pos[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if 0 <= x2 < height and 0 <= y2 < width:
                        if closed[x2][y2] == 0 and grid[x2][y2] == '.':
                            g2 = g + cost
                            f2 = g2 + h_grid[x2][y2]
                            open.append([f2, g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    x = end_pos[0]
    y = end_pos[1]

    while [x, y] != start_pos:
        back_x = x - delta[action[x][y]][0]
        back_y = y - delta[action[x][y]][1]
        # policy[back_x][back_y] = delta_name[action[x][y]]
        x = back_x
        y = back_y
        path.insert(0, [x, y])

    # print np.array(policy)
    return path


def smooth(path, weight_data=0.5, weight_smooth=0.1, tolerance=0.000001):
    newpath = deepcopy(path)
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(1, len(newpath) - 1):
            for j in range(len(newpath[0])):
                point = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j]) + weight_smooth * (
                        newpath[i + 1][j] + newpath[i - 1][j] - 2.0 * newpath[i][j])
                change += abs(point - newpath[i][j])
    return newpath


print(np.array(search(grid_map, startPos, endPos)))