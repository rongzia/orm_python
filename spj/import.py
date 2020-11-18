from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#创建连接
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/spj',encoding='utf-8',echo=True)

db_session_class = sessionmaker(bind=engine)    # db_session_class 仅仅是一个类
session = db_session_class()                    # 实例化一个对象

# ', ('S1','精益','20','天津')'
# ('S2','盛锡','10','北京'),
# ('S3','东方红','30','北京'),
# ('S4','丰泰盛','20','天津'),
# ('S5','为民','30','上海');
from create import S
s = S(SNO='S1', SNAME='精益', STATUS='20', CITY='天津')
session.add(s)
s = S(SNO='S2', SNAME='盛锡', STATUS='10', CITY='北京')
session.add(s)
s = S(SNO='S3', SNAME='东方红', STATUS='30', CITY='北京')
session.add(s)
s = S(SNO='S4', SNAME='丰泰盛', STATUS='20', CITY='天津')
session.add(s)
s = S(SNO='S5', SNAME='为民', STATUS='30', CITY='上海')
session.add(s)
session.commit()



# insert into P(Pno,Pname,color,weight)
# values
# ('P1','螺母','红',12),
# ('P2','螺栓','绿',17),
# ('P3','螺丝刀','蓝',14),
# ('P4','螺丝刀','红',14),
# ('P5','凸轮','蓝',40),
# ('P6','齿轮','红',30);
from create import P
p = P(PNO='P1', PNAME='螺母', COLOR='红', WEIGHT='12')
session.add(p)
p = P(PNO='P2', PNAME='螺栓', COLOR='绿', WEIGHT='17')
session.add(p)
p = P(PNO='P3', PNAME='螺丝刀', COLOR='蓝', WEIGHT='14')
session.add(p)
p = P(PNO='P4', PNAME='螺丝刀', COLOR='红', WEIGHT='14')
session.add(p)
p = P(PNO='P5', PNAME='凸轮', COLOR='蓝', WEIGHT='40')
session.add(p)
p = P(PNO='P6', PNAME='齿轮', COLOR='红', WEIGHT='30')
session.add(p)
session.commit()




# insert into J(Jno,Jname,CITY)
# values
# ('J1','三建','北京'),
# ('J2','一汽','长春'),
# ('J3','弹簧厂','天津'),
# ('J4','造船厂','天津'),
# ('J5','机车厂','唐山'),
# ('J6','无线电厂','常州'),
# ('J7','半导体厂','南京');
from create import J
j = J(JNO='J1', JNAME='三建', CITY='北京')
session.add(j)
j = J(JNO='J2', JNAME='一汽', CITY='长春')
session.add(j)
j = J(JNO='J3', JNAME='弹簧厂', CITY='天津')
session.add(j)
j = J(JNO='J4', JNAME='造船厂', CITY='天津')
session.add(j)
j = J(JNO='J5', JNAME='机车厂', CITY='唐山')
session.add(j)
j = J(JNO='J6', JNAME='无线电厂', CITY='常州')
session.add(j)
j = J(JNO='J7', JNAME='半导体厂', CITY='南京')
session.add(j)
session.commit()



# insert into SPJ(Sno,Pno,Jno,QTY)
# values
# ('S1','P1','J1',200),
# ('S1','P1','J3',100),
# ('S1','P1','J4',700),
# ('S1','P2','J2',100),
# ('S2','P3','J1',400),
# ('S2','P3','J2',200),
# ('S2','P3','J4',500),
# ('S2','P3','J5',400),
# ('S2','P5','J1',400),
# ('S2','P5','J2',100),
# ('S3','P1','J1',200),
# ('S3','P3','J1',200),
# ('S4','P5','J1',100),
# ('S4','P6','J3',300),
# ('S4','P6','J4',200),
# ('S5','P2','J4',100),
# ('S5','P3','J1',200),
# ('S5','P6','J2',200),
# ('S5','P6','J4',500);
session.execute('insert into "SPJ"("SNO", "PNO","JNO", "QTY") values '
                '(\'S1\',\'P1\',\'J1\',200)'
                ', (\'S1\',\'P1\',\'J3\',100)'
                ', (\'S1\',\'P1\',\'J4\',700)'
                ', (\'S1\',\'P2\',\'J2\',100)'
                ', (\'S2\',\'P3\',\'J1\',400)'
                ', (\'S2\',\'P3\',\'J2\',200)'
                ', (\'S2\',\'P3\',\'J4\',500)'
                ', (\'S2\',\'P3\',\'J5\',400)'
                ', (\'S2\',\'P5\',\'J1\',400)'
                ', (\'S2\',\'P5\',\'J2\',100)'
                ', (\'S3\',\'P1\',\'J1\',200)'
                ', (\'S3\',\'P3\',\'J1\',200)'
                ', (\'S4\',\'P5\',\'J1\',100)'
                ', (\'S4\',\'P6\',\'J3\',300)'
                ', (\'S4\',\'P6\',\'J4\',200)'
                ', (\'S5\',\'P2\',\'J4\',100)'
                ', (\'S5\',\'P3\',\'J1\',200)'
                ', (\'S5\',\'P6\',\'J2\',200)'
                ', (\'S5\',\'P6\',\'J4\',500);')
session.commit()