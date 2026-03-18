import pytest
from domain.game import Game

def test_game_creation():
    game = Game()
    assert game.turn == 'white'
    assert len(game.board) == 8

