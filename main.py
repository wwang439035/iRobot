from controller.map_controller import *
from controller.search_controller import *
from render.ui import *
import time


MAP_CHANGE_DURATION = 15
CPU_CYCLE = 1000


def main():
    map_grid, robot, goal = init_env()
    input("Press a key to start")

    while True:
        time_step = 0
        start_time = time.time()
        current_time = start_time
        path_index = 0

        path = get_path(map_grid, [robot.x, robot.y], [goal.x, goal.y])
        render_path(path)

        while current_time - start_time < MAP_CHANGE_DURATION and path_index < len(path):
            setFramerate(30)
            if time_step / CPU_CYCLE == 0:
                render_robot(path[path_index], [goal.x, goal.y])
                path_index += 1
                current_time = time.time()
            time_step += 1

        if path_index == len(path):
            render_complete()
            break

        map_grid, box_pos = change_map([robot, goal])


if __name__ == '__main__':
    main()
