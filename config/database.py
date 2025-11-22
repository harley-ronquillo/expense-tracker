from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData, inspect

db_url = "mysql+pymysql://root:root@localhost:3306/financial_tracking_db"
Base = declarative_base()
engine = create_engine(db_url)
meta = MetaData()
conn = engine.connect()
inspect = inspect(engine)