from sqlalchemy import *
import PTConfig


class User(PTConfig.Base):
    __tablename__ = 'Users'
    UserId = Column(Text, primary_key=True)
    FirstName = Column(Text)
    LastName = Column(Text)

    def __init__(self):
        pass
