'''
Author: Daniel Mulligan
Date: 24/03/2025
Description: This script runs a menu whereby the user may navigate the functions of the program.
File Name: start_menu.py
Notes:
*/
'''

import start_menu #imports itself
from customer_register import CustomerRegistration #imports CustomerRegistartion class
from video_register import VideoRegistration #imports the VideoRegistartion class
from hire_out_video import VideoStoreHiring #imports the VideoStoreHiring class
from return_video import VideoReturn #imports the VideoReturn class
import clear_screen as cs 


def menu(): #defines the function that acts as the start menu for the user

    cs.clear() #clears the screen 
    
    #prints the menu for referencing th users selection
    print ("=======================================================\n"
       "|                  Video Store                        |\n"
       "=======================================================\n"
       "|  1. Register Customer                               |\n"
       "|  2. Register Movie                                  |\n"
       "=======================================================\n"
       "|  3. Hire Out Movie                                  |\n"
       "|  4. Return Movie                                    |\n"
       "=======================================================\n"
       "|  x. Exit                                            |\n"
       "=======================================================\n")

    while True: #runs a while True function looking for user to enter one of the options

        userIn = input("Choice: ") # takes input from the user
        if userIn == "1": #runs if the user selects option 1
            #runs the "run_video_store_client" function from CustomerRegistraion class
            CustomerRegistration.run_video_store_client()
            #asks user to either go back tot the start menu or exit the program
            next = input("Enter M to return to the Start Menu \nOr enter x to exit: ")                          
           
            if next == "x":
                cs.clear()
                exit()

            elif next == "M":
                cs.clear()
                start_menu.menu()

        if userIn == "2": #runs if the user selects option 2

            #runs the "register_movie" function from VideoRegistration class
            video_registration = VideoRegistration()
            video_registration.register_movie()

            #asks user to either go back tot the start menu or exit the program
            next = input("Enter any value to return to the Start Menu \n Or enter x to exit: ")
            if next == "x":
                cs.clear()
                exit()

            elif next == "M":
                cs.clear()
                start_menu.menu()


        if userIn == "3": #runs if the user selects option 3

            #runs the "process_hiring" function from VideoStoreHiring class
            hiring_system = VideoStoreHiring()
            hiring_system.process_hiring()

            #asks user to either go back tot the start menu or exit the program
            next = input("Enter any value to return to the Start Menu \n Or enter x to exit: ")
            if next == "x":
                cs.clear()
                exit()

            elif next == "M":
                cs.clear()
                start_menu.menu()

        if userIn == "4": #runs if the user selects option 4

            #runs the "process_video_return" function from VideoReturn class
            video_return = VideoReturn()
            video_return.process_video_return()
            
            #asks user to either go back tot the start menu or exit the program
            next = input("Enter any value to return to the Start Menu \n Or enter x to exit: ")
            if next == "x":
                    cs.clear()
                    exit()

            elif next == "M":
                cs.clear()
                start_menu.menu()


        if userIn == "x": #runs if the user selects the exit option
            cs.clear()           
            exit()

        else:
            while True: #runs a while True function if no valid option is chosen from the menu
                end = input("please enter a valid option: ")
                if end == "M":
                    menu()
                elif end == "x":
                    exit()

