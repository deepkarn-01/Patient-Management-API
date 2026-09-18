from pydantic import BaseModel, Field
from typing import Annotated

class patient(BaseModel):
    
    name:Annotated[str, Field(max_kegth=50, title='patient name', description= 'write name', examples= 'deepesh') ]
    age:int
    weight: float
    married: bool
    patient_symp:list[str]
    contact_detail:dict[str, str]
    
    
def insert_patient_data(patient1: patient):
    
    print(patient1.name)
    print(patient1.age)
    print('inserted into database')
   
        

patient_info = {'name': 'nitish', 'age': 30, 'weight': 75.2, 'married':True, 'patient_symp':['pollen', 'dust'], 'contact_detail': {'email':'abc@gmail.com', 'ph': '5646'}}
patient1= patient(**patient_info) 
insert_patient_data(patient1)