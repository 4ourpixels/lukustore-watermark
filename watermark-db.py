from PIL import Image
import os
import time


def add_watermark(input_path, output_path, watermark_path, watermark_scale):
    with Image.open(input_path) as image:
        # Calculate the new dimensions based on the desired scale
        watermark_width = int(image.width * watermark_scale)
        watermark_height = int(image.height * watermark_scale)

        # Open the watermark image and resize it
        with Image.open(watermark_path) as watermark:
            watermark.thumbnail(
                (watermark_width, watermark_height), Image.ANTIALIAS)

            # Calculate the position to place the watermark at the bottom left corner
            bottom_left_position = (
                200, image.height - watermark.height - 200)
            top_right_position = (image.width - watermark.width - 500, 500)

            # Create a copy of the image and paste the watermark on it at the bottom left
            watermarked_image = image.copy()
            watermarked_image.paste(
                watermark, bottom_left_position, mask=watermark)

            # Paste the watermark on it at the top right
            watermarked_image.paste(
                watermark, top_right_position, mask=watermark)

        # Save the watermarked image
        watermarked_image.save(output_path)


# Define the input and output paths
input_folder = "target"
output_folder = "output"
watermark_path = "watermark-ring-black.png"
watermark_scale = 0.1  # Adjust the watermark scale as needed

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the total number of items in the input folder
total_items = sum(len(files) for _, _, files in os.walk(input_folder))

# Initialize a counter for the number of processed items
processed_items = 0

# Start the timer
start_time = time.time()

# Iterate through the input folder and its subfolders
for root, dirs, files in os.walk(input_folder):
    for file in files:
        # Check if the file is an image
        if file.endswith((".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG")):
            # Compose the input and output file paths
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_folder, file)

            # Add watermark to the image and save it to the output folder
            add_watermark(input_file_path, output_file_path,
                          watermark_path, watermark_scale)

            # Increment the processed items counter
            processed_items += 1

            # Calculate and print the percentage completed
            percent_completed = (processed_items / total_items) * 100
            print(f"Processing: {percent_completed:.2f}% completed")

# Stop the timer
end_time = time.time()

# Calculate and print the total elapsed time
elapsed_time = end_time - start_time
print(
    f"Elapsed time: {elapsed_time:.2f} seconds.\nItems: {total_items}.")
