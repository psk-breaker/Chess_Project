class Piece:


    def __init__(self, colour, piece_type):
        self.colour = colour
        self.piece_type = piece_type

    def __str__(self):
        return f'{self.colour} {self.piece_type}'

    def __repr__(self):
        return f'Piece({self.colour!r}, {self.piece_type!r})'