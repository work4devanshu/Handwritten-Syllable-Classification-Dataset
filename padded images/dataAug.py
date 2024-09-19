from PIL import Image
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import shutil

# Define augmentation generators for each augmentation type
a = ImageDataGenerator(rotation_range=30)
b = ImageDataGenerator(width_shift_range=0.15)
c = ImageDataGenerator(shear_range=30)
d = ImageDataGenerator(height_shift_range=0.15)
e = ImageDataGenerator(zoom_range=0.3)
f = ImageDataGenerator(shear_range=30,rotation_range=30)
g = ImageDataGenerator(shear_range=30,rotation_range=30,width_shift_range=0.15)
h = ImageDataGenerator(shear_range=30,rotation_range=30,height_shift_range=0.15)
i = ImageDataGenerator(shear_range=30,rotation_range=30,zoom_range=0.25)
j = ImageDataGenerator(height_shift_range=0.15,width_shift_range=0.15)

# Define additional augmentation generators as needed

# Define a function to perform data augmentation and save images
def augment_and_save_images(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for subdir in os.listdir(src_dir):
        src_subdir = os.path.join(src_dir, subdir)
        dest_subdir = os.path.join(dest_dir, subdir)
        if os.path.isdir(src_subdir):
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)

            for img_name in os.listdir(src_subdir):
                img_path = os.path.join(src_subdir, img_name)
                img = Image.open(img_path)
                img = img.convert("RGB")  # Ensure that the image has 3 channels

                img_array = np.array(img)
                img_array = img_array.reshape((1,) + img_array.shape)  # Convert to batch format

                # Generate augmented images for each augmentation type
                for datagen in [a,b,c,d,e,f,g,h,i,j]:
                    aug_generator = datagen.flow(img_array, batch_size=1, save_to_dir=dest_subdir, save_prefix='aug', save_format='png')
                    num_augmented_images = 1   # You can adjust the number of augmented images you want to generate

                    for _ in range(num_augmented_images):
                        next(aug_generator)

# Define paths for source and destination directories
src_base_data_dir = "C:\\Users\\91758\\Downloads\\padded images"
dest_base_data_dir = "C:\\Users\\91758\\Downloads\\augmented_images"

# Call the function to perform data augmentation and save images
augment_and_save_images(src_base_data_dir, dest_base_data_dir)
