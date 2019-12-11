from sqlalchemy import VARCHAR, CHAR, INTEGER
from flask_marshmallow.fields import fields
from server.database import db, ma

class Subject(db.Model):
    __tablename__ = 'subject'
    
    subjectID = db.Column(VARCHAR(255), primary_key=True)
    subjectName = db.Column(VARCHAR(255))
    day = db.Column(CHAR(1), nullable=False)
    time = db.Column(INTEGER, nullable=False)
    room = db.Column(VARCHAR(255), nullable=False)
    
    def __init__(self, subjectID, subjectName, day, time, room):
        self.subjectID = subjectID
        self.subjectName = subjectName
        self.day = day
        self.time = time
        self.room = room
        
class SubjectSchema(ma.ModelSchema):
    class Meta:
        model = Subject
    