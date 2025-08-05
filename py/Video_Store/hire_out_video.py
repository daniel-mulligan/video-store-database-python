'''
Author: Daniel Mulligan
Date: 26/03/2025
Description: This script hires out a movie with the functions of the VideoStoreHiring and VideoManager classes.
File Name: hire_out_video.py
Notes:
*/
'''

import database
import start_menu
import video_manager
import hire_manager
import clear_screen as cs


class VideoStoreHiring:

    #establishes database connection
    def __init__(self):

        self.conn = database.connect_to_db()
        if self.conn is None:
            print("Failed to connect to the database.")
            exit()
        self.cur = self.conn.cursor()
        self.hire_manager = hire_manager.HireManagement(self.conn)
        self.video_manager = video_manager.VideoManager

    def process_hiring(self):
        """Handles the hiring process by taking input and interacting with the database."""
        try:
            cs.clear()

            #loops until a valid Video ID is entered
            while True:
                videoId = input("Please enter Video ID or enter x to exit: ")
                if videoId.lower() == "x":
                    start_menu.menu()
                if self.hire_manager.check_video_id(videoId) is not None:
                    break
                print("Invalid Video ID. Please try again.")

            print("Video ID accepted!")

            #loops until a valid Video Version is entered
            while True:
                videoVer = input("Please enter Video Version or enter x to exit: ")
                if videoVer.lower() == "x":
                    start_menu.menu()
                if self.hire_manager.check_video_ver(videoId, videoVer) is not None:
                    break
                print("Invalid Video Version. Please try again.")

            print("Video Version accepted!")

            #loops until a valid Customer ID is entered
            while True:
                custId = input("Please enter Customer ID or enter x to exit: ")
                if custId.lower() == "x":
                    start_menu.menu()
                if self.hire_manager.check_customer_id(custId) is not None:
                    break
                print("Invalid Customer ID. Please try again.")

            print("Customer ID accepted!")
            
            #fetches time from server through the VideoManager class
            dateHired = self.video_manager.fetch_time()

            #process the hiring of the video
            self.hire_manager.hire_out(custId, videoId, videoVer, dateHired)

        #captures and prints error
        except Exception as err:
            print(f"Error: {err}")

        #calls function to close connections
        finally:
            self.close()

    #closes all connections
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

#ensures this script runs only when executed directly
if __name__ == "__main__":
    hiring_system = VideoStoreHiring()
    hiring_system.process_hiring()