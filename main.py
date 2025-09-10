from fastapi import FastAPI,Path,HTTPException,Query
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

#Path parameter- these are the part of the url but these are variable ex user-id and mandatory /patient/{patient_id}
#Query parameter-http://127.0.0.1:8000/sort?sort_by=height&order_by=desc not mando tary

@app.get('/patient/{patient_id}')
# def get_patient(patient_id:str): can do this also
def get_patient(patient_id:str=Path(..., description="id of the patient",example="p001")):
    data=loadData()
    print(patient_id)
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail="Patient not found")
@app.get('/sort')
def sort_patients(sort_by:str=Query(..., description="Sort on the basis of height weight and bmi"),order_by:str=Query('asc',description="desc or ascending")):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail="please choose a valid parameter to sort")
    
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400, detail="PLsease provide asc or desc for sorting order")
    

    data=loadData()
    sort_order=True if order_by == 'desc'else False
    sorteddata=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorteddata