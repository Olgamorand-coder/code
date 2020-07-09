def init_board():
    return [["I","I","I","I","I", "I","I","I","I","I","I","I"],
         ["I", "I","I","I","I","I","I","I","I","I","I","I"],
         ["I","I","X", "_", "X", "_", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "b", "X", "_", "X", "_", "X","I","I"],
         ["I","I","X", "_", "X", "_", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "_", "X", "w", "X", "_", "X","I","I"],
         ["I","I","X", "b", "X", "_", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "_", "X", "_", "X", "_", "X","I","I"],
         ["I","I","X", "_", "X", "_", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "_", "X", "_", "X", "_", "X","I","I"],
         ["I", "I","I","I","I","I","I","I","I","I","I","I"],
         ["I", "I","I","I","I","I","I","I","I","I","I","I"]]



def display_board(board):
    print("  A", "B", "C", "D", "E", "F", "G", "H")# capitalsmall letters
    print(1, *board[2][2:10])
    print(2, *board[3][2:10])
    print(3, *board[4][2:10])
    print(4, *board[5][2:10])
    print(5, *board[6][2:10])
    print(6, *board[7][2:10])
    print(7, *board[8][2:10])
    print(8, *board[9][2:10])



column_dictionary = {"A": 2, "B": 3, "C": 4, "D": 5, "E": 6, "F": 7, "G": 8, "H": 9}

def check_move_input(letter, number):
    valid=False
    if number in ["1","2","3","4","5","6","7","8"]:

        if letter in column_dictionary:
            valid=True
        else:
            print ("Error, the letter is wrong")
    else:
        print("Error, incorrect input")
    return valid

def parse_move(number, letter):
    row=int(number)+1
    column=column_dictionary[letter]
    return row, column

def check_borders(row, column, board):
    return board[row][column]!="I"

def possible_moves(row_from, column_from, board):

    possible_moves_list=[]
    move_direction=1
    if board[row_from][column_from]=="w":
        move_direction=-1

    r_tuple=int(row_from+move_direction), int(column_from+1)
    l_tuple=int(row_from+move_direction), int(column_from-1)
    if check_borders(r_tuple[0], r_tuple[1], board):
        if board[r_tuple[0]][r_tuple[1]]=="_":
            possible_moves_list.append(r_tuple)
    if check_borders(l_tuple[0], l_tuple[1], board):
        if board[l_tuple[0]][l_tuple[1]]=="_":
            possible_moves_list.append(l_tuple)
    return possible_moves_list






def get_beat_move(row_from, col_from, row_direc, col_direc, player, board):
    adversary = ""
    if player == "w":
        adversary = "b"
    elif player == "b":
        adversary = "w"
    beat_tuple=row_from+2*row_direc, col_from+2*col_direc
    if board[row_from+row_direc][col_from+col_direc]==adversary:
        if board[beat_tuple[0]][beat_tuple[1]]=="_":
            return beat_tuple

def possible_beat(row_from, column_from, player, board):
    possible_beats_list=[]
    # check if can beat left down
    left_up=get_beat_move(row_from, column_from, -1, -1, player, board)
    right_up=get_beat_move(row_from, column_from, -1, 1, player, board)
    left_down=get_beat_move(row_from, column_from, 1, -1, player, board)
    right_down=get_beat_move(row_from, column_from, 1, 1, player, board)
    if left_up!=None:
        possible_beats_list.append(left_up)
    if right_up!=None:
        possible_beats_list.append(right_up)
    if left_down!=None:
        possible_beats_list.append(left_down)
    if right_down!=None:
        possible_beats_list.append(right_down)
    return possible_beats_list


def go_from(player, board):

    row=-1
    column=-1
    valid=False
    while not valid:

        print(player+"'s turn")
        try:
            from_column, from_row=str(input("Choose a pawn. Print a letter and a number separated by comma")).split(",")
            from_column=from_column.upper()

        except ValueError:
            print("Error, you should print a letter and a number")
            continue
        if check_move_input(from_column, from_row):
            row, column=parse_move(from_row, from_column)
            if board[row][column]==player:
                valid=True
            else:
                print("Error, you should choose your pawn")
    return row, column

def go_to(possible_moves_list, possible_beats_list):
    row=-1
    column=-1
    valid=False
    while not valid:
        try:
            to_column, to_row=str(input("Choose where to go. Print a letter and a number separated by comma")).split(",")
            to_column=to_column.upper()
        except ValueError:
            print("Error. You should print a letter and a number")
            continue
        if check_move_input(to_column, to_row):
            row, column=parse_move(to_row, to_column)
            if (row, column) in possible_moves_list or (row, column) in possible_beats_list :
                valid=True
            else:
                print("You can't go there")
    return row, column

def handle_move(row_from, column_from, row_to, column_to, current_player, board):

    possible_moves_list=possible_moves(row_from, column_from, board)
    if (row_to, column_to) in possible_moves_list:
        board[row_from][column_from]="_"
        board[row_to][column_to]=current_player
        display_board(board)
    else:
        print("sorry, you can't go there")

#function serves to find an adversary when it's beaten
def find_killed_adversary_coord(row_from, column_from, row_to, column_to):

    adversary_row=-1
    adversary_column=-1
    if row_from-row_to==2:
        adversary_row=row_from-1
    elif row_from-row_to==-2:
        adversary_row=row_from+1
    if column_from-column_to==2:
        adversary_column=column_from-1
    elif column_from-column_to==-2:
        adversary_column=column_from+1
    return adversary_row, adversary_column


def handle_beat(row_from, column_from, row_to, column_to, current_player, beaten, board):
    # counter how many Ws and Bs were beaten


    possible_beats_list=possible_beat(row_from, column_from, current_player, board)
    # we find the killed adversary
    adversary_row, adversary_column=find_killed_adversary_coord(row_from, column_from, row_to, column_to)
    if (row_to, column_to) in possible_beats_list:
        if board[adversary_row][adversary_column]=="w":
            beaten["w"]+=1
        elif board[adversary_row][adversary_column]=="b":
            beaten["b"]+=1
        # we replace the current_player position with "_"
        board[row_from][column_from] = "_"
        #we put current_player on the valid position
        board[row_to][column_to] = current_player
        # we replace the killed adversary with "_"
        board[adversary_row][adversary_column]="_"
        #we count the number of beaten adversaries for each player
    display_board(board)


#checks if there is a pawn that can beat, but doesn't do it, this pawn goes to beaten and replaced by "_"
def fuk_check(board, current_player, possible_beats_list):
    #check every pawn of the current player on the board if it has possible beats
    for cur_pawn_row in range(len(board)):
        for cur_pawn_column in range(len(board[cur_pawn_row])):
            if board[cur_pawn_row][cur_pawn_column]==current_player:
                pos_beats_lst=possible_beat(cur_pawn_row, cur_pawn_column, current_player, board)
                #if the list is not empty, we return the row and the column of this pawn
                if len(pos_beats_lst)>0:
                    return cur_pawn_row, cur_pawn_column
    return False





def fuk_move(cur_pawn_row, cur_pawn_column, pawns_beaten, board):
    cur_pawn=board[cur_pawn_row][cur_pawn_column]
    pawns_beaten[cur_pawn] += 1
    board[cur_pawn_row][cur_pawn_column] = "_"
    display_board(board)

def check_winner(beaten):

    if beaten["w"]==12:
        return "b"
    elif beaten["b"]==12:
        return "w"
    return ""

def game_over( beaten_pawns):
    winner=check_winner(beaten_pawns)
    if winner!="" or tie(winner, beaten_pawns):
            return True

def tie(the_winner, beaten):
    if the_winner=="" and beaten["b"]==11 and beaten["w"]==11:
        return True

def switch_player(player):
    if player=="w":
        player="b"
    elif player=="b":
        player="w"
    return player

def game():
    board=init_board()
    beaten_pawns={"b":10, "w":11}

    winner=check_winner(beaten_pawns)
    current_player = "w"
    display_board(board)
    game_stopped=False
    while not game_stopped:
        row_from, column_from = go_from(current_player, board)
        possible_moves_list = possible_moves(row_from, column_from, board)
        possible_beats_list = possible_beat(row_from, column_from, current_player, board)
        row_to, column_to = go_to(possible_moves_list, possible_beats_list)
        #if fuk_check(board, current_player, possible_beats_list) != False:
            #cur_pawn_row, cur_pawn_column = fuk_check(board, current_player, possible_beats_list)
        if (row_to, column_to) in possible_moves_list:
            handle_move(row_from, column_from, row_to, column_to, current_player, board)
            #fuk_move(cur_pawn_row,cur_pawn_column, beaten_pawns, board)
            #print("Fuk move, be more attentive next time!")

        elif (row_to, column_to) in possible_beats_list:
            beat_possible = True
            while beat_possible:
                handle_beat(row_from, column_from, row_to, column_to, current_player, beaten_pawns, board)
                row_from = row_to
                column_from = column_to
                possible_beats_list = possible_beat(row_from, column_from, current_player, board)
                if len(possible_beats_list) > 0:
                    row_to, column_to = go_to(possible_moves_list, possible_beats_list)
                    if (row_to, column_to) not in possible_beats_list:
                        beat_possible = False
                else:
                    beat_possible = False
        game_stopped=game_over(beaten_pawns)
        current_player=switch_player(current_player)


    else:
        if not tie(winner, beaten_pawns):
            winner=check_winner(beaten_pawns)
            print(winner+" Wins!")
        else:
            print("Tie")


def become_w_queen(board):

    for i in range(len(board[2])):
        if board[2][i]=="w":
            board[2][i]="W"
            display_board(board)

def become_b_queen(board):
    for i in range(len(board[9])):
        if board[9][i]=="b":
            board[9][i]="B"
            display_board(board)

def get_queen_move(row_from, col_from, row_direc, col_direc, i, board):
    queen_move_tuple=row_from+i*row_direc, col_from+i*col_direc
    try:
        if board[row_from + i*row_direc][col_from + i*col_direc] == "_":
            return queen_move_tuple
    except IndexError:
        pass

def possible_queen_moves(row_from, column_from, board):
    possible_queen_moves_list=[]
    for i in range(1,8):
        left_up = get_queen_move(row_from, column_from, -1, -1, i)
        if left_up!=None:
            if board[left_up[0]][left_up[1]]=="_":
                possible_queen_moves_list.append(left_up)


    for i in range(1, 8):
        right_up = get_queen_move(row_from, column_from, -1, 1, i)
        if right_up!=None:
            if board[right_up[0]][right_up[1]]=="_":
                possible_queen_moves_list.append(right_up)
            else:
                break
    for i in range(1, 8):
        left_down = get_queen_move(row_from, column_from, 1, -1, i)
        if left_down!=None:
            if board[left_down[0]][left_down[1]]=="_":
                possible_queen_moves_list.append(left_down)
            else:
                break
    for i in range(1, 8):
        right_down = get_queen_move(row_from, column_from, 1, 1, i)
        if right_down!=None:
            if board[right_down[0]][right_down[1]]=="_":
                possible_queen_moves_list.append(right_down)
            else:
                break

    return possible_queen_moves_list



game()