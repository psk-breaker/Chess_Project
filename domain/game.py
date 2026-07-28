from domain.board import Board
from domain.piece import Pawn, Rook, Knight, Bishop, Queen, King

TURN = ['BLANK', 'white', 'black']
FILE = 'abcdefgh'

class Game:
    def __init__(self):
        self.turn_counter = 1
        self.turn = TURN[self.turn_counter]
        self.board = Board()

    def king_game_creation(self):
        self.wk = King('white', 'e1', id='wk')
        self.bk = King('black', 'e8', id='bk')
        self.board.place_piece(self.wk)
        self.board.place_piece(self.bk)

    def pawn_game_creation(self):
        self.wp1 = Pawn('white', 'a2', id='wp1')
        self.wp2 = Pawn('white', 'b2', id='wp2')
        self.wp3 = Pawn('white', 'c2', id='wp3')
        self.wp6 = Pawn('white', 'f2', id='wp6')
        self.wp7 = Pawn('white', 'g2', id='wp7')
        self.wp8 = Pawn('white', 'h2', id='wp8')

        self.bp1 = Pawn('black', 'a7', id='bp1')
        self.bp2 = Pawn('black', 'b7', id='bp2')
        self.bp3 = Pawn('black', 'c7', id='bp3')
        self.bp6 = Pawn('black', 'f7', id='bp6')
        self.bp7 = Pawn('black', 'g7', id='bp7')
        self.bp8 = Pawn('black', 'h7', id='bp8')

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

    def queen_game_creation(self):
        
        self.wq = Queen('white', 'd1', id='wq1')
        self.bq = Queen('black', 'd8', id='bq1')

        self.board.place_piece(self.wq) 
        self.board.place_piece(self.bq)
    
    def bishop_game_creation(self):
        self.wb1 = Bishop('white', 'c1', id='wb1')
        self.wb2 = Bishop('white', 'f1', id='wb2')
        self.bb1 = Bishop('black', 'c8', id='bb1')
        self.bb2 = Bishop('black', 'f8', id='bb2')
        
        self.board.place_piece(self.wb1)
        self.board.place_piece(self.wb2)
        self.board.place_piece(self.bb1)
        self.board.place_piece(self.bb2)
    
    def knight_game_creation(self):
        self.wn1 = Knight('white', 'b1', id='wn1')
        self.wn2 = Knight('white', 'g1', id='wn2')
        self.bn1 = Knight('black', 'b8', id='bn1')
        self.bn2 = Knight('black', 'g8', id='bn2')

        self.board.place_piece(self.wn1)
        self.board.place_piece(self.wn2)
        self.board.place_piece(self.bn1)
        self.board.place_piece(self.bn2)
    
    def rook_game_creation(self):
        self.wr1 = Rook('white', 'a1', id='wr1')
        self.wr2 = Rook('white', 'h1', id='wr2')
        self.br1 = Rook('black', 'a8', id='br1')
        self.br2 = Rook('black', 'h8', id='br2')

        self.board.place_piece(self.wr1)
        self.board.place_piece(self.wr2)
        self.board.place_piece(self.br1)
        self.board.place_piece(self.br2)

    def test_game_creation(self):
        self.king_game_creation()
        self.pawn_game_creation()
        # self.queen_game_creation()
        # self.bishop_game_creation()
        # self.knight_game_creation()
        # self.rook_game_creation()

    def standard_game_creation(self):
        self.wp1 = Pawn('white', 'a2', id='wp1')
        self.wp2 = Pawn('white', 'b2', id='wp2')
        self.wp3 = Pawn('white', 'c2', id='wp3')
        self.wp4 = Pawn('white', 'd2', id='wp4')
        self.wp5 = Pawn('white', 'e2', id='wp5')
        self.wp6 = Pawn('white', 'f2', id='wp6')
        self.wp7 = Pawn('white', 'g2', id='wp7')
        self.wp8 = Pawn('white', 'h2', id='wp8')

        self.bp1 = Pawn('black', 'a7', id='bp1')
        self.bp2 = Pawn('black', 'b7', id='bp2')
        self.bp3 = Pawn('black', 'c7', id='bp3')
        self.bp4 = Pawn('black', 'd7', id='bp4')
        self.bp5 = Pawn('black', 'e7', id='bp5')
        self.bp6 = Pawn('black', 'f7', id='bp6')
        self.bp7 = Pawn('black', 'g7', id='bp7')
        self.bp8 = Pawn('black', 'h7', id='bp8')

        self.wk = King('white', 'e1', id='wk')
        self.bk = King('black', 'e8', id='bk')

        self.board.place_piece(self.wp1)
        self.board.place_piece(self.wp2)
        self.board.place_piece(self.wp3)
        self.board.place_piece(self.wp4)
        self.board.place_piece(self.wp5)
        self.board.place_piece(self.wp6)
        self.board.place_piece(self.wp7)
        self.board.place_piece(self.wp8)
        self.board.place_piece(self.bp1)
        self.board.place_piece(self.bp2)
        self.board.place_piece(self.bp3)
        self.board.place_piece(self.bp4)
        self.board.place_piece(self.bp5)
        self.board.place_piece(self.bp6)
        self.board.place_piece(self.bp7)
        self.board.place_piece(self.bp8)

        self.board.place_piece(self.wk)
        self.board.place_piece(self.bk)

        self.queen_game_creation()
        self.bishop_game_creation()
        self.knight_game_creation()
        self.rook_game_creation()

    def promote_piece(self, piece):
        if piece.colour == 'white':
            if self.board.white_promotion_counter == 0:
                self.wx1 = Queen('white', piece.location, 'wq2')
                self.board.place_piece(self.wx1)
                self.board.white_promotion_counter += 1
            if self.board.white_promotion_counter == 1:
                self.wx2 = Queen('white', piece.location, 'wq3')
                self.board.place_piece(self.wx2)
                self.board.white_promotion_counter += 1
        if piece.colour == 'black':
            if self.board.black_promotion_counter == 0:
                self.bx1 = Queen('black', piece.location, 'bq2')
                self.board.place_piece(self.bx1)
                self.board.black_promotion_counter += 1
            if self.board.black_promotion_counter == 1:
                self.bx2 = Queen('black', piece.location, 'bq3')
                self.board.place_piece(self.bx2)
                self.board.black_promotion_counter += 1

    def move_piece(self, piece, target):
        if self.turn_check(piece):
            self.board.move_piece(piece, target)
            if piece.location == target:
                self.promotion(piece, target)
                self.turn_swap()
                self.in_check()
        elif self.turn_check(piece) == False:
            raise ValueError(f"Not your turn {piece.colour}, it's {self.turn}'s turn")
    
    def make_move(self, start, end):
        piece = self.board.get_piece(str(start))
        target = str(end)
        print(f'The web says that the target square is: {target}')
        self.move_piece(piece, target)

    def promotion(self, piece, target):
        if self.board.promotion(piece, target):
            if piece.colour == 'white':
                self.board.white_pieces.remove(piece)
                self.board.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = 0
                self.promote_piece(piece)
                piece.promote()
            if piece.colour == 'black':
                self.board.black_pieces.remove(piece)
                self.board.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = 0
                self.promote_piece(piece)
                piece.promote()

    
    def turn_check(self, piece):
        if self.turn == piece.colour:
            return True
        else:
            return False
    
    def turn_swap(self):
        self.turn_counter *= -1
        self.turn = TURN[self.turn_counter]
    
    def in_check(self):
        if self.turn == 'white':
            for piece in self.board.white_pieces:
                if piece.piece_type == 'king':
                    king = piece
        elif self.turn == 'black':
            for piece in self.board.black_pieces:
                if piece.piece_type == 'king':
                    king = piece
        return self.board.in_check(king)
    