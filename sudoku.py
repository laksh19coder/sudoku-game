#==============================#
#ADVANCED SUDOKU SOLVER
#==============================#

import time

#Global step counter
steps = 0

#----------------------------------#
#PRINT BOARD
#----------------------------------#

def print_board(board):
    for row in board:
        print(row)
#------------------------------#
# FIND EMPTY CELL
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None
#-------------------------------#
#CHECK VALID MOVE
def is_valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and i!= col:
            return False
    for i in range(9):
        if board[i][col] == num and i!= row:
            return False
    box_x = col//3
    box_y = row//3
    for i in range(box_y*3+3):
        for j in range(box_x*3+3):
            if board[i][j] == num and(i,j) != pos:
                return False
    return True
#---------------------------------------------#
#VALIDATE INITIAL BOARD#
def validate_board(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0
                if not is_valid(board, num, (row, col)):
                    return False
                board[row][col] = num
    return True

#--------------------------------------#
#DETECT DIFFICULTY
def detect_difficulty(board):
    empty_cells = 0
    for row in board:
        empty_cells += row.count(0)
    if empty_cells < 30:
        return "Easy"
    elif empty_cells < 50:
        return "Medium"
    else:
        return "Hard"
#--------------------------------------#
#SOLVE USING BACKTRACKING#
def solve(board):
    global steps
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1,10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            steps += 1
            print(f"Trying {num} at position ({row},{col})")
            if solve(board):
                return True
            board[row][col] = 0
            print(f" Backtracking from ({row},{col})")
    return False
#--------------------------------------------#
#USER INPUT#
def input_board():
    board = []
    print("\nEnter Sudoku row by Row")
    print("Use 0 for empty spaces\n")
    for i in range(9):
        while True:
            row = input(f"Enter row {i+1}: ").split()
            if len(row) != 9:
                print("Please enter exactly 9 numbers")
            else:
                row = [int(num) for num in row]
                board.append(row)
                break
    return board

#=============================================#
# MAIN PROGRAM#
print("================================")
print("      ADVNACED SUDOKU SOLVER       ")
board = input_board()
if not validate_board(board):
    print("\nInvalid Sudoku Puzzle")
else:
    print("\nOriginal Sudoku: \n")
    print_board(board)
    difficulty = detect_difficulty(board)
    print(f"\nDifficulty Level: {difficulty}")

    start_time = time.time()
    if solve(board):
        end_time = time.time()
        print("\nSolved Sudoku:\n")
        print_board(board)
        print(f"\nTotal steps: {steps}")
        print(f"Solved in {end_time - start_time: .2f} seconds")
    else:
        print("\nNo Solution Exists")
