from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, ForeignKey
from config.database import Base

# Model = Python class = table in DB
class UserDB(Base):
    __tablename__ = 'users'  # Table name

    # Table fields as class attributes
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    verified = Column(Integer, default=0)
    monthly_income = Column(Integer, nullable=False)
   
    # One-to-many: user -> categories
    categories = relationship("Category", back_populates="user")




