from flask_login import login_required, LoginManager, login_user, logout_user
from server.models import Student
from werkzeug.security import check_password_hash
from flask_restful import Resource


class Login_auth(Resource):
    student = Student()

    def __init__(student: Student, self):
        self.student = student

    def verify_password(password, self):
        if check_password_hash(self.student.password != password):
            return False
        else:
            return True

    # when received auth request
    def post():
        if verify_password():
            

    def logout():
        logout_user()
