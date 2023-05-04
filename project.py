"""Module to generate random numbers"""
import random


# prints all the knights in json format
def print_knights(knights):
    
    for knight in knights:
        Knight.display_knight(knight)


# Function to create a unique knight_id
def create_id(knights):
    
    knights_id = random.randint(100,200)

    try:
        knight_exists= find_knight_by_id(knights_id, knights)
        if knight_exists is None:
            return knights_id
        else:
            create_id(knights)
    except Exception as err:
        print("You can't create anymore knights! The kingdom is full.")
        print(err)


# Function to create a new knight object and save to the list
def create_knight(knights):
    
    print("Let's create a knight!")
    
    user_input_ques = "What is knight's name? "
    # empty string not allowed
    knights_name = get_valid_str(user_input_ques)
    user_input_ques = "What is knight's group? "
    knights_group = get_valid_str(user_input_ques)
    user_input_ques = "What is knight's weapon? "
    knights_weapon = get_valid_str(user_input_ques)
    knights_age = random.randrange(20, 50)
    
    # To assure unique knight_id is created
    knights_id = create_id(knights)

    if knights_id is None:
        return
    else:
        print("--- Your Knight ---")
        k = Knight(knights_id, knights_name, knights_age, knights_group, knights_weapon)
        knights.append(k)
        Knight.display_knight(k)


# Displays all the knights in the list, validates knight_id exists and returns it
def select_knight(knights):
    
    try:
        """If there are no knights, display the msg to create knights list"""
        if len(knights)<1:
            print("There are no knights to update. Create knights first.")
            menu()
        else:
            print("What knight would you like to update?")
            print_knights(knights)
        
        user_input_ques = "Select the knight's id to update: "
        while True:
            knight_to_update = get_knight_to_update(user_input_ques, knights)
            if not knight_to_update is None:
                return knight_to_update
    
    except Exception as err:
        print(err)


# Get a valid knight_id from user input for change_data function
def get_knight_to_update(user_input_ques, knights):
    
    try:
        user_input_knight_id = int(input(user_input_ques))
        
        # Check if given knight_id exists in the list or not
        knight_found = find_knight_by_id(user_input_knight_id, knights)

        if not knight_found is None:
            return knight_found
        else:
            err = "No matching knight's id exists. Please re-enter."
            raise Exception(err)
            
    except Exception as err:
        print(err)


# Find and return selected knight from knights list
def find_knight_by_id(knight_id, knights):
    
    selected_knight = None
    if len(knights) > 0:
        for knight in knights:
            if knight.id == int(knight_id):
                selected_knight = knight
    
    #print(selected_knight)
    return selected_knight

""" 
Call a knight and change their data - name/age/group/weapon. 
Selecting option 0 will display the updated changes to the knight and exit function 
"""
def change_data(knight_to_update):

    try:
        print("--- What would you like to update? ---")
        print("1.Knight's name")
        print("2.Knight's age")
        print("3.Knight's group")
        print("4.Knight's weapon")
        print("0.Exit change data")

        # Set menu options for user
        menu_options = [0,1,2,3,4]
        user_input_ques = "Select your option from "+str(menu_options)+" : "
        select_option = get_valid_menu_option(menu_options, user_input_ques)

        update_item = ''
        new_item = ''
        match select_option:    
            case 1:
                update_item = "name"
            case 2:
                update_item = "age"
            case 3:
                update_item = "group"
            case 4:
                update_item = "weapon"
            case 0:
                return
    
        if select_option != 0:
            user_input_ques = str("What is their new "+update_item+"? ")
            new_item = get_valid_str(user_input_ques)
            update_knight(select_option, knight_to_update, new_item)

        change_data(knight_to_update)

    except:
        print("Error occurred during knight update")
        change_data(knight_to_update)


# Function to update the knight item
def update_knight(select_option, knight_to_update, new_item):
    
    try:
        match select_option:
            case 1:
                knight_to_update.name = new_item
            case 2:
                knight_to_update.age = new_item
            case 3:
                knight_to_update.group = new_item
            case 4:
                knight_to_update.weapon = new_item
        
        Knight.display_knight(knight_to_update)
    except Exception as err:
        print("Error occurred during update_knight")
        print(err)
 

""" 
Generic function to validate the input menu option
If invalid option is entered, user is prompted again to provide input
Pass the menu_options array and input ques as parameters
"""
def get_valid_menu_option(menu_options, user_input_ques):
    err = "Invalid option selected, choose from the menu: "+str(menu_options)
    try:
        selected_option = int(input(user_input_ques))

        if selected_option in menu_options:
            return int(selected_option)
        else:
            raise Exception(err)
    except:
        print(err)
        get_valid_menu_option(menu_options, user_input_ques)


# Function to check if non-empty string is provided in the input
def get_valid_str(user_input):
    
    err = "Input cannot be empty. Please enter a string."
    
    try:
        valid_str = input(user_input)
        if valid_str != '' and not valid_str.isspace():
            return valid_str
        else:
            raise Exception(err)
    except:
        print(err)
        get_valid_str(user_input)


# Knight class
class Knight:
    def __init__(self, id, name, age, group, weapon):
        self.id = id
        self.name = name
        self.age = age
        self.group = group
        self.weapon = weapon
    
    def display_knight(self):
        print(self.__dict__)

# This is the main menu to begin the program
def menu():
    
    try:        
        print("What do you want to do")
        print("1: Create a new knight")
        print("2: Update your knight")
        print("0: Exit")
        
        # Set menu options for user
        menu_options = [0,1,2]
        user_input_ques = "Select option from "+str(menu_options)+" : "
        menu_item = get_valid_menu_option(menu_options, user_input_ques)
        
        if menu_item == 0:
            print_knights(knights)
            exit(0)
        elif menu_item == 1:
            create_knight(knights)
        elif menu_item == 2:
            knight_to_update = select_knight(knights)
            change_data(knight_to_update)
        
        menu()

    except Exception as err:
        print(err)


# Setting the scene
knights = []

# Run the program
menu()