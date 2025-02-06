#all routes POST(create) GET(read) PUT(update) DELETE(delete)
from database.config import db_dependency
from fastapi import APIRouter
import database.cultivator as c
from models.cultivator import CultivatorBase, UpdateCultivatorBase
from models.response import ResponseModel as rs


router=APIRouter()

@router.get("/")
async def get_all_cultivators(db:db_dependency):
    result=c.get_all_cultivator(db)
    if not result:
        return "Could not retrieve all"
    return rs(result,"Retrieved")

@router.get("/{id}")
async def get_the_cultivator_with_id(id:int,db:db_dependency):
    result=c.get_cultivator_with_id(id,db)
    if not result:
        return "Could not retrieve one"
    return rs(result,"Retrieved")


@router.get("/farmer/{company_id}")
async def the_cultivators_with_company_id(company_id:int,db:db_dependency):
    print("in")
    result=c.cultivators_with_companyid(company_id,db)
    if not result:
        print(result)
        return "Could not retrieve one with the farmer company"
    return rs(result,"Retrieved")

@router.post("/")
async def add_the_cultivator(data:CultivatorBase,db:db_dependency):
    result=c.add_cultivator(data.dict(),db)
    if not result:
        return "Could not add"
    return rs(result,"Added")

@router.put("/{id}")
async def update_the_cultivator(id:int,data:UpdateCultivatorBase,db:db_dependency):
    x={key:value for key,value in data.dict().items() if value is not None}
    result=c.update_cultivator(id,x,db)
    if not result:
        return "Could not update"
    return rs(result,"Updated")

@router.delete("/{id}")
async def delete_the_cultivator(id:int,db:db_dependency):
    result=c.delete_cultivator(id,db)
    if not result:
        return "Could not delete"
    return rs(result,"Deleted")