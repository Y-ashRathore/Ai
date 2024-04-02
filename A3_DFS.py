from copy import deepcopy

initial_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

def printState(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=" ")
        print()
    print()

def findBlank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def moveLeft(state):
  i, j = findBlank(state)
  if j != 0:
    state[i][j], state[i][j - 1] = state[i][j - 1], state[i][j]
    return state, 1
  return state, 0

def moveRight(state):
    i, j = findBlank(state)
    if j == 2:
        return state, 0
    else:
        state[i][j], state[i][j + 1] = state[i][j + 1], state[i][j]
        return state, 1

def moveUp(state):
    i, j = findBlank(state)
    if i == 0:
        return state, 0
    else:
        state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]
        return state, 1

def moveDown(state):
    i, j = findBlank(state)
    if i == 2:
        return state, 0
    else:
        state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
        return state, 1

def isGoal(state):
    global goal
    return state == goal
        

def DFS(state, visited, steps):
  print("Current state:")
  printState(state)

  if state == goal:
    print("Goal state reached in", steps, "steps.")
    printState(state)
    return True

  visited.append(state)

  i, j = findBlank(state)

  for move_func in [moveLeft, moveRight, moveUp, moveDown]:
    new_state, moved = move_func(deepcopy(state))
    if moved and new_state not in visited:
        if DFS(new_state, visited, steps + 1):
           return True

  return False


def Puzzle_DFS():
    visited = []
    if DFS(initial_state, visited, 0):
        return True
    else:
        print("Goal state not reachable!")
        return False

Puzzle_DFS()
