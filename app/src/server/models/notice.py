#Noda'sCode
#このコードで実装する事

#noticeID:Int 識別ID
#adminID:String 通知者のID
#title:String 通知タイトル
#content:String 本文内容


from sqlalchemy import VARCHAR, CHAR
from flask_marshmallow.fields import fields
from server.database import db, ma

class User(db.Model):
    __tablename__ = 'notice'

    noticeID = db.Column(int(255), primary_key=True)
    adminID = db.Column(VARCHAR(255), nullable=False)
    title = db.Column(VARCHAR(255), nullable=False)
    content = db.Column(VARCHAR(255), nullable=False)

    def __init__(self, noticeID, adminID):
        self.noticeID = noticeID
        self.adminID = adminID

    def __repr__(self):
        return "<User(id='%s', password='%s')>" % (
            self.id,
            self.password
        )