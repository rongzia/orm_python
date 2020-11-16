import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String #区分大小写
from sqlalchemy.orm import sessionmaker

#创建连接
# engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/test',encoding='utf-8',echo=True)

db_session_class = sessionmaker(bind=engine)    # db_session_class 仅仅是一个类
session = db_session_class()                    # 实例化一个对象

from create_table import User
user_obj = User(username='xiaoming', password='123456');
session.add(user_obj)
user_obj = User(username='xiaowang', password='123456');
session.add(user_obj)
user_obj = User(username='xiaoli', password='123456');
session.add(user_obj)
session.commit()                                #提交，使前面修改的数据生效。
