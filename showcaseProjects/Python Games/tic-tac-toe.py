# Ponder/Prove Assignment Development (TicTacToe)
# By Jordan Kraude
def main():
    board = create_board()
    player = player_turn('O')

    #Loop until game has winner or the board is full(stalemate)
    while not winner(board) or board_full(board):
        display_board(board)
        board = user_choice(player, board)
        player = player_turn(player)


    #Game Finish
    display_board(board)
    print('Thank you for playing!')

#Creates the 9 numbers in a list to format a board)
def create_board():
    board = [1,2,3,4,5,6,7,8,9]
    return board

#Shows the board that users can choose from (format of teacher)
def display_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-',)
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')


#Decides the player that will make the choice
def player_turn(current_player):
    if current_player == 'O':
        return 'X'
    elif current_player == 'X': 
        return 'O'

#Choice from user to play the game
def user_choice(player, board):
    choice = int(input('What number would you like to choose between 1-9? '))
    print()
    board[choice - 1] = player
    return board
    
#If any of these are found the the loop breaks
def winner(board):
    return (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6])
        
#This is if the board is filled up without a winner
def board_full(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 



main()


