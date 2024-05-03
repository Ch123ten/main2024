def createBoard(size):
    board = [[0]*size for _ in range(size)]
    return board

def isSafe(board, row, col):
    size = len(board)
    for i in range(size):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    # up left
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i-=1
        j-=1
    
    # up right
    i, j = row, col
    while i >= 0 and j < size:
        if board[i][j] == 1:
            return False
        i-=1
        j+=1
    
    # down right
    i, j = row, col
    while i < size and j < size:
        if board[i][j] == 1:
            return False
        i+=1
        j+=1
    
    # down left
    i, j = row, col
    while i < size and j >= 0:
        if board[i][j] == 1:
            return False
        i+=1
        j-=1
    return True

def placeQueen(board, row):
    size = len(board)
    if row == size:
        printBoard(board)
        return True
    for i in range(size):
        if isSafe(board, row, i):
            board[row][i] = 1
            placeQueen(board, row+1)
            board[row][i] = 0

def printBoard(board):
    global solution
    solution+=1
    print(f"Solution {solution} : ")
    for i in board:
        for j in i:
            print(j, end=' ')
        print()
    print()


solution = 0
size = int(input("Enter the size of Chess Board : "))
board = createBoard(size)
placeQueen(board, 0)
'''





# This is for Branch and bound, and above is for backtracking

def createBoard(size):
    return [[0]*size for _ in range(size)]

solution = 0

def printBoard(board):
    global solution
    solution += 1
    print(f"Solution {solution} : ")
    for i in board:
        for j in i:
            print(j, end=' ')
        print()
    print()

def placeQueen(matrix, row, col = None, ndig = None, rdig = None):
    size = len(matrix)
    if row == size:
        printBoard(matrix)
        return
    if not col:
        col = [True]*size
        ndig = [True]*(2*size - 1)
        rdig = [True]*(2*size - 1)
    for i in range(size):
        if col[i] and ndig[row+i] and rdig[row-i+size-1]:
            matrix[row][i] = 1
            col[i] = False
            ndig[row+i] = False
            rdig[row-i+size-1] = False
            placeQueen(matrix, row+1, col, ndig, rdig)
            matrix[row][i] = 0
            col[i] = True
            ndig[row+i] = True
            rdig[row-i+size-1] = True

size = int(input("Enter the size of Chess Board : "))
board = createBoard(size)
placeQueen(board, 0)
'''
