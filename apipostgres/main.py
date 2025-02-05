from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import model
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()
model.Base.metadata.create_all(bind=engine)

class ChoiceBase(BaseModel):
    ch_text:str
    is_correct:bool

class QuestionBase(BaseModel):
    q_text:str
    choices:List[ChoiceBase]

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session, Depends(get_db)]

@app.post("/questions/")
async def create_q(question:QuestionBase, db:db_dependency):
    db_q=model.Questions(q_text=question.q_text)
    db.add(db_q)
    db.commit()
    db.refresh(db_q)
    for choice in question.choices:
        db_choice=model.Choices(ch_text=choice.ch_text,is_correct=choice.is_correct)
        db.add(db_choice)
    db.commit()