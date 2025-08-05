'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script creates functions in a class that query and insert data into the flowwing tables of the database:
             videos, customers and hire.
File Name: hire_manager.py
Notes:
*/
'''

class HireManagement:
    
    #initializes the CustomerManager with a database connection
    def __init__(self, conn):
       
        self.conn = conn
        self.cursor = conn.cursor()

    
    #checks if a video exists by ID
    def check_video_id(self, video_id):
        
        query = "SELECT * FROM videos WHERE videoId = %s"
        self.cursor.execute(query, (video_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    #checks if a video version exists for a given video ID
    def check_video_ver(self, video_id, video_ver):
        query = "SELECT videoVer FROM videos WHERE videoId = %s AND videoVer = %s"
        self.cursor.execute(query, (video_id, video_ver))
        result = self.cursor.fetchone()
        return result[0] if result else None

    #checks if a customer exists by ID
    def check_customer_id(self, cust_id):
        
        query = "SELECT * FROM customers WHERE custId = %s"
        self.cursor.execute(query, (cust_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    #hires out a video to a customer
    def hire_out(self, cust_id, video_id, video_ver, date_hired):
        
        insert_query = """INSERT INTO hire (custID, videoID, videoVer, dateHired)
                          VALUES (%s, %s, %s, %s)"""
        self.cursor.execute(insert_query, (cust_id, video_id, video_ver, date_hired))
        self.conn.commit()
        print(f"Video ID: '{video_id}' Version: '{video_ver}' hired out successfully!")

    #closes the database cursor and connection
    def close(self):
        
        self.cursor.close()
        self.conn.close()

    #helper method to clear unread results
    def _clear_results(self):
        
        while self.cursor.nextset():
            pass