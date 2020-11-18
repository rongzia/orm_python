from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint #区分大小写

#创建连接
engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/spj',encoding='utf-8',echo=True)
#生成 orm 基类
base=declarative_base()



# create table S
# (
# 	Sno char(2) unique,
# 	Sname char(6),
# 	Status char(2),
# 	City char(4),
# 	primary key(Sno)
# );
class S(base):
    __tablename__ = 'S'
    SNO    = Column('SNO', String(2), primary_key=True, unique=True)
    SNAME  = Column('SNAME', String(6))
    STATUS = Column('STATUS', String(2))
    CITY   = Column('CITY', String(4))

# create table P
# (
# 	Pno char(2) unique,
# 	Pname char(6),
# 	color char(2),
# 	weight int,
# 	primary key(Pno)
# );
class P(base):
    __tablename__ = 'P'
    PNO    = Column('PNO', String(2), primary_key=True, unique=True)
    PNAME  = Column('PNAME', String(6))
    COLOR = Column('COLOR', String(2))
    WEIGHT   = Column('WEIGHT', Integer)

# create table J
# (
# 	Jno char(2) unique,
# 	Jname char(8),
# 	CITY char(4),
# 	primary key(Jno)
# );
class J(base):
    __tablename__ = 'J'
    JNO   = Column('JNO', String(2), primary_key=True, unique=True)
    JNAME = Column('JNAME', String(8))
    CITY  = Column('CITY', String(4))


# create table SPJ
# (
# 	Sno char(2),
# 	Pno char(2),
# 	Jno char(2),
# 	QTY int,
# 	primary key(Sno,Pno,Jno),
# 	foreign key(Sno) references S(Sno),
# 	foreign key(Pno) references P(Pno),
# 	foreign key(Jno) references J(Jno)
# );
class SPJ(base):
    __tablename__ = 'SPJ'
    SNO = Column('SNO', String(2), ForeignKey('S.SNO'))
    PNO = Column('PNO', String(2), ForeignKey('P.PNO'))
    JNO = Column('JNO', String(2), ForeignKey('J.JNO'))
    # SNO = Column('SNO', String(2))
    # PNO = Column('PNO', String(2))
    # JNO = Column('JNO', String(2))
    QTY = Column('QTY', Integer)
    __table_args__ = (
        PrimaryKeyConstraint('SNO', 'PNO', 'JNO'),
        {},
    )
base.metadata.create_all(engine) #创建表结构
