from PIL import Image
import os


def compress_image(input_path, output_path, max_size):
    with Image.open(input_path) as image:
        # Calculate the aspect ratio to maintain the image's original proportions
        width, height = image.size
        aspect_ratio = width / height

        # Calculate the new dimensions based on the desired maximum size
        new_width = int(max_size * aspect_ratio)
        new_height = max_size

        # Resize the image while maintaining the aspect ratio
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Save the compressed image
        resized_image.save(output_path)


# Define the input and output paths
input_folder = "target-images"
output_folder = "output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through the input folder and its subfolders
for root, dirs, files in os.walk(input_folder):
    for file in files:
        # Check if the file is an image
        if file.endswith((".png", ".jpg", ".jpeg")):
            # Compose the input and output file paths
            input_file_path = os.path.join(root, file)
            # Add "mid_thumbnail_" prefix
            output_file_path = os.path.join(
                output_folder, "ss23_summer_jam_" + file)

            # Compress the image and save it to the output folder
            compress_image(input_file_path, output_file_path, max_size=1080)
