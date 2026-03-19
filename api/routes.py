from flask import Blueprint, jsonify, request, render_template
from domain.game import Game

api = Blueprint('api', __name__)

game = Game()
game.pawn_game_creation()

@api.route('/')
def index():
    return render_template('index.html')


@api.route('/board', methods=['GET'])
def get_board():
    return jsonify(game.board.list_board())


@api.route('/move', methods=['POST'])
def make_move():
    data = request.json
    start = data['start']
    end = data['end']

    try:
        game.make_move(start, end)
        game.board.print_pretty_board() # Debugging back-end
        return jsonify({'status': 'ok'})
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)})
    
