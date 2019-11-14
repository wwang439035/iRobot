######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################

'''
=== Introduction ===

Your file must be called `warehouse.py` and must have two classes
  called `DeliveryPlanner_PartA` and `DeliveryPlanner_PartB`.

- You may add additional classes and functions as needed provided they are all in this file `warehouse.py`.
- You may share code between partA and partB but it MUST BE IN THIS FILE
- Upload warehouse.py to Canvas in the Assignments section. Do NOT put it into an 
  archive with other files.
- Your warehouse.py file must not execute any code when imported.
- Ask any questions about the directions or specifications on Piazza.

=== Grading ===

- Your planner will be graded against a set of test cases, each equally weighted.
- If your planner returns a list of moves of total cost that is K times the minimum cost of 
  successfully completing the task, you will receive 1/K of the credit for that test case.
- Otherwise, you will receive no credit for that test case. This could happen for one of several 
  reasons including (but not necessarily limited to):
  - plan_delivery's moves do not deliver the boxes in the correct order.
  - plan_delivery's output is not a list of strings in the prescribed format.
  - plan_delivery does not return an output within the prescribed time limit.
  - Your code raises an exception.

=== Part A ===

In this Part A, you will build a planner that helps a robot
  find the best path through a warehouse filled with boxes
  that it has to pick up and deliver to a dropzone.

`DeliveryPlanner_PartA` must have an `__init__` function that takes three 
  arguments: `self`, `warehouse`, and `todo`.
`DeliveryPlanner_PartA` must also have a function called `plan_delivery` that 
  takes a single argument, `self`.

=== Part A Input Specifications ===

`warehouse` will be a list of m strings, each with n characters,
  corresponding to the layout of the warehouse. The warehouse is an
  m x n grid. warehouse[i][j] corresponds to the spot in the ith row
  and jth column of the warehouse, where the 0th row is the northern
  end of the warehouse and the 0th column is the western end.

The characters in each string will be one of the following:

'.' (period) : traversable space. The robot may enter from any adjacent space.
'#' (hash) : a wall. The robot cannot enter this space.
'@' (dropzone): the starting point for the robot and the space where all boxes must be delivered.
  The dropzone may be traversed like a '.' space.
[0-9a-zA-Z] (any alphanumeric character) : a box. At most one of each alphanumeric character 
  will be present in the warehouse (meaning there will be at most 62 boxes). A box may not
  be traversed, but if the robot is adjacent to the box, the robot can pick up the box.
  Once the box has been removed, the space functions as a '.' space.

For example, 
  warehouse = ['1#2',
               '.#.',
               '..@']
  is a 3x3 warehouse.
  - The dropzone is at the warehouse cell in row 2, column 2.
  - Box '1' is located in the warehouse cell in row 0, column 0.
  - Box '2' is located in the warehouse cell in row 0, column 2.
  - There are walls in the warehouse cells in row 0, column 1 and row 1, column 1.
  - The remaining five warehouse cells contain empty space. (The dropzone is empty space)
#
The argument `todo` is a list of alphanumeric characters giving the order in which the 
  boxes must be delivered to the dropzone. For example, if 
  todo = ['1','2']
  is given with the above example `warehouse`, then the robot must first deliver box '1'
  to the dropzone, and then the robot must deliver box '2' to the dropzone.

=== Part A Rules for Movement ===

- Two spaces are considered adjacent if they share an edge or a corner.
- The robot may move horizontally or vertically at a cost of 2 per move.
- The robot may move diagonally at a cost of 3 per move.
- The robot may not move outside the warehouse.
- The warehouse does not "wrap" around.
- As described earlier, the robot may pick up a box that is in an adjacent square.
- The cost to pick up a box is 4, regardless of the direction the box is relative to the robot.
- While holding a box, the robot may not pick up another box.
- The robot may put a box down on an adjacent empty space ('.') or the dropzone ('@') at a cost
  of 2 (regardless of the direction in which the robot puts down the box).
- If a box is placed on the '@' space, it is considered delivered and is removed from the ware-
  house.
- The warehouse will be arranged so that it is always possible for the robot to move to the 
  next box on the todo list without having to rearrange any other boxes.

An illegal move will incur a cost of 100, and the robot will not move (the standard costs for a 
  move will not be additionally incurred). Illegal moves include:
- attempting to move to a nonadjacent, nonexistent, or occupied space
- attempting to pick up a nonadjacent or nonexistent box
- attempting to pick up a box while holding one already
- attempting to put down a box on a nonadjacent, nonexistent, or occupied space
- attempting to put down a box while not holding one

=== Part A Output Specifications ===

`plan_delivery` should return a LIST of moves that minimizes the total cost of completing
  the task successfully.
Each move should be a string formatted as follows:

'move {i} {j}', where '{i}' is replaced by the row-coordinate of the space the robot moves
  to and '{j}' is replaced by the column-coordinate of the space the robot moves to

'lift {x}', where '{x}' is replaced by the alphanumeric character of the box being picked up

'down {i} {j}', where '{i}' is replaced by the row-coordinate of the space the robot puts 
  the box, and '{j}' is replaced by the column-coordinate of the space the robot puts the box

For example, for the values of `warehouse` and `todo` given previously (reproduced below):
  warehouse = ['1#2',
               '.#.',
               '..@']
  todo = ['1','2']
`plan_delivery` might return the following:
  ['move 2 1',
   'move 1 0',
   'lift 1',
   'move 2 1',
   'down 2 2',
   'move 1 2',
   'lift 2',
   'down 2 2']

=== Part B ===

In this Part B, you will again build a planner that helps a robot
  find the best path through a warehouse filled with boxes
  that it has to pick up and deliver to a dropzone. Unlike Part A,
  however, in this problem the robot is moving in a continuous world
  (albeit in discrete time steps) and has constraints on the amount
  it can turn its wheels in a given time step.

`DeliveryPlanner_PartB` must have an `__init__` function that takes five 
  arguments: `self`, `warehouse`, `todo`, `max_distance`, and
  `max_steering`.
`DeliveryPlanner_PartB` must also have a function called `plan_delivery` that 
  takes a single argument, `self`.

=== Part B Input Specifications ===

`warehouse` will be a list of m strings, each with n characters,
  corresponding to the layout of the warehouse. The warehouse is an
  m x n grid. warehouse[i][j] corresponds to the spot in the ith row
  and jth column of the warehouse, where the 0th row is the northern
  end of the warehouse and the 0th column is the western end.

The characters in each string will be one of the following:

'.' (period) : traversable space.
'#' (hash) : a wall. If the robot contacts a wall space, it will crash.
'@' (dropzone): the space where all boxes must be delivered. The dropzone may be traversed like 
  a '.' space.

Each space is a 1 x 1 block. The upper-left corner of space warehouse[i][j] is at the point (j,-i) in
  the plane. Spaces outside the warehouse are considered walls; if any part of the robot leaves the 
  warehouse, it will be considered to have crashed into the exterior wall of the warehouse.

For example, 
  warehouse = ['.#.',
               '.#.',
               '..@']
  is a 3x3 warehouse. The dropzone is at space (2,-2) and there are walls at spaces (1,0) 
  and (1,-1). The rest of the warehouse is empty space.

The robot is a square of width 0.5. The robot begins centered in the dropzone space.
  The robot's initial bearing is 0.

The argument `todo` is a list of points representing the center point of each box.
  todo[0] is the first box which must be delivered, followed by todo[1], and so on.
  Each box is a square of size 0.2 x 0.2. If the robot contacts a box, it will crash.

The arguments `max_distance` and `max_steering` are parameters constraining the movement
  of the robot on a given time step. They are described more below.

=== Part B Rules for Movement ===

- The robot may move any distance between 0 and `max_distance` per time step.
- The robot may set its steering angle anywhere between -`max_steering` and 
  `max_steering` per time step. A steering angle of 0 means that the robot will
  move according to its current bearing. A positive angle means the robot will 
  turn counterclockwise by `steering_angle` radians; a negative steering_angle 
  means the robot will turn clockwise by abs(steering_angle) radians.
- Upon a movement, the robot will change its steering angle instantaneously to the 
  amount indicated by the move, and then it will move a distance in a straight line in its
  new bearing according to the amount indicated move.
- The cost per move is 1 plus the amount of distance traversed by the robot on that move.

- The robot may pick up a box whose center point is within 0.5 units of the robot's center point.
- If the robot picks up a box, it incurs a total cost of 2 for that move (this already includes 
  the 1-per-move cost incurred by the robot).
- While holding a box, the robot may not pick up another box.
- The robot may put a box down at a total cost of 1.5 for that move. The box must be placed so that:
  - The box is not contacting any walls, the exterior of the warehouse, any other boxes, or the robot
  - The box's center point is within 0.5 units of the robot's center point
- A box is always oriented so that two of its edges are horizontal and the other two are vertical.
- If a box is placed entirely within the '@' space, it is considered delivered and is removed from the 
  warehouse.
- The warehouse will be arranged so that it is always possible for the robot to move to the 
  next box on the todo list without having to rearrange any other boxes.

- If the robot crashes, it will stop moving and incur a cost of 100*distance, where distance
  is the length it attempted to move that move. (The regular movement cost will not apply.)
- If an illegal move is attempted, the robot will not move, but the standard cost will be incurred.
  Illegal moves include (but are not necessarily limited to):
    - picking up a box that doesn't exist or is too far away
    - picking up a box while already holding one
    - putting down a box too far away or so that it's touching a wall, the warehouse exterior, 
      another box, or the robot
    - putting down a box while not holding a box

=== Part B Output Specifications ===

`plan_delivery` should return a LIST of strings, each in one of the following formats.

'move {steering} {distance}', where '{steering}' is a floating-point number between
  -`max_steering` and `max_steering` (inclusive) and '{distance}' is a floating-point
  number between 0 and `max_distance`

'lift {b}', where '{b}' is replaced by the index in the list `todo` of the box being picked up
  (so if you intend to lift box 0, you would return the string 'lift 0')

'down {x} {y}', where '{x}' is replaced by the x-coordinate of the center point of where the box
  will be placed and where '{y}' is replaced by the y-coordinate of that center point
  (for example, 'down 1.5 -2.9' means to place the box held by the robot so that its center point
  is (1.5,-2.9)).

'''
from copy import deepcopy
from math import sqrt, atan2, pi
import numpy as np

moves = [[-1, -1], [-1, 0], [-1, 1],
         [0, -1], [0, 1],
         [1, -1], [1, 0], [1, 1]]
straight_moves = [1, 3, 4, 6]
diagonal_moves = [0, 2, 5, 7]
actions = ['move', 'lift', 'down', 'na']

robot_size = 0.5
box_size = 0.2
min_dist = 0.4
max_combine = 3
times = 10


# https://repl.it/@billdtnguyen/Project2-Warehouse
class DeliveryPlanner_PartA:

    def __init__(self, warehouse, todo):
        self.grid = warehouse
        self.todo = todo
        self.num_row = len(self.grid)
        self.num_col = len(self.grid[0])
        self.drop_zone = self.get_drop_zone()
        self.goals = self.get_boxes()
        self.moves = []

    def plan_delivery(self):
        position = []
        for i, box in enumerate(self.goals):
            self.remove_box(self.todo[i])
            if i == 0:
                start = self.drop_zone
            else:
                start = position

            # take a box
            (move_list, position) = self.search(start, self.goals[i], self.todo[i], [3, 2])
            self.moves = self.moves + move_list

            # move outside of drop zone if needed
            if position == self.drop_zone:
                (move_list, position) = self.move_outside_drop_zone(i)
                self.moves = self.moves + move_list

            # drop a box onto drop zone
            (move_list, position) = self.search(position, self.drop_zone, None, [3, 2])
            self.moves = self.moves + move_list

        # print self.moves
        return self.moves

    def search(self, init, goal, goal_name, cost):
        closed = [[0 for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        closed[init[0]][init[1]] = 1
        expand = [[-1 for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        action = [[-1 for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        policy = []

        x = init[0]
        y = init[1]
        g = 0
        f = g + self.heuristic([x, y], goal)

        open_list = [[f, g, x, y]]

        found = False
        resign = False
        count = 0

        while not found and not resign:
            if len(open_list) == 0:
                resign = True
                return ["Failed"], goal
            else:
                open_list.sort()
                open_list.reverse()
                next_route_point = open_list.pop()
                x = next_route_point[2]
                y = next_route_point[3]
                g = next_route_point[1]
                expand[x][y] = count
                count += 1

                if x == goal[0] and y == goal[1]:
                    found = True
                else:
                    for i in range(len(moves)):
                        x2 = x + moves[i][0]
                        y2 = y + moves[i][1]
                        if 0 <= x2 < len(self.grid) and 0 <= y2 < len(self.grid[0]):
                            g2 = g + cost[(abs(moves[i][0]) + abs(moves[i][1])) % 2]
                            f2 = g2 + self.heuristic([x2, y2], goal)
                            if (closed[x2][y2] == 0 or f2 < closed[x2][y2]) and self.grid[x2][y2] == '.':
                                open_list.append([f2, g2, x2, y2])
                                closed[x2][y2] = f2
                                action[x2][y2] = i
        x = goal[0]
        y = goal[1]

        while [x, y] != init:
            back_x = x - moves[action[x][y]][0]
            back_y = y - moves[action[x][y]][1]
            policy.append("{} {} {}".format(actions[0], back_x, back_y))
            x = back_x
            y = back_y

        point = policy.pop()
        policy.reverse()
        if goal_name is not None:
            policy.append("{} {}".format(actions[1], goal_name))
        else:
            policy.append("{} {} {}".format(actions[2], goal[0], goal[1]))

        # print policy
        if len(policy) > 1:
            position = policy[-2].split(' ')
        elif len(policy) > 0 and len(policy[-1].split(' ')) > 2 and policy[-1].split(' ')[0] == actions[0]:
            position = policy[-1].split(' ')
        else:
            point = point.split(' ')
            position = [actions[3]] + [point[1], point[2]]
        return policy, [int(position[1]), int(position[2])]

    def move_outside_drop_zone(self, i):
        next_goal = self.goals[i + 1]
        position = []
        cost = 999

        for direction in straight_moves:
            x = self.drop_zone[0] + moves[direction][0]
            y = self.drop_zone[1] + moves[direction][1]
            h = self.heuristic([x, y], next_goal)
            if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
                if self.grid[x][y] == '.':
                    if 0 < h < cost:
                        cost = h
                        position = [x, y]

        return ["{} {} {}".format(actions[0], position[0], position[1])], position

    @classmethod
    def heuristic(cls, a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        return 2 * (dx + dy) + (3 - 2 * 2) * min(dx, dy)

    def get_drop_zone(self):
        for i in range(self.num_row):
            for j in range(self.num_col):
                if self.grid[i][j] == '@':
                    self.grid[i] = self.grid[i][0:j] + '.' + self.grid[i][j + 1:]
                    return [i, j]
        return []

    def get_boxes(self):
        boxes = []
        for box in self.todo:
            for i in range(self.num_row):
                for j in range(self.num_col):
                    if self.grid[i][j] == box:
                        boxes.append([i, j])
        return boxes

    def remove_box(self, box):
        for i in range(self.num_row):
            for j in range(self.num_col):
                if self.grid[i][j] == box:
                    self.grid[i] = self.grid[i][0:j] + '.' + self.grid[i][j + 1:]


class DeliveryPlanner_PartB:

    def __init__(self, warehouse, todo, max_distance, max_steering):
        self.grid = warehouse
        self.goals = todo
        self.max_distance = max_distance
        self.max_steering = max_steering
        self.num_row = len(self.grid) * times
        self.num_col = len(self.grid[0]) * times
        self.drop_zone = self.get_drop_zone()
        self.position = [self.drop_zone[0], self.drop_zone[1], 0]
        self.moves = []

    def plan_delivery(self):
        for i, box in enumerate(self.goals):
            # take a box
            goal = self.convert_to_extend_grid_xy([self.goals[i][1], abs(self.goals[i][0])])
            move_list = self.search(goal, i)
            self.moves = self.moves + move_list

            # move outside of drop zone if needed
            if self.get_distance(self.position, self.drop_zone) <= min_dist * times:
                move_list = self.move_outside_drop_zone(i)
                self.moves = self.moves + move_list

            # drop a box onto drop zone
            move_list = self.search(self.drop_zone, None)
            self.moves = self.moves + move_list

        print self.moves
        return self.moves

    def search(self, goal, goal_index):
        init = self.position
        closed = [[0 for _ in range(self.num_col)] for _ in range(self.num_row)]
        closed[init[0]][init[1]] = 1
        expand = [[-1 for _ in range(self.num_col)] for _ in range(self.num_row)]
        action = [[-1 for _ in range(self.num_col)] for _ in range(self.num_row)]
        path = []

        x = init[0]
        y = init[1]
        g = 0
        f = g + self.heuristic([x, y], goal)

        open_list = [[f, g, x, y]]

        found = False
        resign = False
        count = 0

        while not found and not resign:
            if len(open_list) == 0:
                resign = True
                return ["Failed"], goal
            else:
                open_list.sort()
                open_list.reverse()
                next_route_point = open_list.pop()
                x = next_route_point[2]
                y = next_route_point[3]
                g = next_route_point[1]

                expand[x][y] = count
                count += 1
                # print next_route_point
                if x == goal[0] and y == goal[1]:
                    found = True
                else:
                    for i in range(len(moves)):
                        x2 = x + moves[i][0]
                        y2 = y + moves[i][1]
                        if 0 <= x2 < self.num_row and 0 <= y2 < self.num_col and self.no_wall([x2, y2]):
                            g2 = g + self.cost([x2, y2], [x, y])
                            f2 = g2 + self.heuristic([x2, y2], goal)
                            grid_xy = self.convert_to_grid_xy([x2, y2])
                            if (closed[x2][y2] == 0 or f2 < closed[x2][y2]) and self.grid[grid_xy[0]][
                                grid_xy[1]] == '.':
                                open_list.append([f2, g2, x2, y2])
                                closed[abs(int(x2))][int(y2)] = f2
                                action[abs(int(x2))][int(y2)] = i
        x = goal[0]
        y = goal[1]

        while x != init[0] and y != init[1]:
            back_x = x - moves[action[x][y]][0]
            back_y = y - moves[action[x][y]][1]
            path.append([actions[0], back_x, back_y])
            x = back_x
            y = back_y

        search = True
        path_index = 0
        while search:
            dist = self.get_distance(goal, [path[path_index][1], path[path_index][2]])
            if dist > min_dist * times:
                path = path[path_index:]
                search = False
            path_index += 1

        point = path.pop()
        path.reverse()
        if goal_index is not None:
            path.append([actions[1], goal_index])
        else:
            path.append([actions[2], goal[0], goal[1]])

        # print path
        if len(path) > 1:
            position = path[-2]
        elif len(path) > 0 and len(path[-1]) > 2 and path[-1][0] == actions[0]:
            position = path[-1]
        else:
            position = [actions[3]] + [point[1], point[2]]

        policy = self.transform_path(path, action)
        self.position = [position[1], position[2]]
        return policy

    def transform_path(self, way_points, action):
        policy = []
        wp_queue = []
        n = len(way_points)
        change_points = []
        first_action = -1
        start = 0
        finished = False

        for i in range(n - 1):
            wp = way_points[i]
            wp_queue.append(wp)
            tmp_action = moves[action[wp[1]][wp[2]]]

            if tmp_action != first_action:
                change_points.append(i)
                first_action = tmp_action
        change_points.append(n - 1)

        n = len(change_points)
        for _ in range(n):
            if start + 3 < n and (
                    change_points[start + 2] - change_points[start + 1] <= max_combine and change_points[
                        start + 1] - change_points[start] <= max_combine or
                    change_points[start + 3] - change_points[start + 2] <= max_combine and change_points[
                        start + 1] - change_points[start] <= max_combine or
                    change_points[start + 3] - change_points[start + 2] <= max_combine and change_points[start + 2] -
                        change_points[start + 1] <= max_combine
            ):
                prepared_wps = wp_queue[change_points[start]:change_points[start + 3]]
                start += 3
            elif start + 2 < n and (change_points[start + 2] - change_points[start + 1] <= max_combine or change_points[
                start + 1] - change_points[start] <= max_combine):
                prepared_wps = wp_queue[change_points[start]:change_points[start + 2]]
                start += 2
            elif start + 1 < n:
                prepared_wps = wp_queue[change_points[start]:change_points[start + 1]]
                start += 1
            else:
                prepared_wps = wp_queue[start:]
                finished = True

            if len(prepared_wps) > 0:
                steering_angle = self.get_steering_angle([prepared_wps[0][1], prepared_wps[0][2]],
                                                         [prepared_wps[-1][1], prepared_wps[-1][2]])
                distance = self.get_distance([prepared_wps[0][1], prepared_wps[0][2]],
                                             [prepared_wps[-1][1], prepared_wps[-1][2]])

                while abs(steering_angle) > 0:
                    angle = min(steering_angle, self.max_steering)
                    steering_angle -= angle
                    if steering_angle > 0:
                        policy.append("{} {} {}".format(actions[0], angle, 0.0))
                    else:
                        while distance > 0:
                            dist = min(distance, self.max_distance * times)
                            distance -= dist
                            policy.append("{} {} {}".format(actions[0], angle, dist / times))
            if finished:
                break

        if way_points[-1][0] == actions[1]:
            policy.append("{} {}".format(actions[1], way_points[-1][1]))
            return policy
        elif way_points[-1][0] == actions[2]:
            result_xy = self.convert_to_result_xy([way_points[-1][1], way_points[-1][2]])
            policy.append("{} {} {}".format(actions[2], result_xy[0], result_xy[1]))
            return policy
        return ""

    def move_outside_drop_zone(self, i):
        next_goal = self.convert_to_extend_grid_xy(self.goals[i + 1])
        move_to = []
        policy = []
        cost = 999

        for direction in straight_moves:
            x = self.drop_zone[0] + min_dist * times * moves[direction][0]
            y = self.drop_zone[1] + min_dist * times * moves[direction][1]
            h = self.heuristic([x, y], next_goal)
            if 0 <= x < self.num_row <= y < self.num_col:
                grid_pos = self.convert_to_grid_xy([x, y])
                if self.grid[grid_pos[0]][grid_pos[1]] == '.':
                    if 0 < h < cost:
                        cost = h
                        move_to = [x, y]

        self.position = move_to
        steering_angle = self.get_steering_angle(self.position, move_to)
        while steering_angle != 0:
            if steering_angle > self.max_steering:
                policy.append(["{} {} {}".format(actions[0], self.max_steering, 0)])
                steering_angle -= self.max_steering
            elif steering_angle < -self.max_steering:
                policy.append(["{} {} {}".format(actions[0], -self.max_steering, 0)])
                steering_angle += self.max_steering
            else:
                dist = self.get_distance(self.position, move_to)
                policy.append(["{} {} {}".format(actions[0], steering_angle, dist)])
                steering_angle = 0

        return policy

    def get_steering_angle(self, current, target):
        steering_angle = atan2(target[1], target[0]) - atan2(current[1] - target[1], current[0] - target[0])
        steering_angle = self.angle_trunc(steering_angle)
        return steering_angle

    def no_wall(self, pos):
        result = True
        for i in range(len(moves)):
            x2 = pos[0] + moves[i][0] * int(robot_size * times / 2 + 1)
            y2 = pos[1] + moves[i][1] * int(robot_size * times / 2 + 1)
            grid_xy = self.convert_to_grid_xy([x2, y2])
            if grid_xy[0] < 0 or grid_xy[0] >= len(self.grid) or grid_xy[1] < 0 or grid_xy[1] >= len(self.grid[0]) \
                    or self.grid[grid_xy[0]][grid_xy[1]] == '#':
                result = False
        return result

    def get_drop_zone(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '@':
                    self.grid[i] = self.grid[i][0:j] + '.' + self.grid[i][j + 1:]
                    return [int(abs(-i - 0.5) * times), int((j + 0.5) * times)]
        return []

    @classmethod
    def smooth(cls, path, weight_data=0.5, weight_smooth=0.1, tolerance=0.000001):
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

    @classmethod
    def convert_to_grid_xy(cls, pos):
        return [int(pos[0] / times), int(pos[1] / times)]

    @classmethod
    def convert_to_result_xy(cls, pos):
        return [float(pos[1]) / times, -float(pos[0]) / times]

    @classmethod
    def convert_to_extend_grid_xy(cls, pos):
        return [int(abs(pos[0] * times)), int(abs(pos[1] * times))]

    @classmethod
    def heuristic(cls, a, b):
        d_x = a[0] - b[0]
        d_y = a[1] - b[1]
        return sqrt(d_x * d_x + d_y * d_y)

    @classmethod
    def cost(cls, a, b):
        d_x = a[0] - b[0]
        d_y = a[1] - b[1]
        return sqrt(d_x * d_x + d_y * d_y) + 1

    @classmethod
    def get_distance(cls, a, b):
        d_x = a[0] - b[0]
        d_y = a[1] - b[1]
        return sqrt(d_x * d_x + d_y * d_y)

    @classmethod
    def angle_trunc(cls, a):
        return ((a + pi) % (pi * 2)) - pi
