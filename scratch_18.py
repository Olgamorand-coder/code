board=["-","-","-","-","-","-","-","-","-",]
player="x"
winner=None
game_still_going=True

def play_game():
    show_board()
    while game_still_going:
        handle_turn()
        is_game_over()
        flip_player()
    print(find_winner())

def show_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def handle_turn():
    global player

    while game_still_going:
        valid_position=True
        while valid_position:
            position=input("chose position 1-9:")
            if position in ["1","2","3","4","5","6","7","8","9"]:
                position=int(position)
                if board[position-1]=="-":
                    board[position-1]=player
                    show_board()
                    flip_player()


                else:
                    print("can't go there")
            else:
                print("you should chose position 1-9")
def flip_player():
    global player
    if player=='x':
        player='o'
    elif player=='o':
        player='x'

def is_game_over():
    global game_still_going
    find_winner()

    if winner=="x" or winner=='o' or "-" not in board:
        game_still_going=False
        return True
    else:
        game_still_going=True
        return False

def find_winner():
    global winner
    # horizontal
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return(board[0])

    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return board[3]
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return board[6]
    # vertical
    elif board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return board[0]
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return board[1]
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return board[2]
    # diagonal
    elif board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return board[0]
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return board[2]
    else:
        winner = None
        return None
play_game()