from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.log import echo_property
from sqlalchemy.orm import sessionmaker

DB_CONNECTION = 'sqlite:///data\data.db?check_same_thread=False'
engine = create_engine(DB_CONNECTION, echo = False)
Base = declarative_base()
Session = sessionmaker(bind= engine)