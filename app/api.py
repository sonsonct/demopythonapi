from fastapi import FastAPI

from models.Custumers import Customers
from config.db import cursor
from getdata.DataCustomer import DataCustomer

app = FastAPI()


app = FastAPI()

@app.get("/")
async def getAllcustomers():
    return DataCustomer.get_customers()

@app.get("/{id}")
async def getCustomersById(id: int):
    return DataCustomer.get_customersById(id)

@app.get("/name/{name}")
async def getCustomersByName(name: str):
    return DataCustomer.findByName(name)

@app.delete("/id/{id}")
async def deleteById(id: int):
    return DataCustomer.deleteById(id)


@app.post("/add")
async def Addcustomer(customers: Customers):
    return DataCustomer.insert_Customer(customers)
  


#đóng kết nối sau khi xử lý xong request
@app.on_event("shutdown")
def shutdown_event():
    cursor.close()
