from random import randint


def make_table(table):
    first_row = [table[0], table[1], table[2]]
    second_row = [table[3], table[4], table[5]]
    third_row = [table[6], table[7], table[8]]
    a = []
    a.append(first_row)
    a.append(second_row)
    a.append(third_row)
    return a


def display_table(table):
    print("---------\n|", table[0][0], table[0][1], table[0][2], "|")
    print("|", table[1][0], table[1][1], table[1][2], "|")
    print("|", table[2][0], table[2][1], table[2][2], "|")
    print("---------")


def user_turn(a, sign):
    not_valid = True
    while not_valid:
        try:
            coordinates = input("Enter the coordinates: ")
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


def switch_turn(sign):
    if sign == "X":
        return "O"
    elif sign == "O":
        return "X"

    counter = 0
    if counter % 2 == 0:
        counter += 1
        return "X"
    else:
        counter += 1
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


def winner_or_draw(table):
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


def check_input(some_input):
    possible_input = ["user", "easy"]
    try:
        g_mode = some_input.split()
        if len(g_mode) == 1 and g_mode[0] == "exit":
            return "exit"
        elif len(g_mode) == 3 and g_mode[0] == "start" and g_mode[1] in possible_input and g_mode[2] in possible_input:
            return "start"
    except TypeError:
        print("Bad parameters!")


def parse_input(some_input):
    some_input = some_input.split()
    x, o = some_input[1], some_input[2]
    return x, o


def play_a_turn(a, player, sign):
    if player == "user":
        user_turn(a, sign)
    elif player == "easy":
        computer_turn(a, sign)


def main():
    not_quit = True
    while not_quit:
        not_correct = True
        while not_correct:
            menu_input = input()
            table = '_________'
            a = make_table(table)
            display_table(a)

            if check_input(menu_input) == "exit":
                not_quit = False
                break
            if check_input(menu_input) == "start":
                p1, p2 = parse_input(menu_input)
                game_is_going = True
                sign = 'X'
                while game_is_going:
                    play_a_turn(a, p1, sign)
                    sign = switch_turn(sign)
                    display_table(a)
                    if winner_or_draw(a) == True:
                        game_is_going = False
                        break
                    play_a_turn(a, p2, sign)
                    sign = switch_turn(sign)
                    display_table(a)
                    if winner_or_draw(a) == True:
                        game_is_going = False

            else:
                print("Bad parameters!")


main()