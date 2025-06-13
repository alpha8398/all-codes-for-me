# import os

# # Set your desired path here
# base_path = r"C:/hpswsetup/frames"  # Change this to your desired location

# # Create folders 1 to 277
# for i in range(1, 278):  # 278 because range is exclusive at the end
#     folder_name = str(i)
#     folder_path = os.path.join(base_path, folder_name)
    
#     # Create folder if it doesn't already exist
#     os.makedirs(folder_path, exist_ok=True)

# print("Folders created successfully.")


for num in range(1, 278):
    print(f"ffmpeg -i {num}.mp4 -vf fps=1 frames/{num}/output_%%04d.png")


    # ffmpeg -i 9.mp4 -vf fps=1 frames/output_%04d.png

# 