# Made by Jan de Geest

# Transfer python scripts From USB drive / network share to folder on Rpi main drive.
# Python folder Maintenance

# Import classes
from oscontrol.FileMigration import FileMigration

# Objects / parameters
source_dir = r' ' #@ path
target_dir = r' ' #@ path
file_type = '.py'

py_migration = FileMigration(source_dir, target_dir, file_type)

myloop = True 


# Menu text
print(" \n Python scripts maintenance menu:")
print(" ")
print("1. Import all scripts from external drive a.k.a. shared network folder")
print("2. Move all scripts from external drive a.k.a. shared network folder.")
print("3. Purge all files in Python scripts folder")
print("0. Exit")
print(" ")

while myloop == True:
    try: 
        user_input = int(input("Choose option: \n"))

        if user_input < 0 or user_input > 3:
            print('Chosen number is no menu option.')

        else:
            if user_input == 1:
                py_migration.copy()
                
            elif user_input == 2:
                py_migration.move()

            elif user_input == 3:
                py_migration.purge()

            elif user_input == 0:                
                print("\n Exit")
                myloop = False
                
            else:  
                print("\n Script error. \n Closing down menu...")
                myloop = False
                
    except ValueError:
        print('You have to type a number.')
