'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script registers a new video with the functions of the VideoManager class.
File Name: video_register.py
Notes:
*/
'''

import database
from video_manager import VideoManager
import clear_screen as cs

class VideoRegistration:

    #establishes database connection
    def __init__(self):
        
        self.conn = database.connect_to_db()
        if self.conn is None:
            raise Exception("Failed to connect to the database.")
        self.cur = self.conn.cursor()


    def register_movie(self):
        
        try:
            cs.clear()
            vidname = input("Please enter Video Name: ")
            vidtype = input("Please enter Video Type: ")

            video_manager = VideoManager(self.cur, self.conn)

            #gets or assigns a video ID
            vidId = video_manager.get_or_assign_video_id(vidname)

            #checks and sets the video version
            vidver = video_manager.check_version(vidname) + 1

            cs.clear()

            current_time = VideoManager.fetch_time()

            #registers a new video
            video_manager.register_movie(vidId, vidver, vidname, vidtype, current_time)

        #captures and prints error
        except Exception as err:
            print(f"Error: {err}")

        #closes all connections
        finally:
            self.cur.close()
            self.conn.close()

#nsures this script runs only when executed directly
if __name__ == "__main__":
    video_registration = VideoRegistration()
    video_registration.register_movie()


