from domain.board import Board
from domain.piece import Pawn, Queen

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
    
    def queen_game_creation(self):
        self.wp6 = Pawn('white', 'active', 'f2')
        self.wp7 = Pawn('white', 'active', 'g2')
        self.wp8 = Pawn('white', 'active', 'h2')
        self.wq = Queen('white', 'active', 'd1')

        self.bp6 = Pawn('black', 'active', 'f7')
        self.bp7 = Pawn('black', 'active', 'g7')
        self.bp8 = Pawn('black', 'active', 'h7')
        self.bq = Queen('black', 'active', 'd8')

        self.board.place_piece(self.wp6)
        self.board.place_piece(self.wp7)
        self.board.place_piece(self.wp8)
        self.board.place_piece(self.wq)

        self.board.place_piece(self.bp6)
        self.board.place_piece(self.bp7)
        self.board.place_piece(self.bp8) 
        self.board.place_piece(self.bq)

    
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
        print(f'The web says that the target square is: {target}')
        self.move_piece(piece, target)
    
    def turn_check(self, piece):
        if self.turn == piece.colour:
            return True
        else:
            return False
    
    def turn_swap(self):
        self.turn_counter *= -1
        self.turn = TURN[self.turn_counter]
    