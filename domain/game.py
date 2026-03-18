from domain.board import Board
from domain.piece import Pawn

class Game:
    def __init__(self):
        self.turn = 'white'
        self.board = Board()

