import numpy as np

grid_map = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0]]
end = [len(grid_map) - 1, len(grid_map[0]) - 1]
expense = 1

delta = [[-1, 0],
         [0, -1],
         [1, 0],
         [0, 1]]

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    value = [[99 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x == goal[0] and y == goal[1]:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True
                elif grid[x][y] == 0:
                    for i, action in enumerate(delta):
                        x2 = x + action[0]
                        y2 = y + action[1]
                        if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost
                            if v2 < value[x][y]:
                                value[x][y] = v2
                                policy[x][y] = delta_name[i]
                                change = True
    print np.array(value)
    return policy


print np.array(compute_value(grid_map, end, expense))
