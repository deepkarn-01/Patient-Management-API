from fastapi import FastAPI, Path, HTTPException, Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
def loaddata():
    with open('patient.json', 'r')as f:
        data=json.load(f)
    return data

def savedata(data):
    with open('patient.json','w')as f:
        json.dump(data,f)

app= FastAPI()
class Patient(BaseModel):
    
    id:Annotated[str, Field(..., description='ID of patient', example='P001')]
    name: Annotated[str, Field(..., description='name of patient')]
    city: Annotated[str, Field(..., description='city of patient')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='age of patient')]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description='gender of patient')]
    height: Annotated[float, Field(..., gt=0, description='weight of patient')]
    weight: Annotated[float, Field(..., gt=0, description='height of patient')]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi= round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi <18.5:
            return 'underweight'
        elif self.bmi<25:
            return ' normal'
        elif self.bmi<30:
            return ' normal'
        else:
            return 'obese'


class PatientUpdate (BaseModel):
        name: Annotated [Optional [str], Field(default=None)]
        city: Annotated [Optional [str], Field(default=None)]
        age:  Annotated [Optional [int], Field(default=None, gt=0)]
        gender: Annotated [Optional [Literal['male', 'female']], Field(default=None)]
        height:Annotated [Optional [float], Field(default=None, gt=0)]
        weight: Annotated [Optional [float], Field (default=None, gt=0)]
        
@app.get("/")

def home():
    return {'patient management api'}

@app.get('/view')
def view():
    data=loaddata()
    return data
@app.get('/patient/{patient_id}')

def view_patient(patient_id: str= Path(...,description="write id ", example='p001')):
    data=loaddata()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail='patient not found')
        return {'error: patient detail not found'}
    
@app.get('/sort')
def sort(sort_by: str= Query(..., description='sort by height, weight or bmi'), order:str= Query('asc', desc='sortin asc or desc')):
    valid_fields= ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= f' invalid field from{' valid_fields'}')

    if order not in ['asc', 'desc']:
         raise HTTPException(status_code=400, detail= ' invalid field ')

    data=loaddata()
    sortorder= True if order=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sortorder)
    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):
    data=loaddata()
    if patient.id in data:
        raise HTTPException(status_code=400, detail= 'patient exixt')

    data[patient.id]=patient.model_dump(exclude=['id'])
    savedata(data)

    return JSONResponse(status_code=201, content={'created'})


@app.put('/edit/{patient_id}')
def update_detail(patient_id:str, patient_upd:PatientUpdate):
    data=loaddata()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='not found')
    
    exist_pid=data[patient_id] 
    
    update_Pinfor=patient_upd.model_dump(exclude_unset=True)   
    for key, value in update_Pinfor.items():
        exist_pid[key]=value
        
    exist_pid['id']= patient_id
    patient_pyobj= Patient(**exist_pid)
    exist_pid=patient_pyobj.model_dump(exclude='id')
    
    data[patient_id]= exist_pid
    savedata(data)
    
    return JSONResponse(status_code=200, content={'upate info'})
    
@app.delete('/delete/{patient_id}')
def del_patient(patient_id:str):
    data=loaddata()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    del data[patient_id]
    savedata(data)
    return JSONResponse(status_code=200, content='deleted')

