def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(row, col, slashCode, backslashCode,
           rowLookup, slashCodeLookup,
           backslashCodeLookup):
    if (slashCodeLookup[slashCode[row][col]] or
            backslashCodeLookup[backslashCode[row][col]] or
            rowLookup[row]):
        return False
    return True

def solveNQueensUtil(board, col, slashCode, backslashCode,
                     rowLookup, slashCodeLookup,
                     backslashCodeLookup):

    global count
    if (col >= N):
        count += 1
        printSolution(board)
        print()  # Separate solutions visually
        return True
    for i in range(N):
        if (isSafe(i, col, slashCode, backslashCode,
                   rowLookup, slashCodeLookup,
                   backslashCodeLookup)):

            board[i][col] = 1
            rowLookup[i] = True
            slashCodeLookup[slashCode[i][col]] = True
            backslashCodeLookup[backslashCode[i][col]] = True

            if (solveNQueensUtil(board, col + 1,
                                 slashCode, backslashCode,
                                 rowLookup, slashCodeLookup,
                                 backslashCodeLookup)):
                # Do not reset the board here, as we want to continue exploring other solutions
                # Resetting the board should happen outside the recursive call
                # board[i][col] = 0
                # rowLookup[i] = False
                # slashCodeLookup[slashCode[i][col]] = False
                # backslashCodeLookup[backslashCode[i][col]] = False
                pass

            # Reset board for backtracking
            board[i][col] = 0
            rowLookup[i] = False
            slashCodeLookup[slashCode[i][col]] = False
            backslashCodeLookup[backslashCode[i][col]] = False

    return False

def solveNQueens(N):
    global count
    count = 0
    board = [[0 for i in range(N)]
             for j in range(N)]

    # helper matrices
    slashCode = [[0 for i in range(N)]
                 for j in range(N)]
    backslashCode = [[0 for i in range(N)]
                     for j in range(N)]

    rowLookup = [False] * N

    x = 2 * N - 1
    slashCodeLookup = [False] * x
    backslashCodeLookup = [False] * x

    # initialize helper matrices
    for rr in range(N):
        for cc in range(N):
            slashCode[rr][cc] = rr + cc
            backslashCode[rr][cc] = rr - cc + N - 1

    solveNQueensUtil(board, 0, slashCode, backslashCode,
                     rowLookup, slashCodeLookup,
                     backslashCodeLookup)

    if count == 0:
        print("Solution does not exist")
        return False
    else:
        print("Total solutions:", count)
        return True

N = 8  # Change N to whatever value you want
solveNQueens(N)
