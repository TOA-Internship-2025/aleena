@app.get("/questions/{q_id}")
async def read_question(q_id:int,db:db_dependency):
    result=db.query(model.Questions).filter(model.Questions.id==q_id).first()
    if not result:
        raise HTTPException()
