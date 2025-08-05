'''
Author: Daniel Mulligan
Date: 24/03/2025
Description: This script connects to the database via the MySQL connector.
File Name: database.py
Notes:Please make sure to change the MySQl server login details in lines 17-19 and 35-37.
*/
'''

import mysql.connector
from mysql.connector import errorcode

#Connect to MySQL Server (without database)
def init_connect():
    try:
        conn = mysql.connector.connect(
            user="root", #normally root but if not enter username
            passwd="EfAnA5085", #enter server password
            host="localhost", #normally localhost but if not enter host
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect username or password!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

#connects to the database vis MySQL connector
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            user="root", #normally root but if not enter username
            passwd="EfAnA5085", #enter server password
            host="localhost", #normally localhost but if not enter host
            database="video_store"
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect username or password!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    
    

