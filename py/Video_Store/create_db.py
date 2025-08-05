'''
Author: Daniel Mulligan
Date: 25/03/2025
Description: This script creates the database and tables.
File Name: create_db.py
Notes:
*/
'''

import mysql.connector
import database
from mysql.connector import errorcode

def create() : 
    try:
        # Step 1: Connect to MySQL Server (without database)
        iconn = database.init_connect()
        
        icur = iconn.cursor()

        # Step 2: Create database if it does not exist
        icur.execute("CREATE DATABASE IF NOT EXISTS video_store")
        print("Database 'video_store' checked/created successfully!")

        # Close connection and reconnect to use the new database
        icur.close()
        iconn.close()

        # Step 3: Reconnect to the 'video_store' database
        conn = database.connect_to_db()
        
        cur = conn.cursor()

        # Disable foreign key checks
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")

        # Drop tables if they exist
        cur.execute("DROP TABLE IF EXISTS hire;")
        cur.execute("DROP TABLE IF EXISTS customers;")
        cur.execute("DROP TABLE IF EXISTS videos;")

        # Re-enable foreign key checks
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")

        cur.close()

        # Step 4: Create 'customers' table
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE customers
        (
                custId INT PRIMARY KEY AUTO_INCREMENT,
                fname VARCHAR(40) NOT NULL,
                sname VARCHAR(40) NOT NULL,
                address VARCHAR(40) NOT NULL,
                phone VARCHAR(10) NOT NULL UNIQUE
        );
        """)
        cur.close()
        conn.commit()
        print("customers Table created successfully")

        # Step 5: Create 'videos' table
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE videos
        (
                videoId INT NOT NULL,
                videoVer INT NOT NULL,
                vname VARCHAR(15) NOT NULL,
                type VARCHAR(1) NOT NULL,
                dateAdded DATE NOT NULL
        );
        """)
        cur.close()
        conn.commit()
        print("videos Table created successfully")

        # Step 6: Create 'hire' table with foreign keys
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE hire
        (
                custId INT NOT NULL,
                videoId INT NOT NULL,
                videoVer INT NOT NULL,
                dateHired DATE NOT NULL,
                dateReturn DATE
        );
        """)
        cur.close()
        conn.commit()
        print("hire Table created successfully")

        # Step 7: Close the connection
        conn.close()
        print("MySQL connection closed.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect user name or password!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if __name__ == "__main__":  
    create()