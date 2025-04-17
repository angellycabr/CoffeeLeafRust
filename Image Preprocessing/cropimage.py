from PIL import Image
import numpy as np
import os

# Load the image
image_path = '../MATLAB/EE490/To_Convolve/Convolved'
cropped_image_paths = []
# Loop over all the files in the specified directory

for filename in os.listdir(image_path):
    # Check if the file is a PNG image
    if filename.endswith('.png'):
        # Construct the full file path
        file_path = os.path.join(image_path, filename)
        
        # Open the image
        image = Image.open(file_path)
        
        # Convert the image to a numpy array
        image_np = np.array(image)
        
        # Get the coordinates of the non-white (non-border) parts of the image
        non_white_coords = np.where(image_np < 255)
        
        # Get the bounding box of the non-white area
        x0, y0 = np.min(non_white_coords[1]), np.min(non_white_coords[0])
        x1, y1 = np.max(non_white_coords[1]), np.max(non_white_coords[0])
        
        # Crop the image to the bounding box
        cropped_image = image.crop((x0, y0, x1, y1))
        
        # Construct the path for saving the cropped image
        cropped_image_path = f'filteredimages/{filename}'
        cropped_image_paths.append(cropped_image_path)
        
        # Save the cropped image
        cropped_image.save(cropped_image_path)

# Return the list of paths for the cropped images
cropped_image_paths