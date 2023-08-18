from config.db import cursor, connection
from models.Custumers import Customers
import json

class DataCustomer:
    def get_customers():
        try:
            query = "SELECT * FROM custumers"
            cursor.execute(query)
            results = cursor.fetchall()
            if results:
                customers_list = []
                for customers_data in results:
                    data = {
                        "id": customers_data[0],
                        "name": customers_data[1],
                        "email": customers_data[2],
                        "phone_number": customers_data[3],
                        "address": customers_data[4],
                        "password": customers_data[5],
                        "verify_status": customers_data[6]
                    }
                    Customers1 = Customers(**data)
                    customers_list.append(Customers1)
                    
                return customers_list
            else:
                return {"error": "User not found"}
        except Exception as e:
            return {"error": str(e)}

    def get_customersById(id):
        try:
            query = f"SELECT * FROM custumers where id = {id}"
            cursor.execute(query)
            results = cursor.fetchall()
            if results:
                data = {
                        "id": results[0][0],
                        "name": results[0][1],
                        "email": results[0][2],
                        "phone_number": results[0][3],
                        "address": results[0][4],
                        "password": results[0][5],
                        "verify_status": results[0][6]
                }
                Customers1 = Customers(**data)
                return Customers1  
            else:
                return {"error": "User not found"}
        except Exception as e:
            return {"error": str(e)}
    def insert_Customer(Customer: Customers):
        try:
            query = f"INSERT INTO custumers (`name`, `email`, `phone_number`, `address`, `password`, `verify_status`) VALUES ('{Customer.name}', '{Customer.email}', '{Customer.phone_number}', '{Customer.address}', '{Customer.password}', '{Customer.verify_status}')"
            cursor.execute(query)
            connection.commit()
            return {
                "status": "ok",
                "message": "Thêm thành công",
                "data" : Customer
            }
        except Exception as e:
            return {"error": str(e)}
    def findByName(name):
        try:
            query = f"SELECT * FROM `custumers` WHERE name LIKE '%{name}%'"
            cursor.execute(query)
            results = cursor.fetchall()
            if results:
                customers_list = []
                for customers_data in results:
                    data = {
                        "id": customers_data[0],
                        "name": customers_data[1],
                        "email": customers_data[2],
                        "phone_number": customers_data[3],
                        "address": customers_data[4],
                        "password": customers_data[5],
                        "verify_status": customers_data[6]
                    }
                    Customers1 = Customers(**data)
                    customers_list.append(Customers1)
                    
                return {
                    "status": "ok",
                    "message": "Tìm thành công",
                    "data" : customers_list
                }
            else:
                return {"error": "User not found"}
        except Exception as e:
            return {"error": str(e)}
    def deleteById(id):
        try:
            query = f"DELETE FROM `custumers` WHERE id = {id}"
            cursor.execute(query)
            connection.commit()      
            return {
                "status": "ok",
                "message": "Xóa thành công",
                "data" : []
            }
            
        except Exception as e:
            return {"error": str(e)}
    