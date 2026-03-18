from domain.board import Board
from domain.piece import Pawn

class Game:
    def __init__(self):
        self.turn = 'white'
        self.board = Board()

    def pawn_game_creation(self):
        wp1 = Pawn('white', 'active', 'a2')
        wp2 = Pawn('white', 'active', 'b2')
        wp3 = Pawn('white', 'active', 'c2')
        self.board.place_piece(wp1)
        self.board.place_piece(wp2)
        self.board.place_piece(wp3)
        bp1 = Pawn('black', 'active', 'a7')
        bp2 = Pawn('black', 'active', 'b7')
        bp3 = Pawn('black', 'active', 'c7')
        self.board.place_piece(bp1)
        self.board.place_piece(bp2)
        self.board.place_piece(bp3)