from fastapi import FastAPI
import json
app=FastAPI()

def loadData():
    with open("./patient.json", 'r') as f:
        data=json.load(f)
        return data

@app.get("/")
def hello():
    return {"message":"Patient management system api"}
    
    # uvicorn main:app --reload  reload is used to save the changes automatically no need to run again

@app.get("/about")
def about():
    return {"message":"Api for manage patient reports"}    

# your end point/docs gives the all documentation

@app.get("/view")
def view():
    data=loadData()
    return data