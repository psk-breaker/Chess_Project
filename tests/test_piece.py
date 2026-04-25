import pytest
from domain.piece import Piece, King, Queen, Bishop, Knight, Rook, Pawn
from domain.board import Board


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
        p.legal_move_check('e5', 0)
        p.move('e5')
    # Double square movement at start
    p.move('e4')
    # Only double square movement at start
    with pytest.raises(ValueError):
        p.legal_move_check('e6', 0)
        p.move('e6')
    
    # No lateral or backwards movements
    with pytest.raises(ValueError):
        p.legal_move_check('e4', 0)
        p.move('f4')
    with pytest.raises(ValueError):
        p.legal_move_check('f3', 0)
        p.move('f3')
    with pytest.raises(ValueError):
        p.legal_move_check('e3', 0)
        p.move('e3')

    # No movement onto occupied squares
    obstacle = Pawn('white', 'active', 'e5')
    b = Board()
    b.place_piece(p)
    b.place_piece(obstacle)
    with pytest.raises(ValueError):
        b.move_piece(p, 'e5')
    
    # Diagonal capture only - White
    enemy = Pawn('black', 'active', 'f5')
    b.place_piece(enemy)
    b.move_piece(p, 'f5')
    # Diagonal capture only - Black
    enemy = Pawn('black', 'active', 'g6')
    b.place_piece(enemy)
    b.move_piece(enemy, 'f5')
    assert b.get_piece('f5') == enemy
    # No pinned movement
    # Enpassant
    # Promotion => New piece instance with duplicated attribute info


# =======================================

def test_bishop_legal_move_check():
    b = Bishop("white", "active", "d4")
    with pytest.raises(ValueError):
        b.legal_move_check('d2')
        b.move
    with pytest.raises(ValueError):
        b.legal_move_check('d5')
    with pytest.raises(ValueError):
        b.legal_move_check('c4')
    with pytest.raises(ValueError):
        b.legal_move_check('e4')
    with pytest.raises(ValueError):
        b.legal_move_check('e6')

    
