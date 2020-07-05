board = [["I","I","I","I","I", "I","I","I","I","I","I","I"],
         ["I", "I","I","I","I","I","I","I","I","I","I","I"],
         ["I","I","X", "_", "X", "_", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "_", "X", "_", "X", "_", "X","I","I"],
         ["I","I","X", "_", "X", "_", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "_", "X", "_", "X", "_", "X","I","I"],
         ["I","I","X", "_", "X", "_", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "_", "X", "_", "X", "_", "X","I","I"],
         ["I","I","X", "_", "X", "B", "X", "_", "X", "_","I","I"],
         ["I","I","_", "X", "W", "X", "_", "X", "_", "X","I","I"],
         ["I", "I","I","I","I","I","I","I","I","I","I","I"],
         ["I", "I","I","I","I","I","I","I","I","I","I","I"]]
game_still_going=True
current_player = "W"
adversary="B"
Ws_beaten=11
Bs_beaten=11
winner=""
def display_board():
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

def check_borders(row, column):
    return board[row][column]!="I"


#def check_if_valid_pawn(row_from, column_from):
 #   if board[row_from][column_from]==current_player:
  #      return True
   # else:
    #    print("Error, you should choose your pawn")

def possible_moves(row_from, column_from):

    possible_moves_list=[]
    move_direction=1
    if board[row_from][column_from]=="W":
        move_direction=-1

    r_tuple=int(row_from+move_direction), int(column_from+1)
    l_tuple=int(row_from+move_direction), int(column_from-1)
    if check_borders(r_tuple[0], r_tuple[1]):
        if board[r_tuple[0]][r_tuple[1]]=="_":
            possible_moves_list.append(r_tuple)
    if check_borders(l_tuple[0], l_tuple[1]):
        if board[l_tuple[0]][l_tuple[1]]=="_":
            possible_moves_list.append(l_tuple)
    return possible_moves_list


def possible_beat(row_from, column_from):
    possible_beats_list=[]
    # check if can beat left down

    beat_left_down_tuple=row_from+2,column_from-2
    #check if doesn't go beyond borders
    if check_borders(beat_left_down_tuple[0], beat_left_down_tuple[1]):
        #check if there if an adversary
        if board[row_from+1][column_from-1]==adversary:
            #check if the space is empty
            if board[row_from+2][column_from-2]=="_":
                possible_beats_list.append(beat_left_down_tuple)

    beat_right_down_t=row_from+2, column_from+2
    if check_borders(beat_right_down_t[0], beat_right_down_t[1]):
        if board[row_from + 1][column_from + 1] == adversary:
            if board[row_from + 2][column_from + 2] =="_":
                possible_beats_list.append(beat_right_down_t)

    beat_left_up_t=row_from-2, column_from-2
    if check_borders(beat_left_up_t[0], beat_left_up_t[1]):
        if board[row_from - 1][column_from - 1] == adversary:
            if board[row_from-2][column_from-2]=="_":
                possible_beats_list.append(beat_left_up_t)

    beat_right_up_t=row_from-2, column_from+2
    if check_borders(beat_right_up_t[0], beat_right_up_t[1]):
        if board[row_from - 1][column_from +1] == adversary:
            if board[row_from - 2][column_from + 2] == "_":
                possible_beats_list.append(beat_right_up_t)

    return possible_beats_list
def go_from():
    row=-1
    column=-1
    valid=False
    while not valid:
        print(current_player+"'s turn")
        try:
            from_column, from_row=str(input("Chaoose a pawn. Print a letter and a number separated by comma")).split(",")

        except ValueError:
            print("Error, you should print a letter and a number")
            continue
        if check_move_input(from_column, from_row):
            row, column=parse_move(from_row, from_column)
            if board[row][column]==current_player:
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

def handle_move(row_from, column_from, row_to, column_to):

    possible_moves_list=possible_moves(row_from, column_from)
    if (row_to, column_to) in possible_moves_list:
        board[row_from][column_from]="_"
        board[row_to][column_to]=current_player
        display_board()
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


def handle_beat(row_from, column_from, row_to, column_to):
    # counter how many Ws and Bs were beaten
    global Ws_beaten
    global Bs_beaten

    possible_beats_list=possible_beat(row_from, column_from)
    # we find the killed adversary
    adversary_row, adversary_column=find_killed_adversary_coord(row_from, column_from, row_to, column_to)
    if (row_to, column_to) in possible_beats_list:
        if board[adversary_row][adversary_column]=="W":
            Ws_beaten+=1
        elif board[adversary_row][adversary_column]=="B":
            Bs_beaten+=1
        # we replace the current_player position with "_"
        board[row_from][column_from] = "_"
        #we put current_player on the valid position
        board[row_to][column_to] = current_player
        # we replace the killed adversary with "_"
        board[adversary_row][adversary_column]="_"
        #we count the number of beaten adversaries for each player
    display_board()





def check_winner():
    global winner
    if Ws_beaten==12:
        return "B"
    elif Bs_beaten==12:
        return "W"


def game_over():
    global game_still_going
    winner=check_winner()
    if winner!="" or tie():
            game_still_going=False


def tie():

    if winner=="" and Ws_beaten==11 and Bs_beaten==11:
        return True

def switch_player():
    global current_player
    global adversary
    if current_player=="W":
        current_player="B"
        adversary="W"
    elif current_player=="B":
        current_player="W"
        adversary="B"

def game():
    display_board()
    global game_still_going
    while game_still_going:
        row_from, column_from=go_from()
        possible_moves_list=possible_moves(row_from,column_from)
        possible_beats_list=possible_beat(row_from,column_from)
        row_to, column_to=go_to(possible_moves_list, possible_beats_list)
        if (row_to, column_to) in possible_moves_list:
            handle_move(row_from, column_from, row_to, column_to)
        elif (row_to, column_to) in possible_beats_list:
            handle_beat(row_from, column_from, row_to, column_to)
        game_over()

        switch_player()
    else:
        if not tie():
            winner=check_winner()
            print(winner+" Wins!")
        else:
            print("Tie")



game()




