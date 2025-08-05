'''
Author: Daniel Mulligan
Date: 25/03/2025
Description: This script registers a ne client with the functions of the CustomerManager class through a TCP connection to the server.
File Name: customer_register.py
Notes: This progam acts a client for the server please make sure you enter the correct matching server port in line 16.
*/
'''

import socket
import database  
from customer_manager import CustomerManager  #Import CustomerManager class

class CustomerRegistration:
    #Initialize the client with server details and DB connection
    def __init__(self, server_address="127.0.0.1", server_port=6088): #Please make sure to replace 6088 with you port number if nessicary
        
        self.server_address = server_address
        self.server_port = server_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = database.connect_to_db()  # Connect to Database
        self.customer_manager = CustomerManager(self.conn)

    def connect(self):
        #Establish connection to the server
        try:
            self.client.connect((self.server_address, self.server_port))
        except Exception as e:
            print(f"Error connecting to server: {e}")
            return False
        return True

    def handle_customer(self):
        #Handles customer lookup and registration
        phone_number = input("Please enter your Phone Number or enter x to exit: ")
        if phone_number.lower() == "x":
            return

        try:
            # First, check in the local database before contacting the server
            customer = self.customer_manager.get_customer_by_phone(phone_number)

            if customer:
                print(f"{customer[1]} {customer[2]}, phone number: {customer[4]} is already a customer.")
            else:
                print("No customer found, please register your details.")
                cfname = input("First Name: ")
                csname = input("Surname: ")
                caddress = input("Address: ")

                # Add the new customer to the database
                self.customer_manager.add_new_customer(cfname, csname, caddress, phone_number)

               
        #captures and prints error
        except Exception as err: 
            print(f"Error: {err}")

    #closes all connections
    def close(self):
        
        self.client.close()
        self.customer_manager.close()

#function to run the client as a standalone program
    def run_video_store_client():
        
        video_store_client = CustomerRegistration()

        if video_store_client.connect():
            video_store_client.handle_customer()

        video_store_client.close()

#ensures this script runs only when executed directly
    if __name__ == "__main__":
        run_video_store_client()