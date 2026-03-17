import pytest
from domain.board import Board
from domain.piece import Pawn

def test_board_is_8x8():
    b = Board()
    assert len(b.grid) == 8
    for rank in b.grid:
        assert len(rank) == 8

def test_place_piece_on_board():
    b = Board()
    p = Pawn('white', 'active', 'e2')
    b.place_piece(p)
    assert b.grid[6][4] == p