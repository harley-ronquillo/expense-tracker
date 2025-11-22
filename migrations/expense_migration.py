from sqlalchemy import( 
    Column, 
    Integer, 
    String, 
    Table, 
    Boolean, 
    ForeignKey)

from config.database import meta

expenses = Table(
    "expenses", meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('amount', Integer, default=False),
    Column('description', String, nullable=True),
    Column('date', String, nullable=False),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=True),
    Column('category_id', Integer, ForeignKey('categories.id'), nullable=False),
)
