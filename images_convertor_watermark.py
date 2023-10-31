from PIL import Image
from PIL import ImageDraw
import os


def compress_and_add_watermark(input_path, output_path, max_size, watermark_path, watermark_scale):
    with Image.open(input_path) as image:
        # Calculate the aspect ratio to maintain the image's original proportions
        width, height = image.size
        aspect_ratio = width / height

        # Calculate the new dimensions based on the desired maximum size
        new_width = int(max_size * aspect_ratio)
        new_height = max_size

        # Resize the image while maintaining the aspect ratio
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create a copy of the resized image to apply the watermark
        watermarked_image = resized_image.copy()

        # Check if the watermark file exists
        if os.path.exists(watermark_path):
            # Open the watermark image and resize it while maintaining aspect ratio
            with Image.open(watermark_path) as watermark:
                # Calculate the new dimensions based on the desired scale (e.g., 70% reduction)
                watermark_width = int(watermark.size[0] * watermark_scale)
                watermark_height = int(watermark.size[1] * watermark_scale)

                # Resize the watermark while maintaining the aspect ratio
                watermark.thumbnail(
                    (watermark_width, watermark_height), Image.ANTIALIAS)

                # Calculate the position to place the watermark at the bottom right corner
                watermark_position = (
                    new_width - watermark.width, new_height - watermark.height)

                # Paste the watermark onto the watermarked image
                watermarked_image.paste(
                    watermark, watermark_position, mask=watermark)

        # Save the watermarked and compressed image
        watermarked_image.save(output_path)


# Define the input and output paths
input_folder = "target"
output_folder = "output"
watermark_path = "watermark.png"
watermark_scale = 0.7  # 70% reduction in size

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
            output_file_path = os.path.join(output_folder, file)

            # Compress the image, add watermark if it exists, and save it to the output folder
            compress_and_add_watermark(input_file_path, output_file_path, max_size=1024,
                                       watermark_path=watermark_path, watermark_scale=watermark_scale)
