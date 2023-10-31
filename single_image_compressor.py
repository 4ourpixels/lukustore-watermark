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


# Example usage
input_image_path = "image.jpg"
output_image_path = "compressed_image.png"
max_image_size = 624  # Maximum width or height in pixels

compress_image(input_image_path, output_image_path, max_image_size)
