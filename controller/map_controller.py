from render.ui import *



def init_env():
    panda = renderPanda((0, 0))
    apple = renderApple((WINDOW_WIDTH - appleSize // 2, WINDOW_HEIGHT - appleSize // 2))
    walls = changeMap([apple, panda])
    renderWalls(walls)
    map_grid = generateMap()
    return map_grid, [panda.x, panda.y], [apple.x, apple.y]


def change_map(objects):
    changeMap(objects)
    map_grid = generateMap()
    return map_grid


def render_robot(robot_pos, goal_pos):
    renderPanda(robot_pos)
    renderApple(goal_pos)


def render_path(path):
    renderPath(path)


def render_complete():
    renderComplete()
