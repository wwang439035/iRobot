from search.search import *


def get_path(grid, robot_pos, goal_pos):
    path = search(grid, robot_pos, goal_pos)
    return path

