import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String #区分大小写
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

#创建连接
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/spj',encoding='utf-8',echo=True)

db_session_class = sessionmaker(bind=engine)    # db_session_class 仅仅是一个类
session = db_session_class()                    # 实例化一个对象

# 1. 在零件表的视图中找出 WEIGHT < 20 的零件名字(PNAME)
# spj=# select "PNAME" from "P" where "WEIGHT" < 20;
#  PNAME
# --------
#  螺母
#  螺栓
#  螺丝刀
#  螺丝刀
# (4 行记录)
from create import P
p_list = session.query(P, P.PNAME).filter(P.WEIGHT < 20).all()
for p in p_list:
    print(p.PNAME)

# 2. 在零件表中查询重量大于所有零件平均重量的 零件名字和零件号码
# spj=# select "PNAME", "PNO" FROM "P" where "WEIGHT" > (select AVG("WEIGHT") from "P");
#  PNAME | PNO
# -------+-----
#  凸轮  | P5
#  齿轮  | P6
# (2 行记录)

# avg_weight = session.query(func.avg(P.WEIGHT)).scalar()
# print(avg_weight)
p_list = session.query(P, P.PNAME, P.PNO).filter(P.WEIGHT > session.query(func.avg(P.WEIGHT)).scalar())
for p in p_list:
    print(p.PNAME, p.PNO)

# 3. 查询各工程用到的所有零件的平均数量。
# spj=# select AVG("QTY") from "SPJ" GROUP BY "SPJ"."JNO";
#          avg
# ----------------------
#  150.0000000000000000
#  400.0000000000000000
#  400.0000000000000000
#  242.8571428571428571
#  200.0000000000000000
# (5 行记录)
from create import SPJ
count = session.query(func.avg(SPJ.QTY)).group_by(SPJ.JNO)
for c in count:
    print(c[0])

# 4. 查询工程项目中至少使用了供应商S1所供应的全部零件的城市(CITY)
# spj=# select DISTINCT "CITY"
# spj-# from "J", "SPJ"
# spj-# where "J"."JNO"="SPJ"."JNO" and "SPJ"."SNO"='S1';
#  CITY
# ------
#  北京
#  天津
#  长春
# (3 行记录)
from create import J
city_list = session.query(func.distinct(J.CITY)).outerjoin(SPJ, J.JNO==SPJ.JNO).filter(SPJ.SNO == 'S1');
for c in city_list:
    print(c[0])