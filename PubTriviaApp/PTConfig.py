# JGunter 6/3/16
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# All Pub Trivia App files must import PTConfig.py.
# A single declarative base instance will be used for
# mapping all Model Library classes to the database.

Base = declarative_base()
Engine = create_engine('sqlite:///PubTriviaDB.db')
Session = sessionmaker(bind=Engine)
