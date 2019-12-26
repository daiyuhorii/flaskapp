from flask import Flask, Response, request, render_template
from flask_restful import Api
from .database import init_db, db
from . import hoge
from .apis import UserAPI, Student_API, Student
from flask_login import LoginManager, login_required, logout_user
from hashlib import sha256
from .login import Auth


def create_app():
    # create flask app, enable it to read a relatvie path to config.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('server.config.default.Config')

    # initializes MySQL database and login auth.
    app.secret_key = sha256("teamnull".encode('utf-8')).digest()
    init_db(app)

    login_manager = LoginManager(app)
    @login_manager.user_loader
    def load_user(user_id):
        load_user = db.session.query(Student)\
                    .filter(Student.user_id == user_id).first()
        return load_user

    @app.route('/')
    def index():
        return Response('''
        home: <a href='/login'>Login</a>
        <a href='/protected/'>Protected</a>
        <a href='/logout'>Logout</a>"
        ''')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            return 'login post.'

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return Response('''
            logout success!<br />
            <a href="/login">login</a>
        ''')

    @app.route('/protected/')
    @login_required
    def protected():
        return Response('''
            You are now logged in!<br />
            <a href="/logout">logout</a>
        ''')

    # create an Api object and append WebAPI resource URIs.
    api = Api(app)

    api.add_resource(UserAPI, '/users')
    api.add_resource(Student_API, '/students')
    api.add_resource(Auth, '/auth')

    # delete this when apis are made
    blueprints = [hoge]
    for blueprint in blueprints:
        app.register_blueprint(blueprint.app)

    return app


app = create_app()
