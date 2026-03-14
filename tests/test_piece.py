from domain.piece import Piece


def test_piece_initialisation():
    pawn = Piece('white', 'pawn')
    assert pawn.colour == 'white'
    assert pawn.piece_type == 'pawn'

def test_piece_representation():
    pawn = Piece('black', 'pawn')
    assert repr(pawn) == "Piece('black', 'pawn')"

def test_piece_str():
    pawn = Piece('black', 'pawn')
    assert str(pawn) == 'black pawn'