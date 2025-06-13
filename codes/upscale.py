# from PIL import Image

# # Load your image
# input_path = "C:\hpswsetup\sp108788\codes/3rd.jpg"      # <-- change this to your actual file path
# output_path = "C:\hpswsetup\sp108788\codes/upscaled_image.png"  # Output path

# # Open the image
# image = Image.open(input_path)

# # Target 4K size (width x height)
# target_size = (3840, 2160)  # Standard 4K UHD resolution

# # Use high-quality upscaling (LANCZOS filter)
# upscaled_image = image.resize(target_size, Image.LANCZOS)

# # Save as PNG (lossless)
# upscaled_image.save(output_path, format='PNG')

# print("Image upscaled to 4K and saved as:", output_path)


# from PIL import Image

# input_path = "C:\hpswsetup\sp108788\codes/3rd.jpg"
# output_path = "C:\hpswsetup\sp108788\codes/upscaled_image.png"

# image = Image.open(input_path)

# # Target max dimensions for 4K
# target_width = 3840
# target_height = 2160

# # Calculate proportional size
# image.thumbnail((target_width, target_height), Image.LANCZOS)

# # Save lossless
# image.save(output_path, format='PNG')

# print("Image scaled proportionally and saved as:", output_path)


from PIL import Image

# Input and Output Paths
input_path = "C:\hpswsetup\sp108788\codes/3rd.jpg"  # <-- your image path
output_path = "C:\hpswsetup\sp108788\codes/upscaled_4k.jpg"

# Open your image
image = Image.open(input_path)

# Target 4K resolution
target_width = 3840
target_height = 2160

# Preserve aspect ratio and resize
image.thumbnail((target_width, target_height), Image.LANCZOS)

# Create a new black 4K background
background = Image.new('RGB', (target_width, target_height), (0, 0, 0))

# Calculate center position
offset_x = (target_width - image.width) // 2
offset_y = (target_height - image.height) // 2

# Paste your scaled image onto the center of the background
background.paste(image, (offset_x, offset_y))

# Save as PNG (lossless)
background.save(output_path, format='PNG')

print("✅ Image scaled without distortion and saved as:", output_path)


