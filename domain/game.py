from domain.board import Board
from domain.piece import Pawn

class Game:
    def __init__(self):
        self.turn = 'white'
        self.board = Board()
        
    def pawn_game_creation(self):
        self.wp1 = Pawn('white', 'active', 'a2')
        self.wp2 = Pawn('white', 'active', 'b2')
        self.wp3 = Pawn('white', 'active', 'c2')
        self.bp1 = Pawn('black', 'active', 'a7')
        self.bp2 = Pawn('black', 'active', 'b7')
        self.bp3 = Pawn('black', 'active', 'c7')
        self.board.place_piece(self.wp1)
        self.board.place_piece(self.wp2)
        self.board.place_piece(self.wp3)
        self.board.place_piece(self.bp1)
        self.board.place_piece(self.bp2)
        self.board.place_piece(self.bp3)