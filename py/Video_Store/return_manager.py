'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script creates functions in a class that query and insert data into the flowwing tables of the database:
             videos and hire.
File Name: return_video.py
Notes:
*/
'''

class ReturnManager:
    
    #initializes the CustomerManager with a database connection
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    #checks the video ID
    def return_video_id(self, vidId):
        query = "SELECT * FROM hire WHERE videoId = %s"
        self.cursor.execute(query, (vidId,))
        result = self.cursor.fetchone()
        self._clear_results()
        return result[0] if result else None  # Extract videoId or return None
    
    #checks the video version
    def return_video_ver(self, videoId):
        query = "SELECT videoVer FROM videos WHERE videoId = %s"
        self.cursor.execute(query, (videoId,))
        result = self.cursor.fetchone()
        self._clear_results()
        return result[0] if result else None
    
    #enters the data retrieved and the new date stamp into the hire table
    def return_vid(self, videoId, videoVer, dateReturned):
        update_query = """UPDATE hire 
                          SET dateReturn = %s 
                          WHERE videoId = %s AND videoVer = %s"""
        self.cursor.execute(update_query, (dateReturned, videoId, videoVer))
        self.conn.commit()
        print(f"Video ID: '{videoId}' returned successfully on '{dateReturned}'.")

    #helper method to clear unread results
    def _clear_results(self):
        
        while self.cursor.nextset():
            pass




