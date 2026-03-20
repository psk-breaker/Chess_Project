FILE = 'abcdefgh'

class Board:

    def __init__(self):
        self.grid = []
        square = 0
        rank = []
        for i in range(8):
            for i in range(8):
                rank.append(square)
            self.grid.append(rank)
            rank = []

    def list_board(self):
        nice_board = []
        row = []
        for rank in self.grid:
            row = []
            for square in rank:
                if square == 0:
                    row.append('')
                else:
                    notation = f'{square.colour[0]}{square.piece_type[0]}'
                    row.append(notation)
            nice_board.append(row)
        return nice_board

    def print_pretty_board(self):
        nice_board = self.list_board()
        for rank in nice_board:
            print(rank)

    def place_piece(self, piece):
        rank = -int(piece.location[1])
        file = FILE.index(piece.location[0])
        self.grid[rank][file] = piece

    def get_piece(self, square):
        rank = -int(square[1])
        file = FILE.index(square[0])
        return self.grid[rank][file]
    
    def remove_piece(self, square):
        rank = -int(square[1])
        file = FILE.index(square[0])
        piece = self.grid[rank][file]
        if piece != 0:
            piece.location = 'j0'
            self.grid[rank][file] = 0
    
    def move_piece(self, piece, target):
        rank = -int(target[1])
        file = FILE.index(target[0])
        occupancy = self.occupied_square(target)
        if occupancy == 0 and piece.legal_move_check(target, occupancy):
            self.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = 0
            piece.move(target)
            self.grid[rank][file] = piece
    
        elif occupancy == piece.colour:
            raise ValueError(f"Can't take own pieces")

        elif occupancy != piece.colour:
            if piece.capture_rule(target):
                self.remove_piece(target)
                self.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = 0
                piece.move(target)
                self.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = piece

    def occupied_square(self, target):
        rank = -int(target[1])
        file = FILE.index(target[0])
        piece = self.grid[rank][file]
        if piece != 0:
            return piece.colour
        elif piece == 0:
            return 0
    

    

    