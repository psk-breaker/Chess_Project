import pytest
from domain.board import Board

def test_board_is_8x8():
    b = Board()
    assert len(b.grid) == 8
    for rank in b.grid:
        assert len(rank) == 8
    