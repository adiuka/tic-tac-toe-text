import os

game_board = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-',]


# Board print function:

def show_board(b):
    board = b
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('---------')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('---------')
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Check score function
def check_score(b):
    # Player 1 check
    if b[0] == 'X' and b[4] == 'X' and b[8] == 'X':
        print("Player one wins!")
        return True
    elif b[2] == 'X' and b[4] == 'X' and b[6] == 'X':
        print("Player one wins!")
        return True
    elif b[0] == 'X' and b[1] == 'X' and b[2] == 'X':
        print("Player one wins!")
        return True
    elif b[3] == 'X' and b[4] == 'X' and b[5] == 'X':
        print("Player one wins!")
        return True
    elif b[6] == 'X' and b[7] == 'X' and b[8] == 'X':
        print("Player one wins!")
        return True
    elif b[0] == 'X' and b[3] == 'X' and b[6] == 'X':
        print("Player one wins!")
        return True
    elif b[1] == 'X' and b[4] == 'X' and b[7] == 'X':
        print("Player one wins!")
        return True
    elif b[2] == 'X' and b[5] == 'X' and b[8] == 'X':
        print("Player one wins!")
        return True
    # Player 2 Check:
    elif b[0] == 'O' and b[4] == 'O' and b[8] == 'O':
        print("Player two wins!")
        return True
    elif b[2] == 'O' and b[4] == 'O' and b[6] == 'O':
        print("Player two wins!")
        return True
    elif b[0] == 'O' and b[1] == 'O' and b[2] == 'O':
        print("Player two wins!")
        return True
    elif b[3] == 'O' and b[4] == 'O' and b[5] == 'O':
        print("Player two wins!")
        return True
    elif b[6] == 'O' and b[7] == 'O' and b[8] == 'O':
        print("Player two wins!")
        return True
    elif b[0] == 'O' and b[3] == 'O' and b[6] == 'O':
        print("Player two wins!")
        return True
    elif b[1] == 'O' and b[4] == 'O' and b[7] == 'O':
        print("Player two wins!")
        return True
    elif b[2] == 'O' and b[5] == 'O' and b[8] == 'O':
        print("Player two wins!")
        return True
    else: 
        return False
    

def game(b):
    game_board = b
    game_is_on = True
    turns = 9
    print("Lets start ze game!\n")
    while game_is_on:
        while True:
            try:
                player_1_choice = input("Player 1. Please input where you would like to place your X. Coordinates are decided by 1 to 9, from left to right: " )

                if game_board[int(player_1_choice) - 1] != '-':
                    print("Space already taken, please pick another block.")
                else: 
                    game_board[int(player_1_choice) - 1] = 'X'
                    turns -= 1
                    print(turns)
                    break
            except (IndexError, ValueError) as e:
                print(f"Invalid entry: {e}. Please enter a character ranging 1 to 9. ")

        os.system('cls||clear') # Clears the other text so it is not cluttered
        show_board(game_board)

    # A quick check if there are more turns and for the score
        if turns == 0:
            game_is_on = False
            print("The Game is a tie")
        elif check_score(game_board) == True:
            game_is_on = False
        else:

            while True:
                try:
                    player_2_choice = input("Player 2. Please input where you would like to place your X. Coordinates are decided by 1 to 9, from left to right: " )
                    if turns == 0:
                        break
                    elif game_board[int(player_2_choice) - 1] != '-':
                        os.system('cls||clear')
                        show_board(game_board)
                        print("Space already taken, please pick another block.")
                    else: 
                        game_board[int(player_2_choice) - 1] = 'O'
                        turns -= 1
                        break
                except (IndexError, ValueError) as e:
                    print(f"Invalid entry: {e}. Please enter a character ranging 1 to 9. ")

            os.system('cls||clear') # Clears the other text so it is not cluttered
            show_board(game_board)
            # Check the score:
            if check_score(game_board) == True:
                game_is_on = False
            
