import pytest
from domain.piece import Piece, King, Queen, Bishop, Knight, Rook, Pawn


def test_piece_initialisation():
    pawn = Piece('white', 'pawn', 'active', 'e2')
    assert pawn.colour == 'white'
    assert pawn.piece_type == 'pawn'
    assert pawn.life == 'active'
    assert pawn.location == 'e2'
    assert pawn.move_history == ['e2']

def test_piece_representation():
    pawn = Piece('black', 'pawn', 'captured', 'j0')
    assert repr(pawn) == "Piece('black', 'pawn', 'captured', 'j0')"

def test_piece_str():
    pawn = Piece('black', 'pawn', 'active', 'e7')
    assert str(pawn) == 'black pawn active e7'

def test_all_piece_subclasses_initialising():
    assert str(King('white', 'active', 'e1')) == 'white king active e1'
    assert str(Queen('white', 'active', 'd1')) == 'white queen active d1'
    assert str(Bishop('white', 'active', 'c1')) == 'white bishop active c1'
    assert str(Knight('white', 'active', 'b1')) == 'white knight active b1'
    assert str(Rook('white', 'active', 'a1')) == 'white rook active a1'
    assert str(Pawn('white', 'active', 'a2')) == 'white pawn active a2'

def test_move_piece_to_target():
    p = Pawn('white', 'active', 'e2')
    p.move('e3')
    assert p.location == 'e3'
    assert p.move_history == ['e2', 'e3']

def test_pawn_move_rules():
    p = Pawn('white', 'active', 'e2')
    # No triple square movement
    with pytest.raises(ValueError):
        p.move('e5')
    # Double square movement at start
    p.move('e4')
    # Only double square movement at start
    with pytest.raises(ValueError):
        p.move('e6')
    
    # No lateral or backwards movements
    with pytest.raises(ValueError):
        p.move('f4')
    with pytest.raises(ValueError):
        p.move('f3')
    with pytest.raises(ValueError):
        p.move('e3')

    # No movement onto occupied squares
    # obstacle = Pawn('white', 'active', 'e5')
    # with pytest.raises(ValueError):
    #    p.move('e5')

    # Diagonal capture only
    # No pinned movement
    # Enpassant
    # Promotion => New piece instance with duplicated attribute info
