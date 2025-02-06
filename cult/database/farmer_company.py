from models.farmer_company import FarmerCompany
from sqlalchemy.orm import Session

# FarmerCompany Table:
# - Define a helper function to serialize the FarmerCompany model into a dictionary for API responses.
# - Implement CRUD operations:
#   - Get All Records: Use db.query(FarmerCompany).all() to retrieve all records.
#   - Get Single Record by ID: Use db.query(FarmerCompany).filter(FarmerCompany.id == id).first() to fetch a record by ID.
#   - Add Record: Create a new FarmerCompany record and commit it to the database.
#   - Update Record: Find an existing record by ID, apply updates, and save changes.
#   - Delete Record: Fetch the record by ID and delete it from the database.
# - Ensure error handling for missing records or invalid data.


def get_all_farmercompany(db:Session):
    result=db.query(FarmerCompany).all() 
    return result

def get_farmercompany_with_id(id:int, db:Session):
    try:
        result=db.query(FarmerCompany).filter(FarmerCompany.id==id).first()
        return result
    except:
        return False

def add_farmercompany(data:dict,db:Session):
    try:
        result=FarmerCompany(**data)
        db.add(result)
        db.commit()
        db.refresh(result)
        return True
    except:
        return False

def update_farmercompany(id:int,data:dict,db:Session):
        row=db.query(FarmerCompany).filter(FarmerCompany.id==id).first()
        if not row:
            return False
        for key,value in data.items():
            setattr(row,key,value)
        db.commit()
        db.refresh(row)
        result=db.query(FarmerCompany).filter(FarmerCompany.id==id).first()
        return result

def delete_farmercompany(id:int,db:Session):
    row=db.query(FarmerCompany).filter(FarmerCompany.id==id).first()
    if not row:
        return False
    db.delete(row)
    db.commit()
    return row
