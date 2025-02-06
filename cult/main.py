from route.farmer_company import router as fc_router
from fastapi import FastAPI
from database.config import Base, engine

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(fc_router,prefix="/farmercompany",tags=["farmers"])
