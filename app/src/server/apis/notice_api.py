#Noda'sCode

from flask_restful  import Resource, reqparse, abort
from flask import jsonify

from server.models import User, UserSchema
from server.database import db

class NoticeAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('noticeID', required=True)
        self.reqparse.add_argument('adminID', required=True)
        self.reqparse.add_argument('title', required=True)
        self.reqparse.add_argument('content', required=True)

        super(NoticeAPI, self).__init__()
    
    def get(self):
        users = db.session.query(User).all()
        if users == None:
            abort(404)
        
        jsondata = UserSchema(many=True).dump(users)
        return jsonify({'items': jsondata})