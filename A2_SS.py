import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

def h(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                for m in range(3):
                    for n in range(3):
                        if state[i][j] == goal[m][n]:
                            distance += abs(i - m) + abs(j - n)
    return distance

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_children(node, goal):
    children = []
    for i in range(3):
        for j in range(3):
            if node.state[i][j] == 0:
                x, y = i, j
                break
    
    for dx, dy, move in [(0, 1, 'RIGHT'), (0, -1, 'LEFT'), (1, 0, 'DOWN'), (-1, 0, 'UP')]:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y):
            new_state = [row[:] for row in node.state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            child = PuzzleNode(new_state, node, move, node.depth + 1)
            child.cost = child.depth + h(new_state, goal)
            children.append(child)

    return children

def A_star(start, goal):
    start_node = PuzzleNode(start)
    start_node.cost = h(start, goal)
    frontier = [start_node]
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        if node.state == goal:
            return node
        explored.add(tuple(map(tuple, node.state)))
        children = get_children(node, goal)
        for child in children:
            if tuple(map(tuple, child.state)) not in explored:
                heapq.heappush(frontier, child)

    return None

def print_solution(solution):
  moves = []
  states = []
  while solution.parent:
      moves.append(solution.move)
      states.append(solution.state)
      solution = solution.parent
  moves.reverse()
  states.reverse()

  for move, state in zip(moves, states):
      print("Move:", move)
      for row in state:
          print(row)
      print()

start_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

solution_node = A_star(start_state, goal_state)

if solution_node:
    print_solution(solution_node)
else:
    print("No solution found.")