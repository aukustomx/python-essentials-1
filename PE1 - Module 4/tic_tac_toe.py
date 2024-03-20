from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  | ", board[0][1], "   |   ", board[0][2], " |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  | ", board[1][1], "   |   ", board[1][2], " |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  | ", board[2][1], "   |   ", board[2][2], " |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_move = int(input("Enter your move: "))
            if user_move < 1 or user_move > 9:
                raise ValueError

            board_position = board_dict[user_move]

            # Check if the move user selected is free
            user_selected_square = (board_position[0], board_position[1])
            free_squares = make_list_of_free_fields(board)
            if user_selected_square not in free_squares:
                raise AttributeError("Esta posición ya está ocupada. Elige otra.")
            
            board[board_position[0]][board_position[1]] = user_sign
            display_board(board)
            break
    
        except ValueError:
            print("You need to enter an integer between 1 and 9 ")
        except AttributeError as e:
            print(e)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for row in range(0, len(board)):
        for column in range(0, len(board)):
            if type(board[row][column]) is int:
                free_squares.append((row, column))

    return free_squares


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for combination in row_combination_victory:
        pos_1 = combination[0]
        sign_1 = board[pos_1[0]][pos_1[1]]

        pos_2 = combination[1]
        sign_2 = board[pos_2[0]][pos_2[1]]
        
        pos_3 = combination[2]
        sign_3 = board[pos_3[0]][pos_3[1]]
        #print(sign_1, sign_2, sign_3)

        if sign_1 == sign and sign_2 == sign and sign_3 == sign:
            return True 


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        computer_move = randrange(8) + 1
        try:
            is_squared_ocuppied(board, computer_move)
        except AttributeError as e:
            continue
        board_position = board_dict[computer_move]
        board[board_position[0]][board_position[1]] = computer_sign
        break
    display_board(board)


def is_squared_ocuppied(board, move):
    # The function checks if the position of the move is occupied.
    board_position = board_dict[move]
    selected_square = (board_position[0], board_position[1])
    
    free_squares = make_list_of_free_fields(board)
    if selected_square not in free_squares:
        raise AttributeError("Esta posición ya está ocupada. Elige otra.")


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
board_dict = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2]
    }

computer_sign = 'X'
user_sign = 'O'

row_combination_victory = [
    [[0,0], [0,1], [0,2]],
    [[1,0], [1,1], [1,2]],
    [[2,0], [2,1], [2,2]],
    [[0,0], [1,0], [2,0]],
    [[0,1], [1,1], [2,1]],
    [[0,2], [1,2], [2,2]],
    [[0,0], [1,1], [2,2]],
    [[0,2], [1,1], [2,0]],
    ]


# The first move belongs to the computer − it always puts its first 'X'
# in the middle of the board
board[1][1] = computer_sign
display_board(board)

while len(make_list_of_free_fields(board)) > 0:
    enter_move(board)
    user_won = victory_for(board, user_sign)
    if user_won:
        print("You won!")
        break
    
    draw_move(board)
    computer_won = victory_for(board, computer_sign)
    if computer_won:
        print("Computer won!")
        break

