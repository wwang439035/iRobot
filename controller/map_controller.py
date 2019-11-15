from render.ui import *


def init_env():
    renderBackground()
    panda = renderPanda((0, 0))
    apple = renderApple((WINDOW_WIDTH - appleSize // 2, WINDOW_HEIGHT - appleSize // 2))
    walls = changeMap([apple, panda])
    renderWalls(walls)
    map_grid = generateMap(walls)
    return map_grid, panda, apple


def change_map(objects):
    walls = changeMap(objects)
    renderWalls(walls)
    map_grid = generateMap(walls)
    return map_grid


def render_robot(robot_pos, goal_pos):
    renderPanda(robot_pos)
    renderApple(goal_pos)


def render_path(path):
    renderPath(path)


def render_complete():
    renderComplete()
