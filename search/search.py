import numpy as np
from copy import deepcopy

grid_map = [[0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0]]

startPos = [0, 0]
endPos = [4, 5]


def search(grid, start_pos, end_pos):
    shortest_path = getShortestPath(grid, start_pos, end_pos)
    smooth_shortest_path = smooth(shortest_path)
    return smooth_shortest_path


def getShortestPath(grid, start_pos, end_pos):
    path = []
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


print np.array(search(grid_map, startPos, endPos))