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

player_hits = []
computer_hits = []


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
                if board[i][row] == "S":
                    return False
            for i in range(column, column + ship_len):
                board[i][row] = "S"
    else:
        if row + ship_len > 8:
            return False
        else:
            for i in range(row, row + ship_len):
                if board[i][column] == "S":
                    return False 
            for i in range(row, row + ship_len):
                board[i][column] = "S"
    return True






def player_shot(board, create_ships):

        """
        The function player shot allows the player to choose the cell
        which should be targeted and returns gives him the information 
        if the target was hit or missed.
        """
        while True:
            try:
                numbers = range(1, 9)
                vertical = ','.join(map(str, numbers))
                row = input("Please enter a row on the board 1-8: \n")
                if row in vertical:
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a number between 1-8\n")
        while True:
            try:
                letters = 'ABCDEFGH'               
                column = input("Please a column on the board A-H: \n").upper()
                if column not in letters:
                    print("Please enter a valid letter between A-H\n")
                else:
                    column = coordinates[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-H\n")
        return row, column

def player_turn(board):
    """
    This function checks if the computers ship was hit and returns
    the information to the user if he hit or missed a ship
    """

    row, column = player_shot(COMPUTER_BOARD, create_ships)
    if board[row][column] == "O":
        player_turn(board)
    elif board[row][column] == "X":
        player_turn(board)
    elif COMPUTER_BOARD[row][column] == "S":
        board[row][column] = "X"
        print("You hit a ship!")

    else:
        board[row][column] = "O"
        print("You hit empty waters")



def computer_turn(board):
    """
    The function computer shot randomly chooses a cell
    on the player boards and attacks it. The player receives an
    if his ship was hit or missed
    """
    row, column = random.randint(0, 7), random.randint(0, 7)
    if board[row][column] == "O":
        computer_turn(board)
    elif board[row][column] == "X":
        computer_turn(board)
    elif PLAYER_BOARD[row][column] == "S":
        board[row][column] = "X"
        print("Your ship was hit!")

            
    else:
        board[row][column] = "O"
        print("They hit empty water")


def playerscore_count(board, player_hits):
    """
    The playerscore count function counts the number of times
    the player has hit a ship on the board and returns the count
    """
    score = 0
    for row in board:
        for column in row:
            if column == "X":
                score += 1
    player_hits.append(score)
    print("Player score:", score)
    return score


def computer_score_count(board, computer_hits):
    """
    The computer score count function counts the number of times
    the computer has hit a ship on the board and returns the count
    """
    score = 0
    for row in board:
        for column in row:
            if column == "X":
                score += 1
    computer_hits.append(score)
    print("Computer score:", score)
    return score


def start_game():
    """
    Start game function
    """
    # Add the ships to each board
    create_ships(PLAYER_BOARD)
    create_ships(COMPUTER_BOARD)

    # Display the players board
    print('Player board\n')
    show_board(PLAYER_BOARD)
    # Players turn
    while True:
        # Players turn
        print("Guess the ship coordinates\n")
        # Show the computers current board
        print('Computers board\n')
        show_board(COMPUTER_BOARD)
        # Carry out the players turn, targeting the computers board
        player_turn(COMPUTER_BOARD)
        computer_turn(PLAYER_BOARD)

        if playerscore_count(COMPUTER_BOARD, player_hits) == 3:
            print("You sunk all their ships! You win!")
            return play_again()

        # Computers turn
        print('Player board\n')
        # Carry out the computers turn, targeting the players board

        # Show the players board
        show_board(PLAYER_BOARD)

        if computer_score_count(PLAYER_BOARD, computer_hits) == 3:
            print("They have sunk all your ships! You lose")
            return play_again()


def play_again():
    """
    The play again function will ask the player
    if they want to play again after the game has ended
    """
    global PLAYER_BOARD
    global COMPUTER_BOARD
    PLAYER_BOARD = [[" "] * 8 for i in range(8)]
    COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
    print("Would you like to play again?\n")
    answer = input("Enter Y or N \n").upper()
    print(' ')
    while True:
        if answer == "Y":
            start_game()
        elif answer == "N":
            print(' ')
            print("Goodbye! See you next time!\n")
            print(' ')
            sys.exit()
        else:
            print(' ')
            print("Please enter Y or N\n")
            answer = input("Enter Y or N \n").upper()


# if __name__ == "__main__":
    
start_game()


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