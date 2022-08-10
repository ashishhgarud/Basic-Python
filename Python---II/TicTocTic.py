def draw_position(location, symbol):
    if location == 1:
        game_board[0][0] = symbol
    if location == 2:
        game_board[1][0] = symbol
    if location == 3:
        game_board[2][0] = symbol
    if location == 4:
        game_board[0][1] = symbol
    if location == 5:
        game_board[1][1] = symbol
    if location == 6:
        game_board[2][1] = symbol
    if location == 7:
        game_board[0][2] = symbol
    if location == 8:
        game_board[1][2] = symbol
    if location == 9:
        game_board[2][2] = symbol
    print("|" + game_board[0][0] + "|" + game_board[1][0] + "|" + game_board[2][0] + "|")
    print("|" + game_board[0][1] + "|" + game_board[1][1] + "|" + game_board[2][1] + "|")
    print("|" + game_board[0][2] + "|" + game_board[1][2] + "|" + game_board[2][2] + "|")