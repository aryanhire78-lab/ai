import math

AI = 'O'
HUMAN = 'X'

# Print Board
def print_board(b):
    for row in b:
        print(row)
    print()

# Check Winner
def evaluate(b):

    # Rows & Columns
    for i in range(3):

        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return 10 if b[i][0] == AI else -10

        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return 10 if b[0][i] == AI else -10

    # Diagonals
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return 10 if b[0][0] == AI else -10

    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return 10 if b[0][2] == AI else -10

    return 0

# Check Empty Spaces
def moves_left(b):
    for row in b:
        if ' ' in row:
            return True
    return False

# Minimax with Alpha-Beta
def minimax(board, depth, isMax, alpha, beta):

    score = evaluate(board)

    if score != 0:
        return score

    if not moves_left(board):
        return 0

    if isMax:
        best = -math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j] == ' ':
                    board[i][j] = AI

                    best = max(best,
                               minimax(board, depth+1, False, alpha, beta))

                    board[i][j] = ' '
                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break

        return best

    else:
        best = math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j] == ' ':
                    board[i][j] = HUMAN

                    best = min(best,
                               minimax(board, depth+1, True, alpha, beta))

                    board[i][j] = ' '
                    beta = min(beta, best)

                    if beta <= alpha:
                        break

        return best

# Best Move
def best_move(board):

    bestVal = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == ' ':

                board[i][j] = AI

                moveVal = minimax(board, 0, False,
                                  -math.inf, math.inf)

                board[i][j] = ' '

                if moveVal > bestVal:
                    move = (i, j)
                    bestVal = moveVal

    return move

# Main
board = [[' ']*3 for _ in range(3)]

while True:

    print_board(board)

    # Human Move
    r, c = map(int, input("Enter row col: ").split())
    board[r][c] = HUMAN

    if evaluate(board) == -10:
        print_board(board)
        print("You Win!")
        break

    if not moves_left(board):
        print("Draw!")
        break

    # AI Move
    ai = best_move(board)
    board[ai[0]][ai[1]] = AI

    if evaluate(board) == 10:
        print_board(board)
        print("AI Wins!")
        break

    if not moves_left(board):
        print("Draw!")
        break
