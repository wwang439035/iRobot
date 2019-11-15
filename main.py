from controller.map_controller import *
from controller.search_controller import *
import time

MAP_SIZE = [800, 600]
MAP_CHANGE_DURATION = 15
ACTIONS = ['lift', 'down']
NUM_BOX = 5


def main():
    map_grid, robot_pos, goal_pos = init_env(MAP_SIZE)
    input("Press a key to start")

    for _ in range(NUM_BOX):
        for action in ACTIONS:
            start_time = time.time()
            path_index = 0

            path = get_path(map_grid, robot_pos, goal_pos)
            render_path(path)

            while current_time - start_time < MAP_CHANGE_DURATION and path_index < len(path):
                render_robot(path[path_index])
                path_index += 1
                current_time = time.time()

            if path_index == len(path):
                if action == ACTIONS[0]:
                    render_lift()
                else:
                    render_down()
                continue

            map_grid, box_pos = change_map(path[path_index])


if __name__ == '__main__':
    main()
