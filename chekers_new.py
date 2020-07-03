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
go_from=""
go_to=""
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
    valid = False
    while not valid:
        try:
            from_column, from_row = str( input("W starts. Choose a pawn, print letter A-H, number 1-8:")).split(",")
        except ValueError:
            print("error! print a letter and a number separated by a comma")
            continue

        if from_row in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            from_row=int(from_row)
            if from_column in column_dictionary:
                from_column_index = column_dictionary[from_column]
                if board[from_row - 1][from_column_index]== current_player:
                    #board[from_row - 1][from_column_index] = "_"
                    valid = True

                else:
                    print ("Sorry, you can't go there")
            else:
                print ("Incorrect input(letter). Choose letter A-H and number 1-8.")
        else:
            print("Incorrect input(number). Choose letter A-H and number 1-8")
    return from_row-1, from_column_index



def go_to():
    valid = False
    while not valid:
        try:
            to_column, to_row = str( input("choose where to go, print letter A-H, number 1-8:")).split(",")
        except ValueError:
            print("error! print a letter and a number separated by a comma")
            continue

        if to_row in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            to_row=int(to_row)
            if to_column in column_dictionary:
                to_column_index = column_dictionary[to_column]
                if board[to_row - 1][to_column_index]=="_":
                    #board[to_row - 1][to_column_index] = current_player
                    valid = True
                else:
                    print("not possible to go there")
            else:
                print("the letter is wrong")
        else:
            print("the number is wong")
    return to_row-1, to_column_index



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



def possible_moves(row_from, column_from):
    possible_moves = []

    if board[row_from][column_from] == "W":
        if row_from>=1 and column_from<=6:
            a_tuple = row_from - 1, column_from + 1
            if board[row_from - 1][column_from + 1] == "_":
                possible_moves.append(a_tuple)
        if row_from>=1 and column_from>=1:
            a_tuple2 = row_from - 1, column_from - 1
            if board[row_from - 1][column_from - 1] == "_":
                possible_moves.append(a_tuple2)

    elif board[row_from][column_from] == "B":
        if column_from <= 6 and row_from<=6:
            a_tuple = row_from + 1, column_from + 1
            if board[row_from + 1][column_from + 1] == "_":
                possible_moves.append(a_tuple)
        if column_from>=1 and row_from<=6:
            a_tuple2 = row_from + 1, column_from - 1
            if board[row_from + 1][column_from - 1] == "_":
                possible_moves.append(a_tuple2)
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
    to_coord=go_to()
    row_to, column_to=to_coord
    possible_goes=possible_moves(row_from, column_from)
    possible_beats=possible_beat(row_from, column_from)
    valid = False
    while not valid:
        if to_coord in possible_goes or to_coord in possible_beats:
            if row_from-row_to==abs(1):
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



