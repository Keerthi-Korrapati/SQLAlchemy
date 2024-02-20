from sqlalchemy import create_engine,orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:ke12@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = orm.declarative_base()