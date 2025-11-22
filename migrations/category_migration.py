from sqlalchemy import( 
    Column, 
    Integer, 
    String, 
    Table, 
    Boolean, 
    ForeignKey)

from config.database import meta

categories = Table(
    "categories", meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), nullable=False, index=True),
    Column('is_global', Boolean, default=False),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=True),
)
