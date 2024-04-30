from sqlalchemy import Column, VARCHAR, INTEGER
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CustomObject(Base):
    __tablename__ = 'custom_objects'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(VARCHAR(255))
    category = Column(VARCHAR(255))
    price = Column(INTEGER, nullable=False)
    quantity = Column(INTEGER)