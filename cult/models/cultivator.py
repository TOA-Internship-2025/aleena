#scheme structure
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database.config import Base
from pydantic import BaseModel
from typing import Optional

class Cultivator(Base):
    __tablename__='cultivator'
    id=Column(Integer,primary_key=True, index=True)
    cultivator_name=Column(String,index=True)
    cultivation_lot=Column(String,index=True)
    crop_type=Column(String,index=True)
    company_id=Column(Integer, ForeignKey("farmer_company.id"))

class CultivatorBase(BaseModel):
    cultivator_name:str
    cultivation_lot:str
    crop_type:str
    company_id:int

class UpdateCultivatorBase(BaseModel):
    cultivator_name:Optional[str]
    cultivation_lot:Optional[str]
    crop_type:Optional[str]
    company_id:Optional[int]