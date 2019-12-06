from flask import Flask
from flask_restful import Api
from .database import init_db
from . import hoge
from .apis import UserAPI
def create_app():
    # create flask app, enable it to read a relatvie path to config.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('server.config.default.Config')
    
    # initialize MySQL database.
    init_db(app)

    # create an Api object and append WebAPI resource URIs.
    api = Api(app)
    # e.g. 
    api.add_resource(UserAPI, '/users')

    # delete this when apis are made
    blueprints = [hoge]
    for blueprint in blueprints:
        app.register_blueprint(blueprint.app)
    
    return app


app = create_app()
