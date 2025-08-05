'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script adds a date returned to a hired video with the functions of the ReturnManager and VideoManager classes.
File Name: return_video.py
Notes:
*/
'''

import database
import start_menu
from return_manager import ReturnManager
from video_manager import VideoManager
import clear_screen as cs

class VideoReturn:
    
    #establishes database connection
    def __init__(self):
        self.conn = database.connect_to_db()
        if self.conn is None:
            exit()
        self.cur = self.conn.cursor()
        self.return_manager = ReturnManager(self.cur, self.conn)
        
    
    def process_video_return(self):
        try:
            cs.clear()

            self.video_manager = VideoManager

            #loops until a valid Video ID is entered
            while True:
                videoId = input("Please enter Video ID or enter x to exit: ")
                if videoId == "x":
                    start_menu.menu()
                else:
                    checkVideo = self.return_manager.return_video_id(videoId)
                    if checkVideo is not None:
                        break  
                    print("Invalid Video ID. Please try again.") 

            #loops until a valid Video Version is entered
            while True:
                videoVer = input("Please enter Video Version or enter x to exit: ")
                if videoVer == "x":
                    start_menu.menu()
                else:
                    checkVideoVer = self.return_manager.return_video_ver(videoId)
                    if checkVideoVer is not None:
                        break  
                    print("Invalid Video Version. Please try again.")  

            print("Video ID accepted!") 

            #fetches time from server through the VideoManager class       
            dateReturned = self.video_manager.fetch_time()

            # Get date and process hiring
            self.return_manager.return_vid(videoId, videoVer, dateReturned)

        #captures and prints error
        except Exception as err:
            print(f"Error: {err}")
        
        #closes all connections
        finally:
            self.cur.close()
            self.conn.close()

#ensures this script runs only when executed directly
if __name__ == "__main__":
    video_return = VideoReturn()
    video_return.process_video_return()