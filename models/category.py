from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, ForeignKey
from config.database import Base


# Model = Python class = table in DB
class CategoryDB(Base):
    __tablename__ = 'categories'  # Table name

    # Table fields as class attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_global = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)  
    
    # One-to-many: category -> expenses
    income = relationship("Income", back_populates="category")
    expense = relationship("Expense", back_populates="category")




