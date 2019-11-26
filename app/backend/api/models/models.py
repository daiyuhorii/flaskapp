# api/models/models.py
from sqlalchemy import Column, BIGINT, VARCHAR,  TEXT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# User table schema
class User(Base):
    __tablename__ = 'User'
    id = Column(BIGINT(), primary_key=True, nullable=False)
    name = Column(VARCHAR(40), nullable=False)
    password = Column(VARCHAR(40), nullable=False)

    def __repr__(self):
        return "<id: '%d', name: '%s', password: '%s'>" % (
            self.id, self.name, self.password
        )
    
# article table schema
class Article(Base):
    __tablename__ = "article"

    articleID = Column(BIGINT(), primary_key=True, nullable=False)
    authorID = Column(BIGINT(), ForeignKey(User.id), nullable=False)
    title = Column(VARCHAR(40), nullable=True)
    content = Column(TEXT, nullable=True)

    def __repr__(self):
        return "<Article(articleID='%d', authorID='%d', title='%s', content='%s')>" % (
            self.articleID, self.authorID, self.title, self.content)
