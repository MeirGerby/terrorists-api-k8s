from pydantic import BaseModel 

class Terorists(BaseModel):
    name: str
    location:str 
    gender_rate: int 