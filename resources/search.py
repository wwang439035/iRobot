import numpy as np

grid_map = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]
start = [0, 0]
end = [len(grid_map) - 1, len(grid_map[0]) - 1]
expense = 1

delta = [[-1, 0],
         [0, -1],
         [1, 0],
         [0, 1]]

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    policy[len(grid) - 1][len(grid[0]) - 1] = '*'

    x = init[0]
    y = init[1]
    g = 0

    open_list = [[g, x, y]]

    found = False
    resign = False
    count = 0

    while not found and not resign:
        if len(open_list) == 0:
            resign = True
            return 'fail'
        else:
            open_list.sort()
            open_list.reverse()
            next_rp = open_list.pop()
            x = next_rp[1]
            y = next_rp[2]
            g = next_rp[0]

            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open_list.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i

    x = goal[0]
    y = goal[1]

    while [x, y] != init:
        back_x = x - delta[action[x][y]][0]
        back_y = y - delta[action[x][y]][1]
        policy[back_x][back_y] = delta_name[action[x][y]]
        x = back_x
        y = back_y

    print(np.array(expand))
    return policy


print(np.array(search(grid_map, start, end, expense)))
