import random

# Constants
SIZE = 4

# Initialize the board
board = [[0 for x in range(SIZE)] for y in range(SIZE)]

# Function to add a random number to the board
def add_random_number():
    x = random.randint(0, SIZE-1)
    y = random.randint(0, SIZE-1)
    while board[x][y] != 0:
        x = random.randint(0, SIZE-1)
        y = random.randint(0, SIZE-1)
    board[x][y] = 2

# Function to move the tiles
def move_tiles(direction):
    if direction == "up":
        for x in range(SIZE):
            for y in range(SIZE):
                if board[x][y] != 0:
                    for i in range(x, 0, -1):
                        if board[i-1][y] == 0:
                            board[i-1][y] = board[i][y]
                            board[i][y] = 0
                        elif board[i-1][y] == board[i][y]:
                            board[i-1][y] *= 2
                            board[i][y] = 0
    elif direction == "down":
        for x in range(SIZE-1, -1, -1):
            for y in range(SIZE):
                if board[x][y] != 0:
                    for i in range(x, SIZE-1):
                        if board[i+1][y] == 0:
                            board[i+1][y] = board[i][y]
                            board[i][y] = 0
                        elif board[i+1][y] == board[i][y]:
                            board[i+1][y] *= 2
                            board[i][y] = 0
    elif direction == "left":
        for x in range(SIZE):
            for y in range(SIZE):
                if board[x][y] != 0:
                    for i in range(y, 0, -1):
                        if board[x][i-1] == 0:
                            board[x][i-1] = board[x][i]
                            board[x][i] = 0
                        elif board[x][i-1] == board[x][i]:
                            board[x][i-1] *= 2
                            board[x][i] = 0
    elif direction == "right":
        for x in range(SIZE):
            for y in range(SIZE-1, -1, -1):
                if board[x][y] != 0:
                    for i in range(y, SIZE-1):
                        if board[x][i+1] == 0:
                            board[x][i+1] = board[x][i]
                            board[x][i] = 0
                        elif board[x][i+1] == board[x][i]:
                            board[x][i+1] *= 2
                            board[x][i] = 0

# Function to print the board
def print_board():
    for x in range(SIZE):
        for y in range(SIZE):
            print(board[x][y], end="\t")
        print()

# Main game loop
while True:
    add_random_number()
    print_board()
    direction = input("Enter direction (up, down, left, right): ")
    move_tiles(direction)

