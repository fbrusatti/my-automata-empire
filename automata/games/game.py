from marshmallow import Schema, fields


class Game(object):
    def __init__(self, name, level='Low'):
        self.name = name
        self.level = level
        self.board = [
            [[''], [''], [''], ['']],
            [[''], [''], [''], ['']]
        ]

    def getAll():
        return mockdb

    def find(id):
        return mockdb[id]

    def append(game):
        mockdb[id] = game

        return True

    def __repr__(self):
        return self.name

    def json(self):
        return {
            'name': self.name,
            'id': self.id,
            'level': self.level,
            'board': self.board
        }


mockdb = {
    1: Game(**{'name': 'First game', 'level': 'Low'}),
    2: Game(**{'name': 'Second game', 'level': 'High'}),
    3: Game(**{'name': 'Third game', 'level': 'Medium'})
}


class GameSchema(Schema):
    # _id = fields.Str()
    name = fields.Str()
    level = fields.Str()
    board = fields.List(fields.List(fields.List(fields.List(fields.Str()))))
