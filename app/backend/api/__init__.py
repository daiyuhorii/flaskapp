from flask import Flask, make_response, jsonify
from .views.router import user_router
from flask_cors import CORS
from .database import db
import config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_router, url_prefix="/api")
    CORS(app)

    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(user_router, url_prefix='/api')
    app.config['URI'] = config.Config.URI
    return app

app = create_app()