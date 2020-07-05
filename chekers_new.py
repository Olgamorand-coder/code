board = [["X", "_", "X", "B", "X", "_", "X", "_"],
         ["_", "X", "B", "X", "_", "X", "_", "X"],
         ["X", "_", "X", "_", "X", "_", "X", "_"],
         ["_", "X", "_", "X", "_", "X", "_", "X"],
         ["X", "_", "X", "B", "X", "_", "X", "_"],
         ["W", "X", "W", "X", "W", "X", "W", "X"],
         ["X", "W", "X", "W", "X", "W", "X", "W"],
         ["W", "X", "W", "X", "W", "X", "W", "X"]]
current_player = "B"
adversary="W"

def display_board():
    print("  A", "B", "C", "D", "E", "F", "G", "H")
    print(1, *board[0])
    print(2, *board[1])
    print(3, *board[2])
    print(4, *board[3])
    print(5, *board[4])
    print(6, *board[5])
    print(7, *board[6])
    print(8, *board[7])
display_board()
column_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


def go_from(current_player):
    row = -1
    column = -1

    valid = False
    while not valid:
        try:
            to_column, to_row = str(input("choose where to go, print letter A-H, number 1-8:")).split(",")
        except ValueError:
            print("error! print a letter and a number separated by a comma")
            continue

        if check_move_input(to_column, to_row):
            row, column = parse_move(to_row, to_column)
            # check pawn color
            if board[row][column] == current_player:
                valid = True
            else:
                print ("Sorry, you can't go there")

    return row, column


def go_to(possible_moves):
    row = -1
    column = -1

    valid = False
    while not valid:
        try:
            to_column, to_row = str(input("choose where to go, print letter A-H, number 1-8:")).split(",")
        except ValueError:
            print("error! print a letter and a number separated by a comma")
            continue

        if check_move_input(to_column, to_row):
            row, column = parse_move(to_row, to_column)
            # check if pawn can go there
            if (row, column) in possible_moves:
                valid = True
            else:
                print ("Sorry, you can't go there")

    return row, column

# check if input data is valid
def check_move_input(column, row):
    valid = False
    if row in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        if column in column_dictionary:
            valid = True
        else:
            print("the letter is wrong")
    else:
        print("the number is wong")
    return valid


def parse_move(raw_column, raw_row):
    row = int(raw_row) - 1
    column = column_dictionary[raw_column]
    return row, column


#def handle_turn():

    #possible_moves = []
    #coordinates_from = go_from()
    #row_from, column_from = coordinates_from
    #if column_from <= 6:
        #if current_player=="W":
            #a_tuple = row_from - 1, column_from + 1
            #if board[row_from - 1][column_from + 1] == "_":
             #   possible_moves.append(a_tuple)
        #elif current_player=="B":
         #   a_tuple = row_from +1, column_from + 1
          #  if board[row_from + 1][column_from + 1] == "_":
           #     possible_moves.append(a_tuple)
    #if column_from >= 1:
     #   if current_player == "W":
      #      a_tuple2 = row_from - 1, column_from - 1
       #     if board[row_from - 1][column_from - 1] == "_":
        #        possible_moves.append(a_tuple2)
        #elif current_player == "B":
         #   a_tuple2 = row_from + 1, column_from - 1
          #  if board[row_from + 1][column_from - 1] == "_":
           #     possible_moves.append(a_tuple2)


    #coordinates_to = go_to()
    #row_from, column_from = coordinates_from
    #row_to, column_to = coordinates_to

    #valid = False
   # while not valid:

    #    if coordinates_to in possible_moves:
     #       board[row_from][column_from] = "_"
      #      board[row_to][column_to] = current_player
       #     valid=True
       # else:
        #    print("you can't go there")
         #   handle_turn()

    #display_board()

def check_boarders(row, column):
    return 0 <= row <= 7 and 0 <= column <= 7


def possible_moves(row_from, column_from):
    possible_moves = []

    move_direction = -1
    if board[row_from][column_from] == "B":
        move_direction = 1

    r_tuple = int(row_from + move_direction), int(column_from + 1)
    l_tuple = int(row_from + move_direction), int(column_from - 1)

    if check_boarders(r_tuple[0], r_tuple[1]):
        if board[r_tuple[0]][r_tuple[1]] == "_":
            possible_moves.append(r_tuple)

    if check_boarders(l_tuple[0], l_tuple[1]):
        if board[l_tuple[0]][l_tuple[1]] == "_":
            possible_moves.append(l_tuple)

    return possible_moves
#print(possible_moves(2,3))



def possible_beat(from_row, from_column):
    possible_beats = []
    if board[from_row][from_column] == current_player:
        if from_row <= 6 and from_column <= 5:
            try:
                if board[from_row + 1][from_column + 1] == adversary:
                    try:
                        if board[from_row + 2][from_column + 2] == "_":
                            beats_tuple = (from_row + 2, from_column + 2)
                            possible_beats.append(beats_tuple)
                    except IndexError:
                        pass
            except IndexError:
                pass
        try:
            if board[from_row + 1][from_column - 1] == adversary:
                if from_row <= 6 and from_column >= 2:
                    try:
                        if board[from_row + 2][from_column - 2] == "_":
                            beats_tuple = (from_row + 2, from_column - 2)
                            possible_beats.append(beats_tuple)
                    except IndexError:
                        pass
        except IndexError:
            pass

        try:
            if board[from_row - 1][from_column + 1] == adversary:
                if from_row >= 1 and from_column <= 5:
                    try:
                        if board[from_row - 2][from_column + 2] == "_":
                            beats_tuple = (from_row - 2, from_column + 2)
                            possible_beats.append(beats_tuple)
                    except IndexError:
                        pass
        except IndexError:
            pass

        try:
            if board[from_row - 1][from_column - 1] == adversary:
                if from_row >= 1 and from_column >= 2:
                    try:

                        if board[from_row - 2][from_column - 2] == "_":
                            beats_tuple = (from_row - 2, from_column - 2)
                            possible_beats.append(beats_tuple)
                    except IndexError:
                        pass
        except IndexError:
            pass


    return possible_beats

def handle_turn():
    from_coord=go_from(current_player)
    row_from, column_from=from_coord

    possible_goes=possible_moves(row_from, column_from)
    # possible_beats=possible_beat(row_from, column_from)
    to_coord=go_to(possible_goes)
    row_to, column_to=to_coord

    valid = False
    while not valid:
        if to_coord in possible_goes or to_coord in possible_beats:
            if to_coord in possible_goes:
                board[row_from][column_from] = "_"
                board[row_to][column_to] = current_player
                valid = True

            elif row_from-row_to==2:
                if column_from-column_to==2:
                    board[row_from-1][column_from-1]="_"
                elif column_from-column_to==-2:
                    board[row_from - 1][column_from +1] = "_"
                board[row_from][column_from] = "_"
                board[row_to][column_to] = current_player
                valid = True
            elif row_from-row_to==-2:
                if column_from-column_to==2:
                    board[row_from+1][column_from-1]="_"
                elif column_from-column_to==-2:
                    board[row_from+1][column_from+1]="_"
                board[row_from][column_from] = "_"
                board[row_to][column_to] = current_player

                valid = True


        else:
            print("you can't go there")
            handle_turn()
    display_board()
handle_turn()

def game():
    while not win():
        while not check_ok:
            move = input_move()
            check_ok = check_move()
        do_move(move)
        switch_player()


