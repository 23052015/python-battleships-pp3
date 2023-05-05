from random import randint
import sys

# #Computer board 
# COMPUTER_BOARD = [[" "] * 8 for i in range(8)]


# #Player board
# PLAYER_BOARD = [[" "] * 8 for i in range(8)]


# #board
# coordinates = {
#     'A':0,
#     'B':1,
#     'C':2,
#     'D':3,
#     'E':4,
#     'F':5,
#     'G':6,
#     'H':7,
# }

board = []
for i in range(8):
    board.append(["O"] * 8)

def menu():
    """
    prints the main menu and shows options to choose
    """
    while True:
        print("1.New Game")
        print("2.Instructions")
        print("3.Credits")

        choice = input("Choose option: ")
        if choice == '1':
            show_board(board)
            # def
        elif choice == '2':
            print("hello")
            # def
        elif choice == '3':
            print("hello")
            # def
            break

#prints the board when user hits 1
def show_board(board):
    # print("  A B C D E F G H")
    # row_nr = 1
    for row in board:
        print("|".join(row))
        # row_nr += 1 


def create_ships(board, ship_len):
    while True:
        ship_row = randint(0, len(board) -1)
        ship_col = randint(0, len(board) -1)
        direction = randint(0, 1)

        if direction == 0:
            if ship_col > 8 - ship_len:
                continue
            for i in range(ship_len):
                if board[ship_row][ship_col+i] != "O":
                    continue
            for i in range(ship_len):
                board[ship_row][ship_col+i] != "S"
            break

        elif direction == 1:
            if ship_col > 8 - ship_len:
                continue
            for i in range(ship_len):
                if board[ship_row+i][ship_col] != "O":
                    continue
            for i in range(ship_len):
                board[ship_row+i][ship_col] != "S"
            break


# def player_shot()


menu()