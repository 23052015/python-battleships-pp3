from random import randint

import sys

#Computer board 
COMPUTER_BOARD = [[" "] *8 for i in range(8)]


#Player board
PLAYER_BOARD = [[" "] *8 for i in range(8)]


#board
coordinates = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
}


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
            show_board(coordinates)
            # def
        elif choice == '2':
            print("hello")
            # def
        elif choice == '3':
            print("hello")
            # def
            break

#prints the board when user hits 1
def show_board(coordinates):
    print(" A B C D E F G H")
    print(" O O O O O O O O")
    row_nr = 1
    for row in coordinates:
        print("%d|%s|" % (row_nr, "|".join(row)))
        row_nr += 1 



menu()