FILE = 'abcdefgh'


class Piece:

    def __init__(self, colour, piece_type, life, location):
        self.colour = colour
        self.piece_type = piece_type
        self.life = life
        self.location = location
        self.move_history = []
        self.move_history.append(location)

    def __str__(self):
        return f'{self.colour} {self.piece_type} {self.life} {self.location}'

    def __repr__(self):
        return f'Piece({self.colour!r}, {self.piece_type!r}, {self.life!r}, {self.location!r})'
    
    def move(self, target):
        self.location = target
        self.move_history.append(self.location)

class King(Piece):
    def __init__(self, colour, life, location):
        super().__init__(colour=colour, piece_type='king', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Queen(Piece):
    def __init__(self, colour, life, location):
        super().__init__(colour=colour, piece_type='queen', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Bishop(Piece):
    def __init__(self, colour, life, location):
        super().__init__(colour=colour, piece_type='bishop', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Knight(Piece):
    def __init__(self, colour, life, location):
        super().__init__(colour=colour, piece_type='knight', life=life, location=location)
    
    def __str__(self):
        return super().__str__()
    

class Rook(Piece):
    def __init__(self, colour, life, location):
        super().__init__(colour=colour, piece_type='rook', life=life, location=location)
    
    def __str__(self):
        return super().__str__()


class Pawn(Piece):
    def __init__(self, colour, life, location):
        super().__init__(colour=colour, piece_type='pawn', life=life, location=location)
    
    def __str__(self):
        return super().__str__()
    
    def legal_move_check(self, target):
        rank_check = 0
        if self.colour == 'white':
            rank_check = int(target[1]) - int(self.location[1])
        elif self.colour == 'black':
            rank_check = int(self.location[1]) - int(target[1])
        
        file_check = True if self.location[0] == target[0] else False

        if rank_check == 1:
            if file_check:
                # Just permitting a 1 rank move within file
                return True
        if rank_check == 2 and file_check:
            if self.starting_move_check(target):
                # Just permitting a double rank move for first move
                return True
        if rank_check >= 3:
            raise ValueError(f'Too many ranks crossed')
        if rank_check <= 0:
            raise ValueError(f'Try moving forward')
        if file_check == False:
            if self.capture_rule(target):
                return True
            else:
                raise ValueError(f'Crossing files without permission')

    def starting_move_check(self, target):
        if len(self.move_history) == 1:
            return True
        else:
            raise ValueError(f'Only possible on first move')
    
    def move(self, target):
        if self.legal_move_check(target):
            super().move(target)
    
    def capture_rule(self, target):
        target_rank = int(target[1])
        target_file = FILE.index(target[0])
        piece_rank = int(self.location[1])
        piece_file = FILE.index(self.location[0])

        if self.colour == 'white':
            if (target_rank - piece_rank) == 1:
                if abs(target_file - piece_file) == 1:
                    return True
            else:
                raise ValueError(f'Capture not possible: {target_rank} {piece_rank}')
        elif self.colour == 'black':
            if (target_rank - piece_rank) == -1:
                if abs(target_file - piece_file) == 1:
                    return True
            else:
                raise ValueError(f'Capture not possible')