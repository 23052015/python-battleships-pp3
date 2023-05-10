import random
import sys
import string

# Computer board
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]


# Player board
PLAYER_BOARD = [[" "] * 8 for i in range(8)]


# Ship lengths of ships on the board
SHIP_LENGTHS = [1, 1, 2, 3, 3, 4, 5]


# board
coordinates = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
}


# prints the board when user hits 1
def show_board(board):
    print("  A B C D E F G H")
    row_nr = 1
    for row in board:
        print("%d|%s|" % (row_nr, "|".join(row)))
        row_nr += 1


def create_ships(board):
    """
    The create ships function places the ships on the board.
    Using the place ship function which is called inside it also checks
    if the ships fit and don't overlap
    """
    for ship_len in SHIP_LENGTHS:
        while True:
            direction, row, column = random.choice(["H", "V"]), \
            random.randint(0, 7), random.randint(0, 7)
        if place_ship(board, ship_len, direction, row, column):
            break


def place_ship(board, ship_len, direction, row, column):
    """
    The place ship function checks if the ships fit on the board and
    don't overlap
    """
    if direction == "H":
        if column + ship_len > 8:
            return False
        else:
            for i in range(column, column + ship_len):
                if board[row][i] == "S":
                    return False
            for i in range(column, column + ship_len):
                board[row][i] = "S"
    else:
        if row + ship_len > 8:
            return False
        else:
            for i in range(row, row + ship_len):
                if board[row][i] == "S":
                    return False 
            for i in range(row, row + ship_len):
                board[column][i] = "S"
    return True






def player_shot(board, ship_len):
    while True:
        try:
            guess_row = int(input("Fire at row 1-8: "))
            guess_column = input("Fire at column A-H")    
          
            if guess_row == ship_row and guess_column == ship_col
                print('Bullseye!You hit the ship')
            else:
                if (guess_row < 0 or guess_row > 5) or (guess_column < "i" or guess_column > "z"):
                    print("Please enter valid coordinates")
                elif (board[guess_row][guess_col] == "X"):
                print("You already tried this coordinates!")

                else:
                    print("You missed")
                    board[guess_row][guess_column]
        except ValueError:
            print("Please enter a valid number between 1-8\n")
        except KeyError:
            print('Enter a valid letter between A-H')






# def menu():
#     """
#     prints the main menu and shows options to choose
#     """
#     while True:
#         print("1.New Game")
#         print("2.Instructions")
#         print("3.Credits")

#         choice = input("Choose option: ")
#         if choice == '1':
#             show_board(board)
#             create_ships(board, ship_len)
#             player_shot(board, ship_len)
#             # def
#         elif choice == '2':
#             print("hello")
#             # def
#         elif choice == '3':
#             print("hello")
#             # def
#             break


# menu()