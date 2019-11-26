from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from userclass import User
import json
from collections import OrderedDict

DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    "testuser",
    "testuser",
    "localhost",
    "db20191129",
)
url = 'mysql+pymysql://root:horiid@localhost/db20191129'
engine = create_engine(DATABASE, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
result = session.query(User).all()
#sql = 'SELECT * FROM user'
#result = engine.execute(sql)
data = {}
for user in result:
    print(user.id, user.name, user.password)
    data[user.id] = {"name": user.name, "password": user.password}

with open('result.json', "w") as outf:
    json.dump(data, outf, indent=4, separators=(',', ':'))

print("\nDATA EXTRACTION COMPLETE.")
session.close()