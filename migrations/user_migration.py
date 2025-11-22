from sqlalchemy import( 
    Column, 
    Integer, 
    String, 
    Table, 
    Boolean
)

from config.database import meta

users = Table(
    "users", meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('email', String(100), nullable=False),
    Column('password', String(255), nullable=False),
    Column('verified', Boolean, nullable=False),
    Column('monthly_income', Integer, nullable=False),
)
