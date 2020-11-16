import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String #区分大小写
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

#创建连接
# engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/test',encoding='utf-8',echo=True)

db_session_class = sessionmaker(bind=engine)    # db_session_class 仅仅是一个类
session = db_session_class()                    # 实例化一个对象

from create_table import User
print (session.query(func.count(User.userid)).one()[0])  # 统计多少

query = session.query(User)
for i in query.all():
    print(i.userid, i.username, i.password)
