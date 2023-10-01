from colors import ForegroundColors as fg

game_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def cls():
    for i in range(3):
        print("\n")

print("Player 1 , Enter your Data:")
player1_name = input("\t\tName: ")
player1_symbol = input("\t\tSymbol (X/O): ").upper()

if player1_symbol  != "O":
    player2_symbol = "O"
else:
    player2_symbol = "X"

print("\nPlayer 2 , Enter your Data:")
player2_name = input("\t\tEnter your name: ")

player1 = {
    "name": fg.cyan(player1_name),
    "symbol": fg.cyan(player1_symbol),
}
player2 = {
    "name": fg.purple(player2_name),
    "symbol": fg.purple(player2_symbol),
}

cls()

def print_game_board(game_board):

    vertical_line = fg.orange("|")
    Horizontal_Line = fg.orange("_")

    print("\n")  
    print("\t      {}      {}".format(vertical_line , vertical_line))  
    print("\t    {} {}  {}   {}  {}".format(game_board[0][0], vertical_line , game_board[0][1], vertical_line , game_board[0][2]))  
    print("\t{}{}{}{}{}".format(Horizontal_Line *6 , vertical_line , Horizontal_Line*6 , vertical_line , Horizontal_Line*6))  
 
    print("\t      {}      {}".format(vertical_line , vertical_line))
    print("\t   {}  {}  {}   {}  {}".format(game_board[1][0], vertical_line ,  game_board[1][1], vertical_line , game_board[1][2]))  
    print("\t{}{}{}{}{}".format(Horizontal_Line *6 , vertical_line , Horizontal_Line*6 , vertical_line , Horizontal_Line*6))
    print("\t      {}      {}".format(vertical_line , vertical_line))  

    print("\t  {}   {}  {}   {}  {}".format(game_board[2][0], vertical_line ,  game_board[2][1], vertical_line , game_board[2][2]))  
    print("\t      {}      {}".format(vertical_line , vertical_line))  
    print("\n") 
    
def player_move(board, player):  

    print("{} It's Your Turn, Enter Your Move:".format(player["name"]))
    
    row = int((input("\t\trow (1-3): ")))
    col = int((input("\t\tcol (1-3): ")))

    if 1 <= row < 4 and 1 <= col < 4 and board[row - 1][col - 1] == " ":
        board[row - 1][col - 1] = player["symbol"] 
    else: 
        cls()
        print_game_board(game_board)
        print(fg.red("ERROR !!! TRY AGAIN \n"))
        player_move(game_board , player)

def check_win(board, player):
    for row in board: 
        if row.count(player["symbol"]) == 3: 
            return True 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player["symbol"]: 
            return True 
    
    if board[0][0] == board[1][1] == board[2][2] == player["symbol"]:
        return True 
    elif board[0][2] == board[1][1] == board[2][0] == player["symbol"]:
        return True
    
    return False

def check_tie(board):
    for row in board: 
        for col in row: 
            if col == " ": 
                return False 
    return True

current_player = player1

while True:
    print_game_board(game_board)
    player_move(game_board, current_player)
    
    if check_win(game_board, current_player):
        cls()
        print_game_board(game_board)
        print(fg.green("\t\t\tCONGRATULATIONS!"))
        print("\t\t\tThe Winner is: {}".format(current_player["name"]))
        break
    
    elif check_tie(game_board):
        cls()
        print_game_board(game_board)
        print("It's a tie!")
        break

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

    cls()

print("Thanks for playing!\n")