from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system


class State:
    def __init__(self):
        self.HUMAN = -1
        self.COMP = +1
        self.board = [
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
        ]

    def __str__(self):
        return

    def __repr__(self):
        return



class Minimax(State):
    def __init__(self):
        super().__init__():




def main():
    execution = Minimax()
    

if __name__ == '__main__':
    main()