from domain.board import Board
from domain.piece import Pawn, Rook, Knight, Bishop, Queen, King

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
        self.wp6 = Pawn('white', 'active', 'f2')
        self.wp7 = Pawn('white', 'active', 'g2')
        self.wp8 = Pawn('white', 'active', 'h2')

        self.bp1 = Pawn('black', 'active', 'a7')
        self.bp2 = Pawn('black', 'active', 'b7')
        self.bp3 = Pawn('black', 'active', 'c7')
        self.bp6 = Pawn('black', 'active', 'f7')
        self.bp7 = Pawn('black', 'active', 'g7')
        self.bp8 = Pawn('black', 'active', 'h7')

        self.wk = King('white', 'active', 'e1')
        self.bk = King('black', 'active', 'e8')

        self.board.place_piece(self.wp1)
        self.board.place_piece(self.wp2)
        self.board.place_piece(self.wp3)
        self.board.place_piece(self.wp6)
        self.board.place_piece(self.wp7)
        self.board.place_piece(self.wp8)
        self.board.place_piece(self.bp1)
        self.board.place_piece(self.bp2)
        self.board.place_piece(self.bp3)
        self.board.place_piece(self.bp6)
        self.board.place_piece(self.bp7)
        self.board.place_piece(self.bp8)

        self.board.place_piece(self.wk)
        self.board.place_piece(self.bk)
    
    def queen_game_creation(self):
        
        self.wq = Queen('white', 'active', 'e4')
        self.bq = Queen('black', 'active', 'd4')

        self.board.place_piece(self.wq) 
        self.board.place_piece(self.bq)
    
    def bishop_game_creation(self):
        self.bb1 = Bishop('black', 'active', 'c8')
        self.bb2 = Bishop('black', 'active', 'f8')
        self.wb1 = Bishop('white', 'active', 'c1')
        self.wb2 = Bishop('white', 'active', 'f1')
        self.board.place_piece(self.bb1)
        self.board.place_piece(self.bb2)
        self.board.place_piece(self.wb1)
        self.board.place_piece(self.wb2)
    
    def knight_game_creation(self):
        self.wn1 = Knight('white', 'active', 'b1')
        self.wn2 = Knight('white', 'active', 'f1')
        self.bn1 = Knight('black', 'active', 'b8')
        self.bn2 = Knight('black', 'active', 'f8')

        self.board.place_piece(self.wn1)
        self.board.place_piece(self.wn2)
        self.board.place_piece(self.bn1)
        self.board.place_piece(self.bn2)
    
    def rook_game_creation(self):
        self.wr1 = Rook('white', 'active', 'a1')
        self.wr2 = Rook('white', 'active', 'h1')
        self.br1 = Rook('black', 'active', 'a8')
        self.br2 = Rook('black', 'active', 'h8')

        self.board.place_piece(self.wr1)
        self.board.place_piece(self.wr2)
        self.board.place_piece(self.br1)
        self.board.place_piece(self.br2)

    def test_game_creation(self):
        self.pawn_game_creation()
        self.queen_game_creation()
        self.bishop_game_creation()
        self.knight_game_creation()
        self.rook_game_creation()

    
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
    