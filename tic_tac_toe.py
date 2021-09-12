# board
board = [' ' for x in range(10)]

# insert the letter ('X' or 'O')
def insert_letter(letter, pos):
    board[pos] = letter


# check if the space is empty (free to occupy)
def space_free(pos):
    return board[pos] == ' '


# print board (as 3x3 matrix)
def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# list of win combinations
def is_win(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
        (bo[4] == le and bo[5] == le and bo[6] == le) or \
        (bo[1] == le and bo[2] == le and bo[3] == le) or \
        (bo[1] == le and bo[4] == le and bo[7] == le) or \
        (bo[2] == le and bo[5] == le and bo[8] == le) or \
        (bo[3] == le and bo[6] == le and bo[9] == le) or \
        (bo[1] == le and bo[5] == le and bo[9] == le) or \
        (bo[3] == le and bo[5] == le and bo[7] == le)


# player gets to choose if pvp or pvc
def choose_mode():
    run = True
    while run:
        cmode = input('Please select if pvc (enter 1) or pvp (enter 2): ')

        # check if the input is a number
        try:

            # convert the input to integer
            cmode = int(cmode)

            # choose either 1 or 2 return false to end the loop
            if cmode ==  1 or cmode == 2:
                run = False

                # return the value so that main can choose mode
                return cmode
            
            # ask to input number in the valid range
            else:
                print('Please choose pvc or pvp.')

        # ask to input a valid number
        except:
            print('Please input a valid number.')


# player gets to choose and occupy spots
def player1_move():
    run = True
    while run:
        move = input('Player 1 please select a position to place an \'X\' in (1-9): ')

        # check if the input is a number
        try:

            # convert the input to integer
            move = int(move)

            # check if the input position is in the valid range
            if move > 0 and move < 10:

                # check if the spot is empty
                if space_free(move):
                    run = False

                    # insert the letter in this position
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied.')
            
            # ask to input number in the valid range
            else:
                print('Please type a number within the range (1-9).')
        
        # ask to input a number
        except:
            print('Please type a number.')


# player2 gets to choose and occupy spots
def player2_move():
    run = True
    while run:
        move = input('Player 2 please select a position to place an \'O\' in (1-9): ')

        # check if the input is a number
        try:

            # convert the input to integer
            move = int(move)

            # check if the input position is in the valid range
            if move > 0 and move < 10:

                # check if the spot is empty
                if space_free(move):
                    run = False

                    # insert the letter in this position
                    insert_letter('O', move)
                else:
                    print('Sorry, this space is occupied.')
            
            # ask to input number in the valid range
            else:
                print('Please type a number within the range (1-9).')
        
        # ask to input a number
        except:
            print('Please type a number.')


# computer move
def comp_move():

    # for index, value in enumerate(array_name), providing position of empty spots
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # check if there is a winning positions for either computer or player
    # place at player's winning position as block
    # place at computer's winning position, winning
    for letter in ['O', 'X']:
        for i in possible_moves:

            # duplicate the board with [:]
            board_copy = board[:]

            # place 'O' or 'X' in empty spot
            board_copy[i] = letter
            if is_win (board_copy, letter):
                move = i
                return move
    
    # find empty corner position when there is no winning position
    open_corner = []
    for i in possible_moves:
        if i in [1,3,7,9]:

            # list.append(element), adding element in list
            open_corner.append(i)

    # randomly choose a empty spot at corner when there is one or more
    if len(open_corner) > 0:
            move = select_random(open_corner)
            return move

    # occupy the center spot if it is empty
    if 5 in possible_moves:
            move = 5
            return move
    
    # find empty edge position when there is no winning position
    open_edge = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            open_edge.append(i)

    # randomly choose a empty spot at edge when there is one or more
    if len(open_edge) > 0:
            move = select_random(open_edge)
            return move


# randomly select position from possible_moves
def select_random(li):
    import random
    length = len(li)
    r = random.randrange(0,length)
    return li[r]

# check if the board is full
def board_full(board):

    # count() retun the number of time the ' ' appears on the board
    # while more than 1 empty spot is on the board, the board is not full, thus return false to the statement
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():

    # start the game and print the empty board
    print('Welcome to Tic Tac Toe.')
    mode = choose_mode()
    print_board(board)
 
    # when the board is not full yet, and it's pvc mode
    while not(board_full(board)) and mode == 1:

        # if O (computer) is not the winner, player's turn
        if not(is_win(board, 'O')):
            player1_move()                    

            # last move made by player may win the game
            if (is_win(board, 'X')) and board_full(board):
                print_board(board)
                print('Player 1 won, good job!')
                
            # last move made by player fill out the board
            elif not (is_win(board, 'X')) and board_full(board):
                print_board(board)
                print('Game is a tie since there is no more spaces left to move.')
                
            # simply print the board if it is not the last move
            else:
                print_board(board)

            # if O (computer) is the winner, game is over, break
        else:
            print('Sorry, computer won this time.')
            break
            
        if not board_full(board):

            # if X (player) is not the winner, computer's turn
            if not(is_win(board, 'X')):
                move = comp_move() 
                
                # end the game when no more moves can be made by the computer
                if move == 0:
                    print('A Game is a tie since there is no more spaces left to move.')
                
                # make a move by computer when there is spot available
                else:
                    insert_letter('O', move)
                    print('Computer placed an \'O\' in position:', move , ':')
                    print_board(board)

            
            # if X (player) is the winner, game is over, break
            else:
                print('You won, good job!')
                break

    # when the board is not full yet, and it's pvp mode
    while not(board_full(board)) and mode == 2:

        # if O (player2) is not the winner, player1's turn
        if not(is_win(board, 'O')):
            player1_move()                    

            # last move made by player1 may win the game
            if (is_win(board, 'X')) and board_full(board):
                print_board(board)
                print('Player 1 won, good job!')
                
            # last move made by player1 fill out the board
            elif not (is_win(board, 'X')) and board_full(board):
                print_board(board)
                print('Game is a tie since there is no more spaces left to move.')
                
            # simply print the board if it is not the last move
            else:
                print_board(board)

        else:
            print('Player 2 won, good job!')
            break


        if not board_full(board):

            # if X (player1) is not the winner, player2's turn
            if not(is_win(board, 'X')):
                player2_move() 

                # end the game when no more moves can be made by the computer
                if not (is_win(board, 'O')) and board_full(board):
                    print_board(board)
                    print('A Game is a tie since there is no more spaces left to move.')
                
                else:
                    print_board(board)
            
            # if X (player1) is the winner, game is over, break
            else:
                print('Player 1 won, good job!') 
                break



# ask if wants to play again when game is over
while True:
    answer = input('Would you like to play? (Y/N)')

    #lower() gives lower case of input answer
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-------------------------------------')
        main()

    else:
        break
