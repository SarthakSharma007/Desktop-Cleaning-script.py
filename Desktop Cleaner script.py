import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    """
    Creates a subfolder inside the given folder_path.
    If the subfolder already exists, it does nothing.
    Returns the complete path of the subfolder.
    """
    subfolder_path = os.path.join(folder_path, subfolder_name)
    
    # If the subfolder does not exist, create it
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    return subfolder_path


def move_file_to_subfolder(file_path, subfolder_path):
    """
    Moves a file from its current location to the specified subfolder.
    """
    shutil.move(file_path, subfolder_path)


def clean_folder(folder_path):
    """
    Organizes all files in the given folder into subfolders based on file type (extension).
    
    For example:
    - All '.jpg' files are moved into 'JPG Files' folder
    - All '.pdf' files are moved into 'PDF Files' folder
    """
    for filename in os.listdir(folder_path):
        file_full_path = os.path.join(folder_path, filename)

        # Check if it's actually a file (not a folder)
        if os.path.isfile(file_full_path):
            # Extract file extension (e.g., 'jpg', 'pdf')
            file_extension = filename.split('.')[-1].lower()

            if file_extension:  # Make sure the file has an extension
                # Create a folder name based on the extension
                subfolder_name = f"{file_extension.upper()} Files"
                
                # Create the subfolder if it doesn't exist
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                
                # Move the file into the corresponding subfolder
                move_file_to_subfolder(file_full_path, subfolder_path)

                print(f"Moved: {filename} -> {subfolder_name}/")


if __name__ == "__main__":
    print("📂 Desktop Cleaner Script Started")

    # Dynamically find the current user's Downloads folder
    folder_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # Check if the Downloads folder exists
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("✅ Cleaning complete. Your Downloads folder is now organized!")
    else:
        print("❌ Invalid folder path. Please ensure the path is correct and try again.")
