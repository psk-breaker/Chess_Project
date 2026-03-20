from domain.board import Board
from domain.piece import Pawn

TURN = ['BLANK', 'white', 'black']
class Game:
    def __init__(self):
        self.turn_counter = 1
        self.turn = TURN[self.turn_counter]
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
    
    def move_piece(self, piece, target):
        if self.turn_check(piece):
            self.board.move_piece(piece, target)
            if piece.location == target:
                self.turn_swap()
        elif self.turn_check(piece) == False:
            raise ValueError(f"Not your turn {piece.colour}, it's {self.turn}'s turn")
    
    def make_move(self, start, end):
        piece = self.board.get_piece(str(start))
        target = str(end)
        self.move_piece(piece, target)
    
    def turn_check(self, piece):
        if self.turn == piece.colour:
            return True
        else:
            return False
    
    def turn_swap(self):
        self.turn_counter *= -1
        self.turn = TURN[self.turn_counter]
    