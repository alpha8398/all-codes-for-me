import os
import shutil

# Path to the directory containing your photos
photos_dir = "C:/hpswsetup/sp108788/codes/tupaki_gallery"  # Replace with the actual path

# Path to the directory where the new folders will be created
output_dir = "C:/hpswsetup/sp108789/telegram/actress_photos/nora mommy"  # Replace with the desired output path

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all files in the photos directory
photos = [f for f in os.listdir(photos_dir) if os.path.isfile(os.path.join(photos_dir, f))]

# Sort the photos to maintain a consistent order (optional)
photos.sort()

# Create folders and move 150 photos into each folder
folder_index = 1
for i in range(0, len(photos), 450):
    folder_name = f"folder_{folder_index}"
    folder_path = os.path.join(output_dir, folder_name)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Move 150 photos into the folder
    for photo in photos[i:i+450]:
        src = os.path.join(photos_dir, photo)
        dest = os.path.join(folder_path, photo)
        shutil.move(src, dest)
    
    folder_index += 1

print(f"Photos have been organized into {folder_index - 1} folders.")
