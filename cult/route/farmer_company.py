#all routes POST(create) GET(read) PUT(update) DELETE(delete)
from database.config import db_dependency
from fastapi import APIRouter
import database.farmer_company as fc
from models.farmer_company import FarmerBase
from models.response import ResponseModel as rs


router=APIRouter()
# FarmerCompany Table:
# - Define a helper function to serialize the FarmerCompany model into a dictionary for API responses.
# - Implement CRUD operations:
#   - Get All Records: Use db.query(FarmerCompany).all() to retrieve all records.
#   - Get Single Record by ID: Use db.query(FarmerCompany).filter(FarmerCompany.id == id).first() to fetch a record by ID.
#   - Add Record: Create a new FarmerCompany record and commit it to the database.
#   - Update Record: Find an existing record by ID, apply updates, and save changes.
#   - Delete Record: Fetch the record by ID and delete it from the database.
# - Ensure error handling for missing records or invalid data.


@router.get("/")
async def get_all_farmers(db:db_dependency):
    result=fc.get_all_farmercompany(db)
    if not result:
        return "Could not retrieve"
    return rs(result,"Retrieved")


@router.post("/")
async def add_farmer(data:FarmerBase,db:db_dependency):
    result=fc.add_farmercompany(data.dict(),db)
    if not result:
        return "Could not add"
    return rs(result,"Added")