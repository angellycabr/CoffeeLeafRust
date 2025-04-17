import cv2 as cv
import os
import glob

# Function to apply histogram equalization to an image
def equalize_image(image_path, output_path):
    # Read the image
    src = cv.imread(image_path)
    if src is None:
        print(f'Could not open or find the image: {image_path}')
        return
    # Convert to grayscale (if you want to work with color images, adjust accordingly)
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # Apply histogram equalization
    equalized = cv.equalizeHist(src_gray)
    # Save the equalized image
    cv.imwrite(output_path, equalized)

# Specify the directory containing the images and the directory to save the equalized images
source_directory = 'filteredimages/Healthy'
output_directory = 'equalizedimages/Healthy'

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get all image files in the source directory
image_files = glob.glob(os.path.join(source_directory, '*'))

# Process each image
for image_path in image_files:
    # Construct the output image path
    file_name = os.path.basename(image_path)
    output_path = os.path.join(output_directory, file_name)
    
    # Apply histogram equalization and save the image
    equalize_image(image_path, output_path)
    print(f'Processed and saved: {output_path}')