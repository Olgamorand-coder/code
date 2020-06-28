board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

current_player = "X"
winner = None
game_still_going = True


def display_board():
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])


def play_game():
    display_board()
    while game_still_going:
        handle_turn()
        display_board()
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner, "won")
    elif winner == None:
        print("Tie")



def check_if_game_over():
    global game_still_going
    check_winner(board)
    if winner == "X" or winner == "O":
        game_still_going = False
    elif "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
        game_still_going=False



def handle_turn():
    not_valid=True
    while not_valid:
        position=input("choose position")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8","9"]:
            position=input("choose position from 1-9")
        if position=="1":
            i,j=0,0
        elif position=="2":
            i,j=0,1
        elif position=="3":
            i,j=0,2
        elif position=="4":
            i,j=1,0
        elif position == "5":
            i,j=1,1
        elif position == "6":
            i,j=1,2
        elif position == "7":
            i,j=2,0
        elif position == "8":
            i,j=2,1
        elif position == "9":
            i,j=2,2
        if board[i][j]=="-":
            board[i][j] = current_player
            not_valid=False
        else:
            print("you can't go there, go again")


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_winner(game):
    global winner
    diag1 = 0
    diag2 = 0

    for i in range(len(game)):
        vertical = 0
        horizontal = 0
        for j in range(len(game[i])):
            # game[i][0] - первый элемент в строке
            if (game[i][j]!= "-") and (game[i][j] == game[i][0]):
                horizontal += 1
            # game[0][i] - первый элемент в столбце
            if (game[j][i]!= "-") and (game[j][i] == game[0][i]):
                vertical += 1
            if i == j:
                # game[0][0] - первый элемент в дагонали 1
                if game[i][j] !="-" and game[i][j] == game[0][0]:
                    diag1 += 1
                # game[0][len(game)-1] - первый элемент в дагонали 2
                if game[i][len(game) - 1 - j] !="-" and game[i][len(game) - 1 - j] == game[0][len(game) - 1]:
                    diag2 += 1
        # Внутри цикла, т.к. проверяем каждую строку
        if horizontal == 3:
            winner = game[i][0]
            return game[i][0]
        if vertical == 3:
            winner = game[0][i]
            return game[0][i]
    # Вне цикла, т.к. результат по диагоналям будет известен только после полного прохода по полю
    if diag1 == 3:
        winner = game[0][0]
        return game[0][0]
    if diag2 == 3:
        winner = game[0][len(game) - 1]
        return game[0][len(game) - 1]

    return None

play_game()
