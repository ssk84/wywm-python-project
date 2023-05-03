"""Module to generate random numbers"""
import random
import json

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
    while True:
        knights_id = random.randint(100, 1000)
        is_exists = find_knight_by_id(knights_id, knights)
        if is_exists:
            continue
        else:
            break
    
    print("--- Your Knight ---")
    k = Knight(knights_id, knights_name, knights_age, knights_group, knights_weapon)
    knights.append(k)
    Knight.display_knight(k)


""" 
Call a knight and change their data - name/age/group/weapon. 
Selecting option 0 will display the updated changes to the knight and exit function 
"""
def change_data(knight_to_update_by_id, knights):
    while True:
        print("--- What would you like to update? ---")
        print("1.Knight's name")
        print("2.Knight's age")
        print("3.Knight's group")
        print("4.Knight's weapon")
        print("0.Exit")
        
        user_input_ques = "Select your option [0/1/2/3/4]: "
        select_option = get_valid_menu_option(0, user_input_ques)
        #print("You have a knight!")
        #print("select_option: "+str(select_option))
        
        update_item = ''
        new_item = ''
        match int(select_option):    
            case 1:
                update_item = "name"
            case 2:
                update_item = "age"
            case 3:
                update_item = "group"
            case 4:
                update_item = "weapon"
            case 0:
                pass
        
        if select_option != 0:
            user_input_ques = str("What is their new "+update_item+"? ")
            new_item = get_valid_str(user_input_ques) 
        
        for i in range(0, len(knights)):
            if(knights[i].id == knight_to_update_by_id):
                match select_option:
                    case 0:
                        Knight.display_knight(knights[i])
                    case 1:
                        knights[i].name = new_item
                    case 2:
                        knights[i].age = new_item
                    case 3:
                        knights[i].group = new_item
                    case 4:
                        knights[i].weapon = new_item
                if select_option != 0:
                    Knight.display_knight(knights[i])
        
        if int(select_option) == 0:
            break # breaks the while loop

# Displays all the knights in the list, validates knight_id exists and returns it
def select_knight(knights):
    """If there are no knights, display the msg to create knights list"""
    if len(knights)<1:
        print("There are no knights to update. Create knights first.")
        menu()
    else:
        print("What knight would you like to update?")
        print_knights(knights)
    
    user_input_ques = "Select the knight's id: "
    knight_to_update_by_id = get_knight_id_for_update(user_input_ques, knights)
    
    return knight_to_update_by_id


# prints all the knights in json format
def print_knights(knights):
    for knight in knights:
        Knight.display_knight(knight)


# This is the main menu to begin the program
def menu():
    while True:
        print("What do you want to do")
        print("1: Create a new knight")
        print("2: Update your knight")
        print("0: Exit")
        
        user_input_ques = "Selection number: "
        menu_item = get_valid_menu_option(1, user_input_ques)
        
        if menu_item == 0:
            print_knights(knights)
            exit(0)
        elif menu_item == 1:
            create_knight(knights)
        elif menu_item == 2:
            knight_to_update_by_id = select_knight(knights)
            change_data(knight_to_update_by_id, knights)


# Get a valid knight_id from user input for change_data function
def get_knight_id_for_update(user_input_ques, knights):
    is_valid = False
    
    while not is_valid:
        user_input_knight_id = input(user_input_ques)
        if user_input_knight_id.isdigit():
            # Check if given knight_id exists in the list or not
            is_found = find_knight_by_id(user_input_knight_id, knights)
            if is_found:
                is_valid = True
                break
            else:
                print("No matching knight's id exists. Please re-enter.")
                continue
        else:
            print("Invalid knight's id must be number. Please re-enter.")
        
        print(user_input_knight_id)
    
    return int(user_input_knight_id)


# Find and return selected knight's id from knights list
def find_knight_by_id(knight_id, knights):
    is_found = False
    for knight in knights:
        if knight.id == int(knight_id):
            is_found = True
            break
    
    return is_found


""" 
Generic function to validate the input menu option
If invalid option is entered, user is prompted again to provide input
For main menu item use item=1, for knight item update use item=0
"""
def get_valid_menu_option(item, user_input_ques):
    is_valid = False
    
    while not is_valid:
        selected_option = input(user_input_ques)
        
        if selected_option.isdigit():
            match item:
                case 0: # menu options for updating knight
                    if (int(selected_option) == 1
                        or int(selected_option) == 2
                        or int(selected_option) == 3
                        or int(selected_option) == 4
                        or int(selected_option) == 0):
                        is_valid = True
                case 1: # main menu options
                    if (int(selected_option) == 0
                        or int(selected_option) == 1
                        or int(selected_option) == 2):
                        is_valid = True
        else:
            print("Invalid option selected, please re-enter.")
            continue
    
    return int(selected_option)


# Function to check if non-empty string is provided in the input
def get_valid_str(user_input):
    is_empty = True
    
    while is_empty:
        valid_str = input(user_input)
        if valid_str != '':
            is_empty = False
            break
        else:
            print("Input cannot be empty. Please enter a string.")
            continue
    
    return valid_str


# Knight class
class Knight:
    def __init__(self, id, name, age, group, weapon):
        self.id = id
        self.name = name
        self.age = age
        self.group = group
        self.weapon = weapon
    
    def display_knight(self):
        print(json.dumps(self.__dict__))


# Setting the scene
knights = []

# Run the program
menu()



