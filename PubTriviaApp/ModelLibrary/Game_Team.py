from sqlalchemy import *
from sqlalchemy.orm import relationship
import PTConfig
from ModelLibrary import Game, Team


class Game_Team(PTConfig.Base):
    __tablename__ = 'Game_Team'
    GameId = Column(Integer, ForeignKey(Game.Id), primary_key=True)
    TeamId = Column(Integer, ForeignKey(Team.Id), primary_key=True)
    # Extra column for total score
    Game = relationship('Games', back_populates='Teams')
    Team = relationship('Teams', back_populates='Games')