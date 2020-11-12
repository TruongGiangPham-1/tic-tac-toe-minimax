HUMAN = -1
COMP = +1
class State:
    def __init__(self):
        self.board = [
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
        ]

    def __str__(self):
        return

    def __repr__(self):
        return

    def empty_cells(self):  # need to be in State class. so def empty_cell(self)
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

    def valid_move(self, x, y):  # uses board so it has to be encapsulate in class State
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        if [x, y] in empty_cells(self.board):  # added self.
            return True
        else:
            return False

    def set_move(self, x, y, player):  # a setter of Class State
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        if self.valid_move(x, y):  # added self
            self.board[x][y] = player  # player = 1 or -1 depending on human turn or ai.  added self.
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
        if [player, player, player] in win_state:  # global human = -1 or global comp = +1  == player.
            # ex. [-1, -1, -1]
            return True
        else:
            return False

    def game_over(self):
        """
        This function test if the human or computer wins
        :param state: the state of the current board
        :return: True if the human or computer wins
        """
        return self.wins(HUMAN) or self.wins(COMP)  # runs win(HUMAN) and win(COMP)

    def render(self, c_choice, h_choice):  # since it loops over the board, then it is in Class State
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
        for row in self.board:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')  # prints l  l   l   l
            print('\n' + str_line)


def main():
    state = State()
    print(len(state.empty_cells())) # so that works
    print(state.game_over())  # so that works
    

if __name__ =='__main__':
    main()