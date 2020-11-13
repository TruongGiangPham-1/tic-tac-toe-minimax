from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system
"""
   oominimax.py is mostly cut and pasted from minimax.py to fit the 
   weekly exeercise #6 specification. 
   minimax.py was written by Clederson Cruz, year 2017. Modified by Paul Lu.

   
   name: Truong-Giang Pham
   CCID: 1662405

"""


def clean():
    """
    Clears the console
    """
    # Paul Lu.  Do not clear screen to keep output human readable.
    print()
    return

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


class State:
    def __init__(self):
        """Description: instantiates the board object.
           Argument: self
           Returns: None
        """
        self.type = str(self.__class__)
        self.board = [
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
        ]
        return

    def __str__(self):
        """Description: this method execute when print() is invoked.
           Arguments: self
           return: the class type of the object
        """
        return self.type

    def __repr__(self):
        """Description: formal representation of the class object
           Argument: self
           return: the object id and the class type.
        """
        return f'<{id(self.type)}> {self.type}'

    def get_board(self):
        """Description: a getter for the self.board attribute.
           Argument: self
           return: the self.board attribute.
        """
        return (self.board)

    def set_board(self, x, y, player):
        """Description: a setter for the self.board attribute.
           Argument: self, x, y, player
                     x, y is the coordinate of the board
                     player is HUMAN or COMP
            return: None
        """
        self.board[x][y] = player
        return

    def empty_cells(self):  
        """
        Each empty cell will be added into cells' list
        :param state: the state of the current board
        :return: a list of empty cells
        """
        cells = []

        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def valid_move(self, x, y):  
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        if [x, y] in self.empty_cells():  
            return True
        else:
            return False

    def set_move(self, x, y, player): 
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        if self.valid_move(x, y):  
            self.set_board(x, y, player)  
            return True
        else:
            return False

    def wins(self, player):
        """
        This function tests if a specific player wins. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :param state: the state of the current board
        :param player: a human or a computer
        :return: True if the player wins
        """
        win_state = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        if [player, player, player] in win_state:  
            return True
        else:
            return False

    def game_over(self, COMP, HUMAN):
        """
        This function test if the human or computer wins
        :param state: the state of the current board
        :return: True if the human or computer wins

        **Note: Truong-Giang Pham change this method's parameter, now it takes
                in COMP and HUMAN variable.
        """
        return self.wins(HUMAN) or self.wins(COMP)  

    def evaluate(self, COMP, HUMAN):
        """
        Function to heuristic evaluation of state.
        :param state: the state of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw

        **Note: Truong-Giang Pham change this method's parameter, now it takes
                in COMP and HUMAN variable.
        """
        if self.wins(COMP):
            score = +1
        elif self.wins(HUMAN):
            score = -1
        else:
            score = 0

        return score

    def render(self, c_choice, h_choice):  
        """
        Print the board on console
        :param state: current state of the board
        """

        chars = {
            -1: h_choice,
            +1: c_choice,
            0: ' '
        }
        str_line = '---------------'

        print('\n' + str_line)
        for row in self.get_board():  
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')  
            print('\n' + str_line)


class Turns:
    def __init__(self):
        """Description: initiatize HUMAN,COMP, and type attributes.
           Argument: self
           Return: none
        """
        self.type = str(self.__class__)
        self.HUMAN = -1
        self.COMP = +1
        return

    def __str__(self):
        """Description: this method execute when print() is invoked.
           Arguments: self
           Return: the class type of the object
        """
        return self.type

    def __repr__(self):
        """Description: formal representation of the class object
           Argument: self
           return: the object id and the class type.
        """
        return f'<{id(self.type)}> {self.type}'
            
    def minimax(self, depth, player, state):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """
        if player == self.COMP:  
            best = [-1, -1, -infinity]  
        else:  
            best = [-1, -1, +infinity]

        if depth == 0 or state.game_over(self.COMP, self.HUMAN):
            score = state.evaluate(self.COMP, self.HUMAN)  
            return [-1, -1, score]

        for cell in state.empty_cells():
            x, y = cell[0], cell[1]
            state.set_board(x,y,player)  
            score = self.minimax(depth - 1, -player, state)
            state.board[x][y] = 0  
            score[0], score[1] = x, y

            if player == self.COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  

        return best

    def ai_turn(self, c_choice, h_choice, state):  
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(state.empty_cells())  
        if depth == 0 or state.game_over(self.COMP, self.HUMAN):  
            return

        clean()
        print(f'Computer turn [{c_choice}]')
        state.render(c_choice, h_choice)  

        if depth == 9:
            x = choice([0, 1, 2])  
            y = choice([0, 1, 2])  
        else:
            move = self.minimax(depth, self.COMP, state)
            x, y = move[0], move[1]

        state.set_move(x, y, self.COMP) 
        # Paul Lu.  Go full speed.
        # time.sleep(1)

    def human_turn(self, c_choice, h_choice, state):  
        """
        The Human plays choosing a valid move.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = len(state.empty_cells())
        if depth == 0 or state.game_over(self.COMP, self.HUMAN):
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'Human turn [{h_choice}]')
        state.render(c_choice, h_choice)  

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]  
                can_move = state.set_move(coord[0], coord[1], self.HUMAN)  
                if not can_move:
                    print('Bad move')
                    move = -1  
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):  
                print('Bad choice')



def main():
    randomseed(274 + 2020)
    clean() # clean the board.
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    # Instantiate State class object
    state = State()
    # Instantiate turns_object object
    turns_object = Turns()
    # Main loop of this game
    while len(state.empty_cells()) > 0 and not state.game_over(turns_object.COMP, turns_object.HUMAN):
        if first == 'N':  
            turns_object.ai_turn(c_choice, h_choice, state)  
            first = ''

        turns_object.human_turn(c_choice, h_choice, state)
        turns_object.ai_turn(c_choice, h_choice, state)

    # Game over message
    if state.wins(turns_object.HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        state.render(c_choice, h_choice)
        print('YOU WIN!')
    elif state.wins(turns_object.COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        state.render(c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        state.render(c_choice, h_choice)
        print('DRAW!')

    exit()

    



if __name__ == '__main__':
    main()