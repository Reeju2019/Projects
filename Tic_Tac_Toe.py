#  ----------Global Variable------------
# Game Board 
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-',]
# If the game is still going
game_is_still_going = True
#who win? or tie?
winner = None
# Whose turn it is?
current_player = 'X'

# Display board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Play game
def play_game():
    # Display initial board
    display_board()
    # While the game is still going
    while game_is_still_going:
        # Handle a single turn of a arbitrary player
        handle_turn(current_player)
        # If the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()
    # The game ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')


    
# Handle turn 
def handle_turn(player):
    global current_player
    print(player + '\'s turn.')
    position = input("Enter a number from 1-9: ")
    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Invalid Input.')
            position = input('Choose a position from 1-9: ')
        position = int(position)-1
        if board[position] == '-':
            valid = True
        else:
            print('You can\'t go there. Go again.')
        
    
    board[position] = current_player
    display_board()


# Check if the game is still going
def check_if_game_over():
    check_if_win()
    check_if_tie()

#check win
def check_if_win():
    global winner 
    # Check row
    row_winner = check_rows()
    # Check coloum
    column_winner = check_columns()
    # Check diagonal
    diagonal_winner = check_diags()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None

    return

def check_rows():
    global game_is_still_going
    row1 = board[0]==board[1]==board[2]!='-'
    row2 = board[3]==board[4]==board[5]!='-'
    row3 = board[6]==board[7]==board[8]!='-'
    if row1 or row2 or row3:
        game_is_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
    global game_is_still_going
    column1 = board[0]==board[3]==board[6]!='-'
    column2 = board[1]==board[4]==board[7]!='-'
    column3 = board[2]==board[5]==board[8]!='-'
    if column1 or column2 or column3:
        game_is_still_going = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diags():
    global game_is_still_going
    diagonal1 = board[0]==board[4]==board[8]!='-'
    diagonal2 = board[2]==board[4]==board[6]!='-'
    if diagonal1 or diagonal2:
        game_is_still_going = False
    if diagonal1 :
        return board[0]
    elif diagonal2:
        return board[2]
    return

# Check tie
def check_if_tie():
    global game_is_still_going
    if '-' not in board:
        game_is_still_going = False
    return
# Flip player 
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


#print the rules for playing tic-tac-toe
play_game()