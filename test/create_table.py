import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String #区分大小写

#创建连接
# engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/test',encoding='utf-8',echo=True)

#生成 orm 基类
base=declarative_base()
class User(base):
    __tablename__ = 'users'
    userid = Column('userid',Integer,primary_key=True,nullable=True)
    username = Column('username',String(64),nullable=True)
    password = Column('password',String(64),nullable=True)
base.metadata.create_all(engine) #创建表结构

# 默认主键为自增，会生成一个序列，查看数据库如下：
# test=# \d
#                     关联列表
#  架构模式 |       名称       |  类型  |  拥有者
# ----------+------------------+--------+----------
#  public   | users            | 数据表 | postgres
#  public   | users_userid_seq | 序列数 | postgres
# (2 行记录)

# test=# \d users
#                                      数据表 "public.users"
#    栏位   |         类型          | 校对规则 |  可空的  |                 预设
# ----------+-----------------------+----------+----------+---------------------------------------
#  userid   | integer               |          | not null | nextval('users_userid_seq'::regclass)
#  username | character varying(64) |          |          |
#  password | character varying(64) |          |          |
# 索引：
#     "users_pkey" PRIMARY KEY, btree (userid)