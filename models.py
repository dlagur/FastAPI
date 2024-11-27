from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(11), nullable=False)
    age = Column(Integer, nullable=False)
    job = Column(String(50), nullable=False)
    