'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script creates a server on a specfied port and handels the arguments sent from the client.
File Name: server.py
Notes: Please maker sure you are using a valid port on line 85 for the server to create the TCP connection.
*/
'''

import socket #imports socket for TCP connection
import database #imports database connecting function
from datetime import datetime #imports datetime function

#defines the server function to collect the phone number from customers and pass it back to the client
def get_customer_by_phone(cursor, phone_number): 
    query = "SELECT * FROM customers WHERE phone = %s"
    cursor.execute(query, (phone_number,))
    return cursor.fetchone()

#defines the server function to collect the customer information from the client and inserts it into the database
def add_new_customer(cursor, conn, fname, sname, address, phone):
    insert_query = """INSERT INTO customers (fname, sname, address, phone)
                      VALUES (%s, %s, %s, %s)"""
    cursor.execute(insert_query, (fname, sname, address, phone))
    conn.commit()
    return f"New customer '{fname} {sname}' added successfully!"

#handles the client
def handle_client(conn, cur, db_conn):
    try:
        #continuously listen for client messages
        while True:
            #receive data from the client (up to 1024 bytes) and decode it
            data = conn.recv(1024).decode()
            #if no data is received, break the loop (client disconnected)
            if not data:
                break
            #split received data using '|' as a delimiter
            parts = data.split('|')
            command = parts[0]
            #handles GET command - retrieves customer data by phone number
            if command == "GET":
                phone_number = parts[1]
                row = get_customer_by_phone(cur, phone_number)
                if row:
                    #if customer is found, return their name and address
                    response = f"FOUND|{row[1]}|{row[4]}"
                else:
                    response = "NOT_FOUND"
             #handles ADD command - add a new customers to the database
            elif command == "ADD":
                fname, sname, address, phone = parts[1:]
                response = add_new_customer(cur, db_conn, fname, sname, address, phone)
            #handles TIME command - return the current date and time
            elif command == "TIME":
                # Send current date and time
                response = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #handles invalid commands
            else:
                response = "ERROR|Invalid command"
            #sends a response back to the client
            conn.send(response.encode())

    #handles any exceptions and send an error message to the client
    except Exception as e:
        conn.send(f"ERROR|{str(e)}".encode())

    finally:

         #ensure resources are properly closed before exiting
        conn.close()

def time():

    #establish a connection to the database
    conn = database.connect_to_db()   
    #if the connection fails, exit the function
    if conn is None:
        return
    #creates a cursor object to interact with the database
    cur = conn.cursor()
    #creates a socket for the server (IPv4, TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #binds the server to all available network interfaces (0.0.0.0) on port 6088
    server.bind(("0.0.0.0", 6088)) #Please make sure to replace 6088 with you port number if nessicary
    #starts listening for incoming connections (max queue of 5 clients)
    server.listen(5)
    print("Server is running on port...")
    try:
        #continuously accepts and handle client connections
        while True:
            #accepts a new client connection
            client_conn, _ = server.accept()
             #passes the client connection, cursor, and database connection to the handler
            handle_client(client_conn, cur, conn)

    except KeyboardInterrupt:

        #handles server shutdown when interrupted (Ctrl+C)
        print("\nShutting down server...")

    finally:

         #ensures all resources are properly closed before exiting
        cur.close()
        conn.close()
        server.close()


if __name__ == "__main__":
    time()