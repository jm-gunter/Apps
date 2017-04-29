from sqlalchemy import *
from sqlalchemy.orm import relationship
import PTConfig


class Game(PTConfig.Base):
    __tablename__ = 'Games'
    Id = Column(Integer, primary_key=True)
    Name = Column(Text)
    Date = Column(Date)
    Venue_Id = Column(Integer, ForeignKey('Venues.Id'))
    Teams = relationship('Game_Team', back_populates='Games')
    Rounds = relationship('Rounds', back_populates='Games')

