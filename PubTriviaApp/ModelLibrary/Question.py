from sqlalchemy import *
from sqlalchemy.orm import relationship
import PTConfig
from ModelLibrary.Round import round_question


class Question(PTConfig.Base):
    __tablename__ = 'Questions'
    Id = Column(Integer, primary_key=True)
    Category = Column(Integer, ForeignKey('Category.Id'))
    Text = Column(Text)
    Answer = Column(Text)
    Rounds = relationship('Rounds', secondary=round_question, back_populates='Questions')
