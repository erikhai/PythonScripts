import os
from collections import Counter
import shutil



def move_files_to_folder(source_folder, file_type):
    
    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)

        # Check if the file is of file type
        if filename.lower().endswith(file_type) and os.path.isfile(source_file):
            destination_folder = create_sorted_files_folder(source_folder, file_type) #Create a folder
            destination_file = os.path.join(destination_folder, filename)
            #os.path.join() This function is used to join one or more path components intelligently. 
            # It takes care of using the correct path separator
            
            # Move the current file into the destination folder
            try:
                shutil.move(source_file, destination_file)
                print(f"Moved: {filename} to {destination_folder}")
            except FileNotFoundError:
                print(" ")
            except PermissionError as e:
                print(f"Failed to move {filename} to {destination_folder}")

def create_sorted_files_folder(sourcefile: str, filename: str):

    
    downloads_path = sourcefile

    # Create a new folder 
    new_folder_path = os.path.join(downloads_path, "File Type " + filename)

    try:
        # Create the folder if it doesn't exist
        os.makedirs(new_folder_path)
        print(f"Folder '{new_folder_path}' created successfully!")
    except FileExistsError:
        print(f"Folder '{new_folder_path}' already exists!")  
    return new_folder_path





def check_folder_existence(folder_path):
    if os.path.exists(folder_path):
        return True
    return False

def getting_count_of_files(folder_path):
    file_types = []
    unique_file_types = []

    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path): 
        #The os.walk() function generates file names in a directory tree. 
        # It returns a tuple containing the root directory, a list of subdirectories, and a list of filenames in the given directory. 
        # For each iteration, root is set to the current directory path, dirs is a list of subdirectories in the current directory,
        #  and files is a list of filenames in the current directory.
        for file in files: #This goes through all the files in the current directory
            # Get the file extension
            _, extension = os.path.splitext(file)
            # The os.path.splitext() function splits a path into its root and extension. 
            # The variable _ is a convention to indicate that we are not using the root part of the path. 
            # The extension variable will contain the file extension (including the dot).
            file_types.append(extension.lower())  # Convert to lowercase for consistency

    # Count the occurrences of each file type
    file_types_count = Counter(file_types)

    # Display the unique file types and their counts
    print("Unique file types in the folder:")
    print(folder_path)
    for file_type, count in file_types_count.items():
        print(f"{file_type}: {count} file(s)")
        unique_file_types.append(file_type)
    return unique_file_types


        


def main():
    

    while True: #Keep asking user for a folder path until a valid path is entered.
        file_path = input("Please enter a folder path: ")
        if (check_folder_existence(file_path)):
            break
        else:
            print("Please enter a valid folder path!!")

    unique_file_types = getting_count_of_files(file_path)   #Get all the unique file types in that folder path  
    print("Sorting files...\n")

    for file_type in unique_file_types:
        move_files_to_folder(file_path, file_type) #Provide the source folder path and the file type we wish to move around

    while True: #Ask the user if they wish to sort out another folder or not.
        choice = input("Would you like to sort another folder? [Y/N] (not case sensitive) ")
        if (choice == "Y" or choice == "y" or choice == "N" or choice == "n"):
            break
        else:
            print("Please enter a valid choice!!")

    if (choice == "Y" or choice == "y"):
        main()




if __name__ == "__main__":
    main()