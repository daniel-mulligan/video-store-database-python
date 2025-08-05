'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script creates functions in a class that query and insert data into the customers table of the MySQL database.
File Name: customer_manager.py
Notes:
*/
'''
class CustomerManager:
    
    #initializes the CustomerManager with a database connection
    def __init__(self, conn):
        
        self.conn = conn
        self.cursor = conn.cursor()

    #retrieves a customer by phone number
    def get_customer_by_phone(self, phone_number):
        
        query = "SELECT * FROM customers WHERE phone = %s"
        self.cursor.execute(query, (phone_number,))
        return self.cursor.fetchone()

    #adds a new customer to the database
    def add_new_customer(self, fname, sname, address, phone):
        
        insert_query = """INSERT INTO customers (fname, sname, address, phone)
                          VALUES (%s, %s, %s, %s)"""
        self.cursor.execute(insert_query, (fname, sname, address, phone))
        self.conn.commit()
        print(f"New customer '{fname} {sname}' added successfully!")

    #closes the database cursor and connection
    def close(self):
        
        self.cursor.close()
        self.conn.close()