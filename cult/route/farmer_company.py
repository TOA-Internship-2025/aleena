#all routes POST(create) GET(read) PUT(update) DELETE(delete)
from database.config import db_dependency
from fastapi import APIRouter
import database.farmer_company as fc
from models.farmer_company import FarmerBase,UpdateFarmerBase
from models.response import ResponseModel as rs


router=APIRouter()

@router.get("/")
async def get_all_farmers(db:db_dependency):
    result=fc.get_all_farmercompany(db)
    if not result:
        return "Could not retrieve"
    return rs(result,"Retrieved")

@router.get("/{id}")
async def get_the_farmer_with_id(id:int,db:db_dependency):
    result=fc.get_farmercompany_with_id(id,db)
    if not result:
        return "Could not retrieve"
    return rs(result,"Retrieved")

@router.post("/")
async def add_the_farmer(data:FarmerBase,db:db_dependency):
    result=fc.add_farmercompany(data.dict(),db)
    if not result:
        return "Could not add"
    return rs(result,"Added")

@router.put("/{id}")
async def update_the_farmer(id:int,data:UpdateFarmerBase,db:db_dependency):
    x={key:value for key,value in data.dict().items() if value is not None}
    result=fc.update_farmercompany(id,x,db)
    if not result:
        return "Could not update"
    return rs(result,"Updated")

@router.delete("/{id}")
async def delete_the_farmer(id:int,db:db_dependency):
    result=fc.delete_farmercompany(id,db)
    if not result:
        return "Could not delete"
    return rs(result,"Deleted")