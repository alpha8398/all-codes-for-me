import os

def rename_mp4_files(directory):
    # List all .mp4 files in the directory
    mp4_files = [f for f in os.listdir(directory) if f.lower().endswith('.mp4')]
    mp4_files.sort()  # Optional: sort files alphabetically before renaming

    # Rename each file
    for index, filename in enumerate(mp4_files, start=1):
        new_name = f"{index}.mp4"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)

        # Avoid name collision
        if os.path.exists(dst):
            print(f"Skipping {filename} -> {new_name} (already exists)")
            continue

        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
folder_path = r"C:\hpswsetup\sp108789\po_rn"  # Change this to your folder path
rename_mp4_files(folder_path)
