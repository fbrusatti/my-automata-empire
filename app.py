import os
from automata import create_app
from automata import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(debug=True)

    with app.app_context():
        db.create_all()
        for rule in app.url_map.iter_rules():
            print(rule)
