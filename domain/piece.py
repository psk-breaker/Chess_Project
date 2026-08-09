FILE = 'abcdefgh'


class Piece:

    def __init__(self, colour, piece_type, location, id=None):
        self.colour = colour
        self.piece_type = piece_type
        self.id = id
        self.life = 'active'
        self.location = location
        self.pinned = False
        self.enemy = None
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
    def __init__(self, colour, location, id):
        super().__init__(colour=colour, piece_type='king', location=location, id=id)
    
    def __str__(self):
        return super().__str__()
    
    def legal_move_check(self, target, occupancy=0):
        # Occupancy irrelevant
        rank_check = abs(int(target[1]) - int(self.location[1]))
        file_check = abs(FILE.index(target[0]) - FILE.index(self.location[0]))
        
        # legal check for cardinal movement
        if rank_check == 1 and file_check == 0:
            return True
        elif rank_check == 0 and file_check == 1:
            return True
        
        # legal check for ordinal directions
        elif rank_check == 1 and file_check == 1:
            return True
        # if not within same rank or file, illegal move
        else:
            raise ValueError(f'King can not move to {target}')
    
    def move(self, target):
        super().move(target)
    
    def capture_rule(self, target):
        # King has no exclusive capture rule
        return True

    def castling_rule(self, target):
        if len(self.move_history) == 1:
            if self.colour == 'white':
                if target == 'c1' or target == 'g1':
                    return True
            elif self.colour == 'black':
                if target == 'c8' or target == 'g8':
                    return True
        return False


class Queen(Piece):
    def __init__(self, colour, location, id):
        super().__init__(colour=colour, piece_type='queen', location=location, id=id)
    
    def __str__(self):
        return super().__str__()

    def legal_move_check(self, target, occupancy):
        # Occupancy irrelevant
        rank_check = abs(int(target[1]) - int(self.location[1]))
        file_check = abs(FILE.index(target[0]) - FILE.index(self.location[0]))
        diagonal_check = file_check - rank_check
        
        # legal check for movement within same rank and file
        if rank_check == 0 or file_check == 0:
            return True
        # if not within same rank or file, diagonal check necessary
        if diagonal_check == 0:
            return True
        
        return False
        
    
    def move(self, target):
        super().move(target)
    
    def capture_rule(self, target):
        # Queen has no exclusive capture rule
        return True


class Bishop(Piece):
    def __init__(self, colour, location, id):
        super().__init__(colour=colour, piece_type='bishop', location=location, id=id)
    
    def __str__(self):
        return super().__str__()
    
    def legal_move_check(self, target, occupancy=0):
        # Occupancy irrelevant
        rank_check = abs(int(target[1]) - int(self.location[1]))
        file_check = abs(FILE.index(target[0]) - FILE.index(self.location[0]))
        diagonal_check = file_check - rank_check
        
        # Only a diagonal move is possible for a bishop
        if diagonal_check == 0:
            return True
        elif diagonal_check != 0:
            raise ValueError(f'Bishop can not move outside diagonals')
        
        return False
    
    def move(self, target):
        super().move(target)
    
    def capture_rule(self, target):
        # Bishop has no exclusive capture rule
        return True


class Knight(Piece):
    def __init__(self, colour, location, id):
        super().__init__(colour=colour, piece_type='night', location=location, id=id)
    
    def __str__(self):
        return super().__str__()
    
    def legal_move_check(self, target, occupancy=0):
        # Occupancy irrelevant
        file_check = abs(FILE.index(target[0]) - FILE.index(self.location[0]))
        rank_check = abs(int(target[1]) - int(self.location[1]))
        
        # vertical L move
        if file_check == 1 and rank_check == 2:
            return True
        # horizontal L move check
        elif file_check == 2 and rank_check == 1:
            return True
        else:
            raise ValueError(f'Knight can not move outside of Ls')
    
    def move(self, target):
        super().move(target)
    
    def capture_rule(self, target):
        # Knight has no exclusive capture rule
        return True
    

class Rook(Piece):
    def __init__(self, colour, location, id):
        super().__init__(colour=colour, piece_type='rook', location=location, id=id)
    
    def __str__(self):
        return super().__str__()
    
    def legal_move_check(self, target, occupancy=0):
        # Occupancy irrelevant
        rank_check = abs(int(target[1]) - int(self.location[1]))
        file_check = abs(FILE.index(target[0]) - FILE.index(self.location[0]))
        
        # legal check for movement within same rank and file
        if rank_check == 0 or file_check == 0:
            return True
        # if not within same rank or file, illegal move
        else:
            raise ValueError(f'Rook can not move to {target}')
    
    def move(self, target):
        super().move(target)
    
    def capture_rule(self, target):
        # Rook has no exclusive capture rule
        return True


class Pawn(Piece):
    def __init__(self, colour, location, id):
        super().__init__(colour=colour, piece_type='pawn', location=location, id=id)
        self.enpassant = False
    
    def __str__(self):
        return super().__str__()
    
    def legal_move_check(self, target, occupancy):
        # occupancy is a redundant feature with blocked_check
        rank_check = 0
        if self.colour == 'white':
            rank_check = int(target[1]) - int(self.location[1])
        elif self.colour == 'black':
            rank_check = int(self.location[1]) - int(target[1])
        
        file_check = True if self.location[0] == target[0] else False

        if rank_check == 1:
            if file_check and occupancy == 0:
                # Just permitting a 1 rank move within file
                return True
        if rank_check == 2 and file_check and occupancy == 0:
            if self.starting_move_check(target):
                # Just permitting a double rank move for first move
                return True
        if rank_check >= 3:
            raise ValueError(f'Too many ranks crossed: {rank_check}')
        if rank_check <= 0:
            raise ValueError(f'Try moving forward')
        if file_check == False:
            if self.capture_rule(target) and occupancy != 0:
                return True
            else:
                raise ValueError(f'illegal move')

    def starting_move_check(self, target):
        if len(self.move_history) == 1:
            return True
        else:
            raise ValueError(f'Only possible on first move')
    
    def move(self, target):
        self.enpassant_check(target)
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
        return False

    def enpassant_rule(self, target):
        return self.capture_rule(target)

    def enpassant_check(self, target):
        if abs(int(self.location[1]) - int(target[1])) == 2:
            self.enpassant = True
            print('Enpassantable!')

    def promotion_check(self, target):
        target_rank = int(target[1])
        if self.colour == 'white' and target_rank == 8:
            return True
        elif self.colour == 'black' and target_rank == 1:
            return True

        return False

    def promote(self):
        # promoted piece goes to heaven
        self.location = 'h1'