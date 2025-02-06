from models.cultivator import Cultivator
from sqlalchemy.orm import Session

# Cultivator Table:
# - Define a helper function to serialize the Cultivator model into a dictionary for API responses.
# - Implement CRUD operations:
#   - Get All Records: Use db.query(Cultivator).all() to fetch all records.
#   - Get Single Record by ID: Use db.query(Cultivator).filter(Cultivator.id == id).first() to retrieve a record by ID.
#   - Get All Cultivators by Cultivator ID: Use db.query(Cultivator).filter(Cultivator.company_id == comp_id).all() to retrieve all cultivators for a specific farmer company.
#   - Add Record: Insert a new Cultivator record and commit it to the database.
#   - Update Record: Find a Cultivator by ID, apply updates, and commit the changes.
#   - Delete Record: Locate a record by ID and delete it from the database.
# - Implement error handling to manage invalid IDs or missing records.


def get_all_cultivator(db:Session):
    result=db.query(Cultivator).all() 
    return result

def get_cultivator_with_id(id:int, db:Session):
    try:
        result=db.query(Cultivator).filter(Cultivator.id==id).first()
        return result
    except:
        return False
    
def cultivators_with_companyid(company_id:int,db:Session):
    try:
        result=db.query(Cultivator).filter(Cultivator.company_id==company_id).all()
        return result
    except:
        return False

def add_cultivator(data:dict,db:Session):
    try:
        result=Cultivator(**data)
        db.add(result)
        db.commit()
        db.refresh(result)
        return True
    except:
        return False

def update_cultivator(id:int,data:dict,db:Session):
        row=db.query(Cultivator).filter(Cultivator.id==id).first()
        if not row:
            return False
        for key,value in data.items():
            setattr(row,key,value)
        db.commit()
        db.refresh(row)
        result=db.query(Cultivator).filter(Cultivator.id==id).first()
        return result

def delete_cultivator(id:int,db:Session):
    row=db.query(Cultivator).filter(Cultivator.id==id).first()
    if not row:
        return False
    db.delete(row)
    db.commit()
    return row
