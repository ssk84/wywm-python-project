import random
import json

# Function to create a new knight
def create_knight(knights):
    print("Let's create a knight!")
    user_input_ques = "What is knight's name? "
    # empty string not allowed
    kname = get_valid_str(user_input_ques)
    user_input_ques = "What is knight's group? "
    kgroup = get_valid_str(user_input_ques)
    user_input_ques = "What is knight's weapon? "
    kweapon = get_valid_str(user_input_ques)
    kage = random.randrange(20, 50)
    kid = random.randint(100, 1000)
    print("--- Your Knight ---")
    k = Knight(kid, kname, kage, kgroup, kweapon)
    print(json.dumps(k.__dict__))
    knights.append(k)

# Call a knight and change their data - name/age/group/weapon
# selecting option 0 will display the changes and exit function
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
        print("You have a knight!")
        #print("select_option: "+str(select_option))
        if int(select_option) == 1:
            update_item = "name"
        if int(select_option) == 2:
            update_item = "age"
        if int(select_option) == 3:
            update_item = "group"
        if int(select_option) == 4:
            update_item = "weapon"        
        if int(select_option) != 0:
            user_input_ques = "What is their new "+update_item+"? "
            new_item = get_valid_str(user_input_ques)
        for i in range(0, len(knights)):
            if(knights[i].id == knight_to_update_by_id):
                if select_option == 1:
                    knights[i].name = new_item
                if select_option == 2:
                    knights[i].age = new_item
                if select_option == 3:
                    knights[i].group = new_item
                if select_option == 4:
                    knights[i].weapn = new_item
                if select_option == 0:
                    print(json.dumps(knights[i].__dict__))
        if int(select_option) == 0:
            break

# Show the current knights and select one
def select_knight(knights):
    print("What knight would you like to update?")
    print_knights(knights)
    user_input_ques = "Select the knight's id: "
    knight_to_update_by_id = find_knight_by_id(user_input_ques, knights)
    return knight_to_update_by_id

# prints all the knights in json format
def print_knights(knights):
    for knight in knights:
        print(json.dumps(knight.__dict__))

# This is the menu to make our selections
def menu(knights_number):
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

# Find and return selected knight's id from knights list
def find_knight_by_id(user_input_ques, knights):
    is_valid = False
    while not is_valid:
        user_input_kid = input(user_input_ques)
        if user_input_kid.isdigit():
            for knight in knights:
                if knight.id == int(user_input_kid):
                    is_valid = True
                    break
            if not is_valid:
                print("No matching knight's id exists. Please re-enter.")
                continue
        else:
            print("Invalid knight's id must be number. Please re-enter.")
        print(user_input_kid)
    return int(user_input_kid)

# Generic function to validate the input menu option
# If invalid option is entered, user is prompted again to provide input
# For menu item => item=1, for knight item update => item=0
def get_valid_menu_option(item, user_input_ques):
    is_valid = False
    while not is_valid:
        selected_option = input(user_input_ques)
        if selected_option.isdigit(): 
            if int(item) == 1 and (int(selected_option) == 0
                                  or int(selected_option) == 1
                                  or int(selected_option) == 2):
                is_valid = True
            elif int(item) == 0 and (int(selected_option) == 1
                                     or int(selected_option) == 2
                                     or int(selected_option) == 3
                                     or int(selected_option) == 4
                                     or int(selected_option) == 0):
                is_valid = True
        else:
            print("Invalid option selected, please re-enter.")
            continue
    return int(selected_option)

# Function to check if non-empty string is provided in the input
def get_valid_str(askinput):
    is_empty = True
    while is_empty:
        userinput = input(askinput)
        if userinput != '':
            is_empty = False
            break
        else:
            print("Input cannot be empty. Please enter a string.")
            continue
    return userinput

# Knight class
class Knight:
    def __init__(self, id, name, age, group, weapon):
        self.id = id
        self.name = name
        self.age = age
        self.group = group
        self.weapon = weapon

# Setting the scene
knights_number = 0
knights = []
options = []

# Run the program
menu(knights_number)



