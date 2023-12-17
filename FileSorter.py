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
            #os.path.join() This function is used to join one or more path components. 
           
            
            # Move the current file into the destination folder
            try:
                shutil.move(source_file, destination_file)
                print(f"Moved: {filename} to {destination_folder}")
            except FileNotFoundError:
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
        print(" ")
    return new_folder_path





def check_folder_existence(folder_path):
    if os.path.exists(folder_path):
        return True
    return False

def getting_count_of_files(folder_path):
    file_types = []

    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)
            file_types.append(extension.lower())  # Convert to lowercase for consistency

    # Count the occurrences of each file type
    file_types_count = Counter(file_types)

    # Display the unique file types and their counts
    print("Unique file types in the folder:")
    for file_type, count in file_types_count.items():
        print(f"{file_type}: {count} file(s)")


        


def main():
    

    while True:
        file_path = input("Please enter a folder path: ")
        if (check_folder_existence(file_path)):
            break
        else:
            print("Please enter a valid folder path!!")

    getting_count_of_files(file_path)    
    print("Sorting files...")

    while True:
        choice = input("Would you like to sort another folder? [Y/N] (not case sensitive) ")
        if (choice == "Y" or choice == "y" or choice == "N" or choice == "n"):
            break
        else:
            print("Please enter a valid choice!!")

    if (choice == "Y" or choice == "y"):
        main()




if __name__ == "__main__":
    main()