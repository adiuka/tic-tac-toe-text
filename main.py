from tkinter import * # This is a text based version, but will aim to make it in GUI as well.
import functions as f


print("Hello and welcome to the text based tic tac toe 2 player game!\n" 
      "Instructions are very simple, when each player is promted, enter a number between 1 and 9, \n"
      "symbolising the 9 blocks counting from 1 to 9. You can play against your friends or a CPU...\n"
      "Enjoyyyy!\n")


while True:
    answer = input("Would you like to play a game of Tic Tac Toe? y for yes and n for no: ")
    if answer.lower() == 'y':
        while True:
            answer2 = input("Select game mode (1 for single player, 2 for multiplayer and q for quit): ")
            if answer2 == '2':
                game_board = ['-', '-', '-',
                              '-', '-', '-',
                              '-', '-', '-',]
                f.two_player_game(game_board)
            elif answer2 == '1':
                game_board = ['-', '-', '-',
                              '-', '-', '-',
                              '-', '-', '-',]
                f.against_cpu(game_board)
            elif answer2 == 'q':
                break
            else:
                print("That is an incorrect input!")

    elif answer.lower() == 'n':
        print("Well... Then have a wonderful day!")
        break
    else:
        print("Incorrect input. Remember - y for yes, n for no")