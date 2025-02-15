#scheme structure
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.config import Base
from pydantic import BaseModel
from typing import Optional

class FarmerCompany(Base):
    __tablename__='farmer_company'
    id=Column(Integer,primary_key=True, index=True)
    company_name=Column(String,index=True)
    code=Column(Integer, index=True)
    active=Column(Boolean, default=True)


class FarmerBase(BaseModel):
    company_name:str
    code:int
    active:bool

class UpdateFarmerBase(BaseModel):
    company_name: Optional[str]
    code: Optional[int]
    active: Optional[bool]
