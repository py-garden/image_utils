from PIL import Image 
from typing import List
from fs_utils.main import process_files_recursively
import math
import os
import argparse

def nearest_power_of_two(value):
    """Find the nearest power of two greater than or equal to the value."""
    return 2 ** math.ceil(math.log2(value))

def resize_image_to_power_of_two(image_path):
    """Resize the image to the nearest power of two dimensions."""
    with Image.open(image_path) as img:
        # Get original dimensions
        original_width, original_height = img.size
        print(f"Original Dimensions: {original_width}x{original_height}")
        
        # Calculate nearest power of two dimensions
        new_width = nearest_power_of_two(original_width)
        new_height = nearest_power_of_two(original_height)
        print(f"Resized Dimensions: {new_width}x{new_height}")
        
        # Resize the image
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Generate the output file name
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_{new_width}x{new_height}{ext}"
        
        # Save the resized image
        resized_img.save(output_path)
        print(f"Image saved to {output_path}")


def process_images_to_power_of_two(directory: str, filetypes: List[str]) -> None:
    """
    Process image files recursively in a directory, resizing each to the nearest power of two dimensions.

    Args:
        directory (str): The root directory to search for image files.
        filetypes (List[str]): A list of image file extensions to process (e.g., ['.jpg', '.png']).
    """
    process_files_recursively(directory, filetypes, resize_image_to_power_of_two)

def main():
    parser = argparse.ArgumentParser(
        description="Resize image files in a directory to the nearest power-of-two dimensions."
    )
    parser.add_argument(
        "directory",
        type=str,
        help="The root directory to search for image files.",
    )
    parser.add_argument(
        "--filetypes",
        type=str,
        nargs="+",
        default=[".jpg", ".png"],
        help="A list of image file extensions to process (e.g., '.jpg', '.png'). Defaults to '.jpg' and '.png'.",
    )
    args = parser.parse_args()

    print(f"Processing images in directory: {args.directory}")
    print(f"File types to process: {args.filetypes}")

    process_images_to_power_of_two(args.directory, args.filetypes)

if __name__ == "__main__":
    main()
