class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g  # cost from start node to current node
        self.h = h  # heuristic cost from current node to goal node

    def __repr__(self):
        return f"Node({self.state}, {self.action}, g={self.g}, h={self.h})"

    def f(self):
        return self.g + self.h


class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.blank_position = self.find_blank_position()

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

    def find_blank_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j

    def move(self, direction):
        i, j = self.blank_position
        new_board = [row[:] for row in self.board]  

        if direction == "UP" and i > 0:
            new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
        elif direction == "DOWN" and i < self.size - 1:
            new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
        elif direction == "LEFT" and j > 0:
            new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        elif direction == "RIGHT" and j < self.size - 1:
            new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]
        else:
            return None

        return PuzzleState(new_board)

    def manhattan_distance(self, goal_state):
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                if value != 0:
                    goal_position = goal_state.find_position(value)
                    distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        return distance

    def find_position(self, value):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == value:
                    return i, j


def print_solution(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent

    for state in path:
        print_state(state)


def print_state(state):
    for row in state.board:
        print(row)
    print()


def solve_puzzle(initial_state, goal_state):
    open_list = [Node(initial_state, g=0, h=initial_state.manhattan_distance(goal_state))]
    closed_set = set()

    while open_list:
        open_list.sort(key=lambda x: x.f())
        current_node = open_list.pop(0)

        if current_node.state == goal_state:
            print("Solution found:")
            print_solution(current_node)
            return

        closed_set.add(current_node.state)

        for action in ["UP", "DOWN", "LEFT", "RIGHT"]:
            child_state = current_node.state.move(action)

            if child_state and child_state not in closed_set:
                
                child_node = Node(child_state, current_node, action, g=current_node.g + 1,
                                  h=child_state.manhattan_distance(goal_state))
                if not any(node for node in open_list if node.state == child_state and node.f() <= child_node.f()):
                    open_list.append(child_node)

    print("No solution found.")


initial_state = PuzzleState([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal_state = PuzzleState([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
solve_puzzle(initial_state, goal_state)
