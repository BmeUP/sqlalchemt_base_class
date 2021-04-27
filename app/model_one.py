from sqlalchemy import Column, Integer, String
from app.base_model import Base

class One(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

