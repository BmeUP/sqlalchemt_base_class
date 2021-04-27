from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.base_model import Base
# from app.model_one import One
# from app.model_two import Two

engine = create_engine("sqlite+pysqlite:///sqldb.db", echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


