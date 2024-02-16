import copy

final = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
initial = [[2, 3, 6], [1, -1, 5], [4, 7, 8]]

# Find position of blank tile
def find_blank(state):
    for i, row in enumerate(state):
        for j, tile in enumerate(row):
            if tile == -1:
                return i, j

# Perform move in given direction
def move(state, direction):
    blank_row, blank_col = find_blank(state)
    new_state = copy.deepcopy(state)
    if direction == "left" and blank_col > 0:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col - 1] = new_state[blank_row][blank_col - 1], new_state[blank_row][blank_col]
    elif direction == "up" and blank_row > 0:
        new_state[blank_row][blank_col], new_state[blank_row - 1][blank_col] = new_state[blank_row - 1][blank_col], new_state[blank_row][blank_col]
    elif direction == "right" and blank_col < 2:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col + 1] = new_state[blank_row][blank_col + 1], new_state[blank_row][blank_col]
    elif direction == "down" and blank_row < 2:
        new_state[blank_row][blank_col], new_state[blank_row + 1][blank_col] = new_state[blank_row + 1][blank_col], new_state[blank_row][blank_col]
    else:
        new_state = None
    return new_state

# Heuristic function using Manhattan distance
def heuristic(state, goal):
    return sum(abs(i//3 - j//3) + abs(i%3 - j%3) for i in range(3) for j in range(9) if state[i//3][i%3] != -1 and state[i//3][i%3] != goal[j//3][j%3])

# A* algorithm
def astar(initial, goal):
    queue = [(heuristic(initial, goal), 0, initial, [])]
    explored = set()
    while queue:
        _, cost, current_state, path = queue.pop(0)
        if current_state == goal:
            return path
        explored.add(tuple(map(tuple, current_state)))
        for direction in ["left", "up", "right", "down"]:
            new_state = move(current_state, direction)
            if new_state is not None and tuple(map(tuple, new_state)) not in explored:
                new_cost = cost + 1
                queue.append((new_cost + heuristic(new_state, goal), new_cost, new_state, path + [direction]))
        queue.sort(key=lambda x: x[0])

def print_steps(initial, steps):
    current_state = initial
    print("Initial State:")
    for row in current_state:
        print(row)
    print("")
    for i, step in enumerate(steps, 1):
        print("Step", i)
        current_state = move(current_state, step)
        for row in current_state:
            print(row)
        print("")

def main():
    steps = astar(initial, final)
    if steps is not None:
        print_steps(initial, steps)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
