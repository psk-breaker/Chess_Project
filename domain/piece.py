class Piece:

    def __init__(self, colour, piece_type, life, location):
        self.colour = colour
        self.piece_type = piece_type
        self.life = life
        self.location = location
        self.move_history = None

    def __str__(self):
        return f'{self.colour} {self.piece_type} {self.life} {self.location}'

    def __repr__(self):
        return f'Piece({self.colour!r}, {self.piece_type!r}, {self.life!r}, {self.location!r})'


class King(Piece):
    def __init__(self, colour, piece_type, life, location):
        super().__init__(colour=colour, piece_type='king', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Queen(Piece):
    def __init__(self, colour, piece_type, life, location):
        super().__init__(colour=colour, piece_type='queen', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Bishop(Piece):
    def __init__(self, colour, piece_type, life, location):
        super().__init__(colour=colour, piece_type='bishop', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Knight(Piece):
    def __init__(self, colour, piece_type, life, location):
        super().__init__(colour=colour, piece_type='knight', life=life, location=location)
    
    def __str__(self):
        return super().__str__()
    

class Rook(Piece):
    def __init__(self, colour, piece_type, life, location):
        super().__init__(colour=colour, piece_type='rook', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Pawn(Piece):
    def __init__(self, colour, piece_type, life, location):
        super().__init__(colour=colour, piece_type='pawn', life=life, location=location)
    
    def __str__(self):
        return super().__str__()