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
        

def Puzzle():
    queue = [ ]
    visited = [ ]
    queue. append( ( initial_state, 0)) # Including the number of steps taken

    while queue:
        curr_state, steps = queue.pop(0)

        print("Current state:")
        printState(curr_state)

        if curr_state == goal:
            print("Goal state reached in", steps, "steps.")
            printState(curr_state)
            return True

        i, j = findBlank(curr_state)
        
        visited.append(curr_state)

        for move_func in (moveLeft, moveRight, moveUp, moveDown):
            new_state, moved = move_func(deepcopy(curr_state))
            if moved and new_state not in visited:
                queue.append((new_state, steps + 1))
                visited.append(new_state)

    print("Goal state not reachable!")
    return False


Puzzle()