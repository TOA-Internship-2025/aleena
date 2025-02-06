#scheme structure
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.cultivator import Base

class farmer_company(Base):
    __tablename__='farmer_company'
    id=Column(Integer,primary_key=True, index=True)
    company_name=Column(String,index=True)
    code=Column(Integer, index=True)
    active=Column(Boolean, default=True)
