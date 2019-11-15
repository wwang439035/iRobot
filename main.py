from controller.map_controller import *
from controller.search_controller import *
import time

MAP_SIZE = [800, 600]
MAP_CHANGE_DURATION = 15
CPU_CYCLE = 1000


def main():
    map_grid, robot_pos, goal_pos = init_env(MAP_SIZE)
    input("Press a key to start")

    while True:
        time_step = 0
        start_time = time.time()
        current_time = start_time
        path_index = 0

        path = get_path(map_grid, robot_pos, goal_pos)
        render_path(path)

        while current_time - start_time < MAP_CHANGE_DURATION and path_index < len(path):
            if time_step / CPU_CYCLE == 0:
                render_robot(path[path_index])
                path_index += 1
                current_time = time.time()
            time_step += 1

        if path_index == len(path):
            render_complete()
            break

        map_grid, box_pos = change_map(path[path_index])


if __name__ == '__main__':
    main()
