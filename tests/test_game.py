import pytest
from domain.game import Game

def test_game_creation():
    game = Game()
    assert game.turn == 'white'
    assert len(game.board.grid) == 8

def test_pawn_game_creation():
    game = Game()
    game.pawn_game_creation()
    assert game.board.get_piece('a2').colour == 'white'
    assert game.board.get_piece('c7').colour == 'black'

def test_turn_alternation():
    game = Game()
    game.pawn_game_creation()
    with pytest.raises(ValueError):
        game.move_piece(game.bp1, 'a6')
    game.move_piece(game.wp1, 'a4')
    with pytest.raises(ValueError):
        game.move_piece(game.wp1, 'a5')