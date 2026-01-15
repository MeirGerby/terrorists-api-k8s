from pydantic import BaseModel 

class Terorists(BaseModel):
    name: str
    location:str 
    denger_rate: int 