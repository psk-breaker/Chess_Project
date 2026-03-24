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
        quit = False

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

        #diagonals check

        for i in range(int(piece.location[1]) -1, 1, -1):
            rank = str(i)
            i = int(piece.location[1]) - i
            print(f'i is {i}')
            try:
                file =  FILE[FILE.index(piece.location[0]) +i]
            except IndexError:
                break
            check_square = file + rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)
              
        for i in range(int(piece.location[1]) -1, 1, -1):
            rank = str(i)
            i = int(piece.location[1]) - i
            try:
                file =  FILE[FILE.index(piece.location[0]) -i]
            except IndexError:
                print(f'Outside of board: {i} and {rank}')
                break
            check_square = file + rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)
        
        # diagonal up
        for i in range(int(piece.location[1]) +1, 9):
            rank = str(i)
            i = i - int(piece.location[1])
            try:
                file =  FILE[FILE.index(piece.location[0]) +i]
            except IndexError:
                print(f'Outside of board: {i} and {rank}')
                break
            check_square = file + rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    print(f'h8 check {check} on {check_square}')
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)
        
        for i in range(int(piece.location[1]) +1, 8):
            rank = str(i)
            i = i - int(piece.location[1])
            try:
                file =  FILE[FILE.index(piece.location[0]) -i]
            except IndexError:
                print(f'Outside of board: {i} and {rank}')
                break
            check_square = file + rank
            check = self.get_piece(check_square)
            if check != 0:
                if check.colour == piece.colour:
                    break
                elif check.colour != piece.colour:
                    unblocked_squares.append(check_square)
                    break
            elif check == 0:
                unblocked_squares.append(check_square)

        print(unblocked_squares)
        return unblocked_squares