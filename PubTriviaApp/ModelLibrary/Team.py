from sqlalchemy import *
from sqlalchemy.orm import relationship
import PTConfig


class Team(PTConfig.Base):
    __tablename__ = 'Teams'
    Id = Column(Integer, primary_key=True)
    Name = Column(Text)
    Games = relationship('Game_Team', back_populates='Team')

