from flask import Flask
from . import hoge

app = Flask(__name__, instance_relative_config=True)

blueprints = [hoge]
for blueprint in blueprints:
    app.register_blueprint(blueprint.app)
