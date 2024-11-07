from fastapi import FastAPI
from pydantic import BaseModel #provides data validation
 
app=FastAPI()

#define a request model
class AddRequest(BaseModel): #The AddRequest class is a blueprint for the data that we expect to receive when someone sends a request to our FastAPI application to add two numbers. which inherits the base model 
    num1:float
    num2:float

@app.post("/add")
async def add_numbers(request:AddRequest):
    result=request.num1+request.num2
    return {"result":result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)


