#all routes POST(create) GET(read) PUT(update) DELETE(delete)
from database.config import db_dependency
from fastapi import APIRouter
import database.farmer_company as fc


router=APIRouter()

@router.get("/")
async def get_all_farmers(db:db_dependency):
    result=fc.get_all_farmercompany(db)
    if not result:
        return "Could not retrieve"
    return result
