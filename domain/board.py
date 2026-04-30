FILE = 'abcdefgh'
RANK = '12345678'

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
        available = self.available_moves(piece)
        
        if occupancy == piece.colour:
           raise ValueError(f"Can't take own pieces") 
        
        elif piece.legal_move_check(target, occupancy) and target in available:
            if occupancy == 0:
                print(f'You just made the move {piece.location} to {target}')
                self.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = 0
                piece.move(target)
                self.grid[rank][file] = piece  
    
            elif occupancy != piece.colour:
                if piece.capture_rule(target):
                    print(f'You just captured from {piece.location} to {target}')
                    self.remove_piece(target)
                    self.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = 0
                    piece.move(target)
                    self.grid[-int(piece.location[1])][FILE.index(piece.location[0])] = piece             

    def occupied_square(self, target):
        piece = self.get_piece(target)
        if piece != 0:
            return piece.colour
        elif piece == 0:
            return 0

    def available_moves(self, piece):
        if piece == 0:
            return
        available = []
        rank = 8
        for row in self.grid:
            j = -1
            for square in row:
                j += 1
                occupancy = square.colour if square != 0 else 0
                file =  FILE[j]
                target = file + str(rank)
                legal = False
                try:
                    legal = piece.legal_move_check(target, occupancy)
                except ValueError:
                    pass
                if legal and occupancy != piece.colour:
                    available.append(target)
            rank -= 1
        
        unblocked_squares = self.blocked_check(piece) 

        true_available_squares = []  
        for square in available:
            if square in unblocked_squares:
                true_available_squares.append(square)
        print(f'Available squares to move to: {true_available_squares}')    
        
        return true_available_squares
    
    
    def blocked_check(self, piece):
        unblocked_squares = []

        if piece.piece_type == 'pawn':
            result = self.unblocked_pawn_moves(piece)
            for square in result:
                unblocked_squares.append(square)
            print(unblocked_squares)
            return unblocked_squares
        if piece.piece_type == 'night':
            result = self.unblocked_knight_moves(piece)
            for square in result:
                unblocked_squares.append(square)
            return unblocked_squares
        if piece.piece_type == 'king':
            result = self.unblocked_king_moves(piece)
            for square in result:
                unblocked_squares.append(square)
            return unblocked_squares
        if piece.piece_type == 'queen' or piece.piece_type == 'rook':
            result = self.unblocked_cardinal_moves(piece)
            for square in result:
                unblocked_squares.append(square)

        if piece.piece_type == 'queen' or piece.piece_type == 'bishop':
            result = self.unblocked_ordinal_moves(piece)
            for square in result:
                unblocked_squares.append(square)

        print(unblocked_squares)
        return unblocked_squares
    
    def check_square_result(self, piece, check_square):
        check_square_result = self.get_piece(check_square)
        if check_square_result != 0:
            if check_square_result.colour == piece.colour:
                return None
            elif check_square_result.colour != piece.colour:
                return check_square
        elif check_square_result == 0:
            return check_square

    def unblocked_pawn_moves(self, piece):
        unblocked_squares = []
        file = FILE.index(piece.location[0])
        rank = int(piece.location[1])

        # up
        if piece.colour == 'white':
            for i in range(2):
                rank += 1
                check_square = FILE[file] + str(rank)
                print(f'check this square: {check_square}')
                try:
                    check_square_result = self.check_square_result(piece, check_square)
                    if check_square_result != None:
                        unblocked_squares.append(check_square_result)
                except:
                    pass
            # capture
            file = FILE.index(piece.location[0])
            rank = int(piece.location[1])
            # left
            if file >= 1:
                rank += 1
                check_square = FILE[file - 1] + str(rank)
                print(f'check this square: {check_square}')
                check_square_result = self.check_square_result(piece, check_square)
                if check_square_result != None:
                    unblocked_squares.append(check_square_result)
            file = FILE.index(piece.location[0])
            rank = int(piece.location[1])
            # right
            if file <= 6:
                rank += 1
                check_square = FILE[file + 1] + str(rank)
                check_square_result = self.check_square_result(piece, check_square)
                if check_square_result != None:
                    unblocked_squares.append(check_square_result)

        # down
        elif piece.colour == 'black':
            for i in range(2):
                rank -= 1
                check_square = FILE[file] + str(rank)
                print(f'check this square: {check_square}')
                check_square_result = self.check_square_result(piece, check_square)
                if check_square_result != None:
                    unblocked_squares.append(check_square_result)
            
            # capture
            file = FILE.index(piece.location[0])
            rank = int(piece.location[1])
            # left
            if file >= 1 and rank >= 2:
                rank -= 1
                check_square = FILE[file - 1] + str(rank)
                check_square_result = self.check_square_result(piece, check_square)
                if check_square_result != None:
                    unblocked_squares.append(check_square_result)
            
            file = FILE.index(piece.location[0])
            rank = int(piece.location[1])
            # right
            if file <= 6 and rank >= 2:
                rank -= 1
                check_square = FILE[file + 1] + str(rank)
                check_square_result = self.check_square_result(piece, check_square)
                if check_square_result != None:
                    unblocked_squares.append(check_square_result)
        
        return unblocked_squares

    def unblocked_cardinal_moves(self, piece):
        unblocked_squares = []
        # Up
        for rank in range(int(piece.location[1]) +1, 9):
            check_square = piece.location[0] + str(rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)
        
        # down
        for rank in range(int(piece.location[1]) -1, 0, -1):
            check_square = piece.location[0] + str(rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)
        
        # left
        for file_index in range((FILE.index(piece.location[0]) -1), -1, -1):
            check_square = FILE[file_index] + piece.location[1]
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)

        # right   
        for file_index in range((FILE.index(piece.location[0]) +1), 8):
            check_square = FILE[file_index] + piece.location[1]
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)
        
        return unblocked_squares
    
    def unblocked_ordinal_moves(self, piece):
        unblocked_squares = []

        #diagonals check
        # bottom right
        piece_file = piece.location[0]
        piece_rank = int(piece.location[1])
        i = FILE.index(piece_file)
        j = piece_rank
        while i < 7 and j > 1:
            try:
                check_file = FILE[i + 1]  
            except:
                print(f'Error blocked_check: bottom right')
                break
            check_rank = str(j - 1)
            check_square = check_file + check_rank 
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    break
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check_square_result == 0:
                unblocked_squares.append(check_square) 
            i += 1
            j -= 1
        
        # bottom left 
        piece_file = piece.location[0]
        piece_rank = int(piece.location[1])
        i = FILE.index(piece_file)
        j = piece_rank
        while i > 0 and j > 1:
            try:
                check_file = FILE[i - 1]  
            except:
                print(f'Error blocked_check: bottom left')
                break
            check_rank = str(j - 1)
            check_square = check_file + check_rank 
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    break
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check_square_result == 0:
                unblocked_squares.append(check_square) 
            i -= 1
            j -= 1
        
        # diagonal up top right h8
        piece_file = piece.location[0]
        piece_rank = int(piece.location[1])
        i = FILE.index(piece_file)
        j = piece_rank
        while i < 7 and j < 8:
            try:
                check_file = FILE[i + 1]  
            except:
                print(f'Error blocked_check: top right')
                break
            check_rank = str(j + 1)
            check_square = check_file + check_rank 
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    break
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check_square_result == 0:
                unblocked_squares.append(check_square) 
            i += 1
            j += 1
      
        # top left a8
        piece_file = piece.location[0]
        piece_rank = int(piece.location[1])
        i = FILE.index(piece_file)
        j = piece_rank
        while i > 0 and j < 8:
            try:
                check_file = FILE[i - 1]  
            except:
                print(f'Error blocked_check: top left')
                break
            check_rank = str(j + 1)
            check_square = check_file + check_rank 
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    break
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check_square_result == 0:
                unblocked_squares.append(check_square) 
            i -= 1
            j += 1
        
        return unblocked_squares

    def unblocked_knight_moves(self, piece):
        unblocked_squares = []
        # knight moves
        file = FILE.index(piece.location[0])
        rank = int(piece.location[1])
        # top left
        if file >= 1 and rank <= 6:
            target_file = FILE[file - 1]
            target_rank = rank + 2
            check_square = target_file + str(target_rank)
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # top right
        if file <= 6 and rank <= 6:
            target_file = FILE[file + 1]
            target_rank = rank + 2
            check_square = target_file + str(target_rank)
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # upper left
        if file >=2 and rank <= 7:
            target_file = FILE[file - 2]
            target_rank = rank + 1
            check_square = target_file + str(target_rank)
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
            elif check_square_result == 0:
                unblocked_squares.append(check_square)

        # upper right
        if file <= 5 and rank <=7:
            result = self.knight_checker(piece, file, rank, 2, 1)
            for squares in result:
                unblocked_squares.append(squares)
        
        # lower left
        if file >= 2 and rank >= 2:
            result = self.knight_checker(piece, file, rank, -2, -1)
            for squares in result:
                unblocked_squares.append(squares)
        
        # lower right
        if file <= 5 and rank >= 2:
            result = self.knight_checker(piece, file, rank, 2, -1)
            for squares in result:
                unblocked_squares.append(squares)
        
        # bottom left
        if file >= 1 and rank >= 3:
            result = self.knight_checker(piece, file, rank, -1, -2)
            for squares in result:
                unblocked_squares.append(squares)
        
        # bottom right
        if file <= 6 and rank >= 3:
            result = self.knight_checker(piece, file, rank, 1, -2)
            for squares in result:
                unblocked_squares.append(squares)

        return unblocked_squares
    
    def knight_checker(self, piece, file, rank, i, j):
        unblocked_squares = []
        target_file = FILE[file + i]
        target_rank = rank + j
        check_square = target_file + str(target_rank)
        check_square_result = self.get_piece(check_square)
        if check_square_result != 0:
            if check_square_result.colour == piece.colour:
                pass
            elif check_square_result.colour != piece.colour:
                unblocked_squares.append(check_square)
        elif check_square_result == 0:
            unblocked_squares.append(check_square)
        return unblocked_squares
    
    def unblocked_king_moves(self, piece):
        unblocked_squares = []
        file = FILE.index(piece.location[0])
        rank = int(piece.location[1])

        # up
        if rank <= 7:
            target_file = FILE[file]
            target_rank = str(rank + 1)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # down
        if rank >= 2:
            target_file = FILE[file]
            target_rank = str(rank - 1)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # left
        if file >= 1:
            target_file = FILE[file - 1]
            target_rank = str(rank)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)

        # right   
        if file <= 6:
            target_file = FILE[file + 1]
            target_rank = str(rank)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # diags
        # top left
        if file >= 1 and rank <= 7:
            target_file = FILE[file - 1]
            target_rank = str(rank + 1)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # top right
        if file <= 6 and rank <= 7:
            target_file = FILE[file + 1]
            target_rank = str(rank + 1)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # bottom left
        if file >= 1 and rank >= 2:
            target_file = FILE[file - 1]
            target_rank = str(rank - 1)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # bottom right
        if file <= 6 and rank >= 2:
            target_file = FILE[file + 1]
            target_rank = str(rank - 1)
            check_square = target_file + target_rank
            check_square_result = self.get_piece(check_square)
            if check_square_result != 0:
                if check_square_result.colour == piece.colour:
                    pass
                elif check_square_result.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    pass
            elif check_square_result == 0:
                unblocked_squares.append(check_square)
        
        # castling left

        #castling right

        unblocked = []
        for square in unblocked_squares:
            result = self.threat_detection(piece, square)
            if result == False:
                unblocked.append(square)
            elif result == True:
                print(f'{square} is dangerous to move to')
        return unblocked

    def threat_detection(self, king, square):
        result = False
        threat = False
        nearest_pieces = []

        # cardinal check for queen and rook
        # Up
        for rank in range(int(square[1]) +1, 9):
            if len(nearest_pieces) == 2:
                break
            check_square = square[0] + str(rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'rook':
                        threat = True
                        break
                    else:
                        break
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True
            
        
        threat = False
        nearest_pieces = []

        # down
        for rank in range(int(square[1]) -1, 0, -1):
            if len(nearest_pieces) == 2:
                break
            check_square = square[0] + str(rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'rook':
                        threat = True
                        break
                    else:
                        break
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True

        threat = False
        nearest_pieces = []

        # left
        for file_index in range((FILE.index(square[0]) -1), -1, -1):
            if len(nearest_pieces) == 2:
                break
            check_square = FILE[file_index] + square[1]
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'rook':
                        threat = True
                        break
                    else:
                        break
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True

        threat = False
        nearest_pieces = []

        # right   
        for file_index in range((FILE.index(square[0]) +1), 8):
            if len(nearest_pieces) == 2:
                break
            check_square = FILE[file_index] + square[1]
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'rook':
                        threat = True
                        break
                    else:
                        break
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True

        threat = False
        nearest_pieces = []

        # ordinal check for queen and bishop

        #diagonals check
        # find threats coming from bottom right
        i = FILE.index(square[0])
        j = int(square[1])
        while i < 7 and j > 1:
            if len(nearest_pieces) == 2:
                break
            try:
                check_file = FILE[i + 1]  
            except:
                print(f'Error blocked_check: bottom right')
                break
            check_rank = str(j - 1)
            check_square = check_file + check_rank 
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'bishop':
                        threat = True
                        break
                    else:
                        break
            i += 1
            j -= 1
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True 
        threat = False
        nearest_pieces = []

        # threats coming from bottom left 
        i = FILE.index(square[0])
        j = int(square[1])
        while i > 0 and j > 1:
            if len(nearest_pieces) == 2:
                break
            try:
                check_file = FILE[i - 1]  
            except:
                print(f'Error blocked_check: bottom left')
                break
            check_rank = str(j - 1)
            check_square = check_file + check_rank 
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'bishop':
                        threat = True
                        break
                    else:
                        break 
            i -= 1
            j -= 1
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True
        threat = False
        nearest_pieces = []

        # threats from top right h8
        i = FILE.index(square[0])
        j = int(square[1])
        while i < 7 and j < 8:
            if len(nearest_pieces) == 2:
                break
            try:
                check_file = FILE[i + 1]  
            except:
                print(f'Error blocked_check: top right')
                break
            check_rank = str(j + 1)
            check_square = check_file + check_rank 
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'bishop':
                        threat = True
                        break
                    else:
                        break 
            i += 1
            j += 1
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True
        threat = False
        nearest_pieces = []

        # threats top left a8
        i = FILE.index(square[0])
        j = int(square[1])
        while i > 0 and j < 8:
            if len(nearest_pieces) == 2:
                break
            try:
                check_file = FILE[i - 1]  
            except:
                print(f'Error blocked_check: top left')
                break
            check_rank = str(j + 1)
            check_square = check_file + check_rank 
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == king.colour and check != king:
                    nearest_pieces.append(check)
                elif check.colour != king.colour:
                    if check.piece_type == 'queen' or check.piece_type == 'bishop':
                        threat = True
                        break
                    else:
                        break  
            i -= 1
            j += 1
        if threat == True and len(nearest_pieces) == 0:
            result = True
        if threat== True and len(nearest_pieces) == 1:
            nearest_pieces[0].pinned = True

        threat = False
        nearest_pieces = []

        # knight check
    
        file = FILE.index(square[0])
        rank = int(square[1])
        # top left
        if file >= 1 and rank <= 6:
            target_file = FILE[file - 1]
            target_rank = rank + 2
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
                        
        if threat == True:
            result = True

        threat = False
        
        file = FILE.index(square[0])
        rank = int(square[1])
        # top right
        if file <= 6 and rank <= 6:
            target_file = FILE[file + 1]
            target_rank = rank + 2
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
        if threat == True:
            result = True

        threat = False

        # upper left
        if file >=2 and rank <= 7:
            target_file = FILE[file - 2]
            target_rank = rank + 1
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
        if threat == True:
            result = True

        threat = False
        # upper right
        if file <= 5 and rank <=7:
            target_file = FILE[file + 2]
            target_rank = rank + 1
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
        if threat == True:
            result = True
        threat = False

        # lower left
        if file >= 2 and rank >= 2:
            target_file = FILE[file - 2]
            target_rank = rank - 1
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
        if threat == True:
            result = True
        threat = False

        # lower right
        if file <= 5 and rank >= 2:
            target_file = FILE[file + 2]
            target_rank = rank - 1
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
        if threat == True:
            result = True
        threat = False

        # bottom left
        if file >= 1 and rank >= 3:
            target_file = FILE[file - 1]
            target_rank = rank - 2
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
        if threat == True:
            result = True
        threat = False
        
        # bottom right
        if file <= 6 and rank >= 3:
            target_file = FILE[file + 1]
            target_rank = rank - 2
            check_square = target_file + str(target_rank)
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour:
                    if check.piece_type == 'night':
                        threat = True
        if threat == True:
            result = True
        threat = False
        
        # pawn check
        
        # white pawn attacking top left
        file = FILE.index(square[0])
        rank = int(square[1])
        if file < 7 and rank > 2:
            target_file = FILE[file + 1]
            target_rank = str(rank - 1)
            check_square = target_file + target_rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour and check.colour == 'white':
                    if check.piece_type == 'pawn':
                        threat = True
        if threat == True:
            result = True
        threat = False    

        # white pawn attacking top right
        if file > 0 and rank > 2:
            target_file = FILE[file - 1]
            target_rank = str(rank - 1)
            check_square = target_file + target_rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour and check.colour == 'white':
                    if check.piece_type == 'pawn':
                        threat = True
        if threat == True:
            result = True
        threat = False

        # black pawn attacking bottom left
        if file < 7 and rank < 7:
            target_file = FILE[file + 1]
            target_rank = str(rank + 1)
            check_square = target_file + target_rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour and check.colour == 'black':
                    if check.piece_type == 'pawn':
                        threat = True
        if threat == True:
            result = True
        threat = False

        # black pawn attacking bottom right
        if file > 0  and rank < 7:
            target_file = FILE[file - 1]
            target_rank = str(rank + 1)
            check_square = target_file + target_rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour != king.colour and check.colour == 'black':
                    if check.piece_type == 'pawn':
                        threat = True
        if threat == True:
            result = True
        # king check

        return result
        
# end