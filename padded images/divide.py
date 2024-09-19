import os
import shutil
import random

def split_dataset(source_folder, train_folder, test_folder, validation_folder, split_ratio=(0.7, 0.15, 0.15)):
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)

    for root, dirs, files in os.walk(source_folder):
        for dir_name in dirs:
            train_dir = os.path.join(train_folder, os.path.relpath(root, source_folder), dir_name)
            test_dir = os.path.join(test_folder, os.path.relpath(root, source_folder), dir_name)
            validation_dir = os.path.join(validation_folder, os.path.relpath(root, source_folder), dir_name)
            os.makedirs(train_dir, exist_ok=True)
            os.makedirs(test_dir, exist_ok=True)
            os.makedirs(validation_dir, exist_ok=True)

        random.shuffle(files)
        total_files = len(files)
        train_split = int(total_files * split_ratio[0])
        test_split = int(total_files * split_ratio[1])

        for i, file_name in enumerate(files):
            source_path = os.path.join(root, file_name)
            if i < train_split:
                destination_path = os.path.join(train_folder, os.path.relpath(root, source_folder), file_name)
            elif i < train_split + test_split:
                destination_path = os.path.join(test_folder, os.path.relpath(root, source_folder), file_name)
            else:
                destination_path = os.path.join(validation_folder, os.path.relpath(root, source_folder), file_name)

            shutil.copy(source_path, destination_path)  # Use shutil.move if you want to move instead of copy

# Set your source, train, test, and validation folder paths
source_folder = r"C:\Users\91758\Downloads\padded images"
train_folder = r"C:\Users\91758\Downloads\dataset\train_set"
test_folder = r"C:\Users\91758\Downloads\dataset\test_set"
validation_folder = r"C:\Users\91758\Downloads\dataset\validation_set"

split_dataset(source_folder, train_folder, test_folder, validation_folder)
