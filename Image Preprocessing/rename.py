import os

# WARNING: Be wary of where you run this code. Otherwise, you risk renaming the wrong files. 

# Get the current working directory
current_directory = os.getcwd()

# Get the path to the folder containing the images
folder_path = os.path.join(current_directory)

# Create a list of all the images in the folder
image_list = os.listdir(folder_path)

# Loop through the list of images
for image in image_list:
    # Get the extension of the image
    extension = image.split(".")[-1]

    if extension != "py":
        # Define the base name
        base_name = "leaf_rust_"
        
        # Initialize a counter
        count = 0
        
        # Construct the new name
        while True:
            new_name = f"{base_name}{count:02d}.{extension}"
            if new_name not in image_list:
                break
            count += 1
        
        # Rename the image
        os.rename(os.path.join(folder_path, image), os.path.join(folder_path, new_name))
        # Update the image_list to reflect the new name
        image_list[image_list.index(image)] = new_name
