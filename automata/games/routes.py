from flask import jsonify, request
from automata.games import api
from automata.games.game import Game, GameSchema
from automata import db
from flask_restful import Resource


class GameResource(Resource):
    def get(self, game_id):
        game_schema = GameSchema()

        game = Game.query.filter_by(id=game_id).first()

        return jsonify(game_schema.dump(game))

    def post(self):
        data = request.json

        game_data = {
            'name': data.get('name'),
            'level': data.get('level', 'Random')
        }

        game_schema = GameSchema()
        # Validate with schema
        game = Game(**game_schema.load(game_data))

        # Game.append(game)
        db.session.add(game)
        db.session.commit()

        return jsonify({'success': 'true'})

    def index(self):
        return jsonify({"success": "false"})
        # game_data = []
        # game_schema = GameSchema()

        # for game in Game.getAll():
        #     game_data.append(game_schema.dump(game))

        # return jsonify({"games": game_data})


# api.add_resource(GameResource, '/', '/<int:game_id>')
api.add_resource(GameResource, '/', '/<int:game_id>', '/')
