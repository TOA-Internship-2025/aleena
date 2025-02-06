from models.farmer_company import FarmerCompany
from sqlalchemy.orm import Session

def get_all_farmercompany(db:Session):
    result=db.query(FarmerCompany).all() 
    return result


def get_farmercompany_with_id(id:int, db:Session):
    result=db.query(FarmerCompany).filter(FarmerCompany.id==id)
    return result

def add_farmercompany(data:dict,db:Session):
    try:
        result=FarmerCompany(**data)
        db.add(result)
        db.commit()
        db.refresh(db)
        return True
    except:
        return False

    