from controller.map_controller import *
from controller.search_controller import *
from render.ui import *
import numpy as np
import time


MAP_CHANGE_DURATION = 15
CPU_CYCLE = 1000


def main():
    map_grid, robot, goal, walls = init_env()
    # input("Press a key to start")

    path_index = 0
    print(np.array(map_grid))
    path = get_path(map_grid, [robot.x, robot.y], [goal.x, goal.y])
    print(path)
    while True:
        setFramerate(30)
        renderBackground()
        render_robot(path[path_index], [goal.x, goal.y])
        renderWalls(walls)
        render_path(path)

        path_index += 1
        print(path_index)

        if path_index == len(path):
            render_complete()
            break

        # map_grid, box_pos = change_map([robot, goal])


if __name__ == '__main__':
    main()
