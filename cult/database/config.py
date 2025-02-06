from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE='postgresql://postgres:postgres@localhost:5432/cultdb'

engine=create_engine(URL_DATABASE)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session, Depends(get_db)]