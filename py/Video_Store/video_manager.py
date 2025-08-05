'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script creates functions in a class that query and insert data into the videos table of the MySQL database.
File Name: video_manager.py
Notes:This progam acts a client for the server please make sure you enter the correct matching server port in line 62.
*/
'''


import socket

class VideoManager:
    
    #initializes the CustomerManager with a database connection
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    #adds a new video to the database
    def register_movie(self, videoId, videoVer, vname, type, dateAdded):
        insert_query = """INSERT INTO videos (videoId, videoVer, vname, type, dateAdded)
                          VALUES (%s,%s, %s, %s, %s)"""
        self.cursor.execute(insert_query, (videoId, videoVer, vname, type, dateAdded))
        self.conn.commit()
        print(f"New Video '{vname} {type}' added successfully!")

    #returns the number of videos with the same name for video version
    def check_version(self, vidname):
        query = "SELECT COUNT(*) FROM videos WHERE vname = %s"
        self.cursor.execute(query, (vidname,))
        result = self.cursor.fetchone()
        return result[0] if result else None 

    #checks video ID from the captured name
    def get_video_id(self, vidname):
        query = "SELECT videoId FROM videos WHERE vname = %s"
        self.cursor.execute(query, (vidname,))
        result = self.cursor.fetchone()       
        return result[0] if result else None  

    #returns the highest video Id or 0 if empty
    def get_highest_video_id(self):
        query = "SELECT MAX(videoId) FROM videos"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0  

    #checks if the video Id exists and returns 1 higher if so
    def get_or_assign_video_id(self, vidname):
        existing_vid = self.get_video_id(vidname)

        if existing_vid is not None:
            return existing_vid  

        highest_vid = self.get_highest_video_id()
        return highest_vid + 1  # Assign new ID (highest ID + 1)
    
    #fetches the time from TCP server
    def fetch_time():
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP socket
            soc.connect(('localhost', 6088))  #Please make sure to replace 6088 with you port number if nessicary

            soc.send("TIME".encode())  # Send TIME command to server

            tm = soc.recv(1024).decode()  # Receive response from server
            soc.close()

            return tm