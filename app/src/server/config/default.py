
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


class MysqlConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@"\
        "{host}/{database}?charset=utf8".format(
            **{
                'user': 'root',
                'password': 'teamnull',
                'host': os.getenv('DB_HOST', 'flaskapp_mysql_1:3306'),
                'database': 'db2019'
            }
        )
    ENGINE = create_engine(SQLALCHEMY_DATABASE_URI, encoding='utf-8',
                           echo=True)

    SESSION = scoped_session(
        sessionmaker(
            bind=ENGINE,
            autocommit=False,
            autoflush=False
        ))
    Session = SESSION()

    Base = declarative_base()
    Base.query = SESSION.query_property()


Config = MysqlConfig
