from pydantic import BaseModel

class Customers(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    address: str
    password: str
    verify_status: int
    

