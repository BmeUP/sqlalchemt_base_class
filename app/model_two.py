from sqlalchemy import Column, Integer, String
from app.base_model import Base

class Two(Base):
    __tablename__ = 'polzovateli'

    id = Column(Integer, primary_key=True)
    surename = Column(String)