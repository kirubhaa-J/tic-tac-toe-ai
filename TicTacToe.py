
import math


board = [" " for _ in range(9)]


def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")


def check_winner(player):
    win_cond = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_cond)


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def play_game():
    print("Play Tic-Tac-Toe!\nYou = X | AI = O")
    print_board()

    while True:
        try:
            user_move = int(input("Enter your move (1–9): ")) - 1
        except ValueError:
            print("Invalid input! Please enter a number 1–9.")
            continue

        if 0 <= user_move < 9 and board[user_move] == " ":
            board[user_move] = "X"
        else:
            print("Invalid move. Try again.")
            continue

        print_board()

        if check_winner("X"):
            print("You win! 🎉")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("Opponent thinking...\n")
        ai = best_move()
        board[ai] = "O"
        print_board()

        if check_winner("O"):
            print("AI wins! 🤖")
            break
        if is_draw():
            print("It's a draw!")
            break

play_game()             

