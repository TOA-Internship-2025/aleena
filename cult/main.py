from route.farmer_company import router as fc_router
from route.cultivator import router as c_router
from fastapi import FastAPI
from database.config import Base, engine
from fastapi.middleware.cors import CORSMiddleware

origins = [
    
    "https://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080",
]

app=FastAPI()
Base.metadata.create_all(bind=engine)
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_methods=["*"],
                   )

app.include_router(fc_router,prefix="/farmercompany",tags=["farmers"])
app.include_router(c_router,prefix="/cultivators",tags=["cultivators"])