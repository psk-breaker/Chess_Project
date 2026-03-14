from domain.piece import Piece


def test_piece_initialisation():
    pawn = Piece('white', 'pawn', 'active', 'e2')
    assert pawn.colour == 'white'
    assert pawn.piece_type == 'pawn'
    assert pawn.life == 'active'
    assert pawn.location == 'e2'
    assert pawn.move_history is None

def test_piece_representation():
    pawn = Piece('black', 'pawn', 'captured', 'j0')
    assert repr(pawn) == "Piece('black', 'pawn', 'captured', 'j0')"

def test_piece_str():
    pawn = Piece('black', 'pawn', 'active', 'e7')
    assert str(pawn) == 'black pawn active e7'

def test_all_piece_subclasses_initialising():
    assert str(King('white', 'king', 'active', 'e1')) == 'white king active e1'
    assert str(Queen('white', 'queen', 'active', 'd1')) == 'white queen active d1'
    assert str(Bishop('white', 'bishop', 'active', 'c1')) == 'white bishop active c1'
    assert str(Knight('white', 'knight', 'active', 'b1')) == 'white knight active b1'
    assert str(Rook('white', 'rook', 'active', 'a1')) == 'white rook active a1'
