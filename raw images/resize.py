from PIL import Image, ImageOps
import os

def pad_image(input_path, output_path, padding_color, padding_width):
    image = Image.open(input_path)
    
    padded_image = ImageOps.expand(image, border=(padding_width, padding_width, padding_width, padding_width), fill=padding_color)
    
    padded_image.save(output_path)

if __name__ == "__main__":
    remo_folder = r"C:\Users\91758\Downloads\raw images"  # Path to the main folder containing subfolders
    output_folder = r"C:\Users\91758\Downloads\padded images"  # Path to the output folder
    padding_color = (0, 0, 0)  # RGB value for black
    padding_width = 25  # Specify the width of the padding
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through subfolders in the remo folder
    for subfolder in os.listdir(remo_folder):
        subfolder_path = os.path.join(remo_folder, subfolder)
        
        # Check if the subfolder is a directory
        if os.path.isdir(subfolder_path):
            output_subfolder = os.path.join(output_folder, subfolder)
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            
            # Iterate through image files in the subfolder
            for filename in os.listdir(subfolder_path):
                if filename.endswith(('.jpg', '.jpeg', '.png')):
                    input_path = os.path.join(subfolder_path, filename)
                    output_filename = f"padded_{filename}"
                    output_path = os.path.join(output_subfolder, output_filename)
                    
                    pad_image(input_path, output_path, padding_color, padding_width)
