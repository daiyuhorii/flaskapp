from server.database import db, ma
from sqlalchemy import VARCHAR, INTEGER, TEXT

class SubjectSchedule(db.Model):
    __tablename__ = "subjectSchedule"

    id = db.Column(INTEGER, nullable=False, primary_key=True)
    title = db.Column(VARCHAR(255), nullable=False)
    content = db.Column(TEXT, nullable=False)

    def __init__(id, title, content):
        self.id = id
        self.title = title
        self.content = content
    
    def get(self):
        pass
    