from controller.map_controller import *
from controller.search_controller import *

MAP_SIZE = [800, 600]
MAP_CHANGE_DURATION = 1000
ACTIONS = ['lift', 'down']
NUM_BOX = 5


def main():
    map_grid, robot_pos, goal_pos = init_env(MAP_SIZE)
    input("Press a key to start")

    for _ in range(NUM_BOX):
        for action in ACTIONS:
            time_step = 0
            path_index = 0
            print(time_step)

            path = get_path(map_grid, robot_pos, goal_pos)
            render_path(path)

            while time_step < MAP_CHANGE_DURATION and path_index < len(path):
                render_robot(path[path_index])
                path_index += 1
                time_step += 1

            if path_index == len(path):
                if action == ACTIONS[0]:
                    render_lift()
                else:
                    render_down()

                continue

            map_grid, box_pos = change_map(path[path_index])


if __name__ == '__main__':
    main()
