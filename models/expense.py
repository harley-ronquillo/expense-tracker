from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, ForeignKey
from config.database import Base


# Model = Python class = table in DB
class ExpenseDB(Base):
    __tablename__ = 'expenses'  # Table name

    # Table fields as class attributes
    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    date = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    
      
    




