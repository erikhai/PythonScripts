import os
from collections import Counter
import shutil

import os
import comtypes

def convert_word_to_pdf(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # Skip non-Word files
        if not filename.lower().endswith('.docx'):
            continue

        # Generate the output PDF filename
        output_filename = os.path.splitext(filename)[0] + '.pdf'
        output_path = os.path.join(output_folder, output_filename)

        # Convert Word to PDF
        try:
            convert(input_path, output_path)
            print(f"Converted {filename} to {output_filename}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")



def create_folder(sourcefile: str):

    
    downloads_path = sourcefile

    # Create a new folder 
    new_folder_path = os.path.join(downloads_path, "Word to PDF")

    try:
        # Create the folder if it doesn't exist
        os.makedirs(new_folder_path)
        print(f"Folder '{new_folder_path}' created successfully!")
    except FileExistsError:
        print(f"Folder '{new_folder_path}' already exists.")
    return new_folder_path





def check_folder_existence(folder_path):
    if os.path.exists(folder_path):
        return True
    return False


        


def main():
    

    while True: #Keep asking user for a folder path until a valid path is entered.
        file_path = input("Please enter a folder path: ")
        if (check_folder_existence(file_path)):
            break
        else:
            print("Please enter a valid folder path!!")

    print("Converting files...\n")

    convert_word_to_pdf(file_path, create_folder(file_path))
        
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