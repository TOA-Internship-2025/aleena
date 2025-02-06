from route.farmer_company import router as fc_router
from route.cultivator import router as c_router
from fastapi import FastAPI
from database.config import Base, engine

app=FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(fc_router,prefix="/farmercompany",tags=["farmers"])
app.include_router(c_router,prefix="/cultivators",tags=["cultivators"])