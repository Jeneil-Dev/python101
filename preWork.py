from random import randrange


def displayBoard(board):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print("|   " + board[i][0] + "   |   " + board[i][1] + "   |   " + board[i][2] + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enterMove(board):
    move = input("Enter your move (1-9): ")

    if not move.isdigit():
        enterMove(board)
        return

    move = int(move)

    if move < 1 or move > 9:
        enterMove(board)
        return

    row = (move - 1) // 3
    col = (move - 1) % 3

    if board[row][col] in ["X", "O"]:
        enterMove(board)
    else:
        board[row][col] = "O"


def freeFields(board):
    free = []

    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                free.append((i, j))

    return free


def victoryFor(board, sign):
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


def drawMove(board):
    free = freeFields(board)

    if len(free) > 0:
        move = randrange(len(free))
        row, col = free[move]
        board[row][col] = "X"


board = [
    ["1", "2", "3"],
    ["4", "X", "6"],
    ["7", "8", "9"]
]


while True:
    displayBoard(board)

    enterMove(board)

    if victoryFor(board, "O"):
        displayBoard(board)
        print("You won!")
        break

    drawMove(board)

    if victoryFor(board, "X"):
        displayBoard(board)
        print("Computer won!")
        break