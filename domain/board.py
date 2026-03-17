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
    
    def place_piece(self, piece):
        rank = -int(piece.location[1])
        file = FILE.index(piece.location[0])
        self.grid[rank][file] = piece

    def get_piece(self, square):
        rank = -int(square[1])
        file = FILE.index(square[0])
        return self.grid[rank][file]