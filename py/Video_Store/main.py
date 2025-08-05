'''
Author: Daniel Mulligan
Date: 23/03/2025
Description: This script begins the program and assists the user in creating a new table if nessicary.
File Name: main.py
Notes:
*/
'''

import start_menu 
import create_db 
import clear_screen as cs 

print("Welcome") 

#defines athe fucntion to either create a new database or use an old one
def db(): 
    new_db = input("Would you like to set up a new database: Y or N: ") 

    if new_db == "Y": #runs if create a new database is selected
        
        cs.clear()  #clears the screen 
        create_db.create()  #calls the create_db function to set up the database
        
        #asks to go to main menu after creating the database
        next = input("Type M to continue to the menu, or type anything else to exit: ") 
        if next == "M":
            cs.clear()
            start_menu.menu()  #goes to the menu if 'M' is typed
        else: 
            cs.clear()
            print("Bye!")  #exits if anything else is typed

    elif new_db == "N":
        start_menu.menu()  #goes to the menu if 'N' is typed

    else:
        cs.clear()
        print("Please enter a valid answer.")  #prompts for valid answer if input is invalid
        db()  #recursively calls the db function if the input is invalid


db()  #calls the db function after printing 'Welcome'