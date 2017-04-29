from sqlalchemy import *
from sqlalchemy.orm import relationship
import PTConfig


class Venue(PTConfig.Base):
    __tablename__ = 'Venues'
    Id = Column(Integer, primary_key=True)
    Name = Column(Text)
    Address = Column(Text)
    City = Column(Text)
    State = Column(Text)
    Games = relationship("Game")

    def __init__(self):
        pass
