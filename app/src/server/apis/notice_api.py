 #Noda'sCode
#このコードで実装する事

#noticeID:Int 識別ID
#adminID:String 通知者のID
#title:String 通知タイトル
#content:String 本文内容
#get,post,put,deliteの4メソッドに分けて、リソースクラスから継承するAPIクラス(APIsのリソース)にGETやPOSTメソッドが用意されている

from flask_restful import Resource, reqparse, abort
from flask import jsonify, request
from server.models import Notice, NoticeSchema
from server.database import db, Session

# define API associated with Student table.
class Notice_API(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('noticeID', required=True)
        self.parser.add_argument('adminID', required=True)
        super(Notice_API, self).__init__()

    def get(self):
        sess = db.session.query(Notice).all()
        if sess is None:
            return abort(400)
        else:
            data = NoticeSchema(many=True).dump(sess)
            return jsonify(data)

    def post(self):
        self.parser.parse_args()
        self.parser.add_argument('noticeID', required=True)
        self.parser.add_argument('adminID', required=True)

        # if content-type is not json, return 400
        if request.headers['Content-Type'] != 'application/json':
            return jsonify(res='error'), 400

        # check duplicates later
        req = request.get_json()
        notice_id = req['notice_id']
        print("received " + notice_id)
        admin_id = req['admin_id']
        print("received " + admin_id)
        notice = Notice(notice_id, admin_id)
        session = Session
        session.add(notice)
        session.commit()
        return req

