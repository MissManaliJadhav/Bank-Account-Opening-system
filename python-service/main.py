from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Customer(BaseModel):

 name:str
 accountType:str
 deposit:int

@app.post("/verify")

def verify(c:Customer):

 if c.deposit>=500:
  return {"status":"verified"}

 return {"status":"rejected"}
