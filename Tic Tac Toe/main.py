board = [" "," "," ",
        " "," "," ",
        " "," "," "]

win = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,4,8],
    [2,4,6],
    [0,3,6],
    [1,4,7],
    [2,5,8]
]

def check_winner(board,symbol):
    for combination in win:
        if board[combination[0]]==board[combination[1]]==board[combination[2]]==symbol:
            return True
    return False

def check_draw(board):
    if " " not in board:
        return True
    return False

def display_board(board):
    return f"""
 {board[0]} | {board[1]} | {board[2]}
---+---+---
 {board[3]} | {board[4]} | {board[5]}
---+---+---
 {board[6]} | {board[7]} | {board[8]}
"""

current_player = "X"
game = True

def validate_input(x,symbol,board):
    if board[x-1]!=" ":
        return False
    else:
        board[x-1] = symbol
        return True

player1 = input("Enter Player 1 Name: ")
player2 = input("Enter Player 2 Name: ")
turn = player1
scores = {
    "X": 0,
    "O": 0,
    "Draw": 0
}

def reset_scores(scores):
    scores["X"] = 0
    scores["O"] = 0
    scores["Draw"] = 0

def reset_board():
    return [" "] * 9

def play_game(board,player1,player2,scores):

    play_again = True

    while play_again:

        board = reset_board()
        current_player = "X"
        turn = player1

        while game:
            try:
                a = int(input(f"{turn}'s Turn(1-9, 0 to Exit): "))
                if 1 <= a <= 9:
                    validation = validate_input(a,current_player,board)
                    if validation:
                        print(display_board(board))
                        if check_winner(board,current_player):
                            scores[current_player] += 1
                            print(f"{current_player} Wins!!")
                            print(f"ScoreBoard")
                            print(f"------------")
                            print(f"{player1}: {scores['X']}")
                            print(f"{player2}: {scores['O']}")
                            print(f"Draws: {scores['Draw']}")
                            a = input("Play Again(y/n)? ")
                            if a != "y":
                                reset_scores(scores)
                                return
                            break
                        else:
                            if not check_draw(board):
                                current_player = "O" if current_player == "X" else "X"
                                turn = player2 if turn == player1 else player1
                            else:
                                print("Game Draw")
                                scores["Draw"] += 1
                                a = input("Play Again(y/n)? ")
                                if a != "y":
                                    reset_scores(scores)
                                    return
                                break
                    else:
                        continue
                elif a == 0:
                    print("Game Stopped")
                    reset_scores(scores)
                    play_again = False
                    break
                else:
                    print("Please Enter Between 1-9")
            except ValueError:
                print("Please Enter Integer")

play_game(board,player1,player2,scores)