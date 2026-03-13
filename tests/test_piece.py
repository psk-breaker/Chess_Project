from domain.piece import Piece


def test_piece_initialisation():
    pawn = Piece('white', 'pawn')
    assert pawn.colour == 'white'
    assert pawn.name == 'pawn'

def test_piece_representation():
    pawn = Piece('black', 'pawn')
    assert str(pawn) == 'black pawn'