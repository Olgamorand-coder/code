from random import randint
table="_________"
first_row=[table[0],table[1],table[2]]
second_row=[table[3],table[4],table[5]]
third_row=[table[6],table[7],table[8]]
a=[]
a.append(first_row)
a.append(second_row)
a.append(third_row)


# functions

def display_table(table):
    print("---------\n|", table[0][0], table[0][1], table[0][2], "|")
    print("|", table[1][0], table[1][1], table[1][2], "|")
    print("|", table[2][0], table[2][1], table[2][2], "|")
    print("---------")


def user_turn(a, sign):
    not_valid = True
    while not_valid:
        try:
            coordinates = input("please enter the coordinates to make a move")
            coordinates = [int(i) for i in coordinates.split()]
            x, y = coordinates[0] - 1, coordinates[1] - 1
            if a[x][y] == "_":
                a[x][y] = sign
                not_valid = False
            elif a[x][y] == "X" or a[x][y] == "O":
                print("This cell is occupied! Choose another one!")

        except ValueError:
            print("You should enter numbers!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")
    return a

def sign():
    counter=0
    if counter%2==0:
        counter+=1
        return "X"
    else:
        counter+=1
        return "O"

def computer_turn(a, sign):
    not_valid = True
    while not_valid:
        x = randint(0, 2)
        y = randint(0, 2)
        if a[x][y] == "_":
            not_valid = False
            a[x][y] = sign
            print('Making move level \"easy\"')

    return a


def winner(a):
    if a[0][0] == a[1][1] == a[2][2] != "_":
        return a[0][0]
    elif a[0][2] == a[1][1] == a[2][0] != "_":
        return a[0][2]
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2] != "_":
            return (a[i][0])
        elif a[0][i] == a[1][i] == a[2][i] != "_":
            return (a[0][i])

    else:
        return None


def is_draw(table):
    for row in table:
        for i in row:
            if i == "_":
                return False
    return True


def game_state(table):
    is_winner = winner(table)
    if is_winner == None:
        if is_draw(table) == True:
            print("Draw")
            return True
        elif is_draw(table) == False:
            return False
    else:
        print(is_winner, "wins")
        return True



def menu():
    not_correct=True
    while not_correct:
        g_mode=input('print start, players or quit: ').split()
        possible_input=["user", "easy"]
        if len(g_mode)==3 and g_mode[0]=="start" and g_mode[1] in possible_input and g_mode[2] in possible_input:
            x,o=g_mode[1], g_mode[2]
            return x,o

        elif len(g_mode)==1 and g_mode[0]=="exit":
            return False
        else:
            print("Bad parameters!")



def main(a):
    display_table(a)
    game_is_going=True


    x, o = menu()

    while game_is_going:

        if x=='user':
            user_turn(a, "X")
        elif x=='easy':
            computer_turn(a, "X")
        display_table(a)
        game_state(a)
            #game_is_going=False
        if o=='user':
            user_turn(a, "O")
        elif o=='easy':
            computer_turn(a, "O")
        display_table(a)
        game_state(a)
            #game_is_going=False





main(a)