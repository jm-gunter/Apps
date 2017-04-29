from sqlalchemy import *
from sqlalchemy.orm import relationship
import PTConfig

round_question = Table('Round_Question', PTConfig.Base.metadata,
                       Column('RoundId', Integer, ForeignKey('Round.Id')),
                       Column('QuestionId', Integer, ForeignKey('Question.Id')))


class Round(PTConfig.Base):
    __tablename__ = 'Rounds'
    Id = Column(Integer, primary_key=True)
    Name = Column(Text)
    GameId = Column(Integer, ForeignKey('Game.Id'))
    Game = relationship('Games', back_populates='Rounds')
    Questions = relationship('Questions', secondary=round_question, back_populates='Rounds')
