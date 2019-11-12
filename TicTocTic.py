import sys
import time


def check_position(the_position):
    if the_position not in taken_positions:
        return True
    else:
        return False

def get_position():
    position = int(input("Enter a position : "))
    return position

def draw_position_x(location):
    if location == 1:
        game_board[0][0] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")

    if location == 2:
        game_board[1][0] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 3:
        game_board[2][0] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 4:
        game_board[0][1] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 5:
        game_board[1][1] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 6:
        game_board[2][1] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 7:
        game_board[0][2] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 8:
        game_board[1][2] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 9:
        game_board[2][2] = 'x'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")

def draw_position_o(location):
    if location == 1:
        game_board[0][0] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 2:
        game_board[1][0] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 3:
        game_board[2][0] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 4:
        game_board[0][1] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 5:
        game_board[1][1] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 6:
        game_board[2][1] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 7:
        game_board[0][2] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 8:
        game_board[1][2] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")
    if location == 9:
        game_board[2][2] = 'o'
        print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
        print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
        print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")

def win_check():
    if game_board[0][0] == 'x' and game_board[1][0] == 'x' and game_board[2][0] == 'x' or \
        (game_board[0][0] == 'o' and game_board[1][0] == 'o' and game_board[2][0] == 'o'):  # 1 HORIZONTAL
        return True
    if game_board[0][1] == 'x' and game_board[1][1] == 'x' and game_board[2][1] == 'x' or \
        (game_board[0][1] == 'o' and game_board[1][1] == 'o' and game_board[2][1] == 'o'):  # 2 HORIZONTAL
        return True
    if game_board[0][2] == 'x' and game_board[1][2] == 'x' and game_board[2][2] == 'x' or \
        (game_board[0][2] == 'o' and game_board[1][2] == 'o' and game_board[2][2] == 'o'):  # 3 HORIZONTAL
        return True
    if game_board[0][0] == 'x' and game_board[0][1] == 'x' and game_board[0][2] == 'x' or \
        (game_board[0][0] == 'o' and game_board[0][1] == 'o' and game_board[0][2] == 'o'):  # 1 VERTICAL
        return True
    if game_board[1][0] == 'x' and game_board[1][1] == 'x' and game_board[1][2] == 'x' or \
        (game_board[1][0] == 'o' and game_board[1][1] == 'o' and game_board[1][2] == 'o'):  # 2 VERTICAL
        return True
    if game_board[2][0] == 'x' and game_board[2][1] == 'x' and game_board[2][2] == 'x' or \
        (game_board[2][0] == 'o' and game_board[2][1] == 'o' and game_board[2][2] == 'o'):  # 3 VERTICAL
        return True
    if game_board[0][0] == 'x' and game_board[1][1] == 'x' and game_board[2][2] == 'x' or \
        (game_board[0][0] == 'o' and game_board[1][1] == 'o' and game_board[2][2] == 'o'):  # 1 DIAGONAL
        return True
    if game_board[0][2] == 'x' and game_board[1][1] == 'x' and game_board[2][0] == 'x' or \
        (game_board[0][2] == 'o' and game_board[1][1] == 'o' and game_board[2][0] == 'o'):  # 2 DIAGONAL
        return True
    else:
        return False
intro_board = [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]

print("Welcome to TIC TAC TOE!")
print("You can pick location by identifying the position on the board. (There are 9 positions)")
print("The player who plays first will be using 'x' and the second player will be using 'o'.")
print("|" + intro_board[0][0] + "|" + intro_board[1][0] + "|" + intro_board[2][0] + "|")
print("|" + intro_board[0][1] + "|" + intro_board[1][1] + "|" + intro_board[2][1] + "|")
print("|" + intro_board[0][2] + "|" + intro_board[1][2] + "|" + intro_board[2][2] + "|")

game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
taken_positions = []
which_turn = 'P1'
win = False
num_moves = 0
running = True
isValid = True

while running:
    while num_moves < 9 and not win:
        which_position = get_position()

        if which_turn == 'P1':

            isValid = check_position(which_position)
            if isValid:
                which_turn = 'P2'
                num_moves = num_moves + 1
                taken_positions.append(which_position)
                draw_position_x(which_position)
                break
            if not isValid:
                print("Position taken, try again.")
                break
        if which_turn == 'P2':

            isValid = check_position(which_position)
            if isValid:
                which_turn = 'P1'
                num_moves = num_moves + 1
                taken_positions.append(which_position)
                draw_position_o(which_position)
                break
            if not isValid:
                print("Position taken, try again.")
                break

    win = win_check()
    if win:
        print("We have a winner!!!")
        print("Exiting in 10 seconds")
        time.sleep(10)
        running = False

    if num_moves == 9 and not win:
        print("Draw!")
        print("Exiting in 10 seconds")
        time.sleep(10)
        running = False

if not running:
    print("Exiting Game")
    sys.exit()