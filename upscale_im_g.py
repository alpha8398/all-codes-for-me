# # from PIL import Image

# # def upscale_preserve_aspect(input_path, output_path):
# #     # Target resolution (1080p)
# #     max_width, max_height = 1920, 1080

# #     # Open original image
# #     img = Image.open(input_path)
# #     orig_width, orig_height = img.size

# #     # Calculate scaling factor (fit within 1080p)
# #     scale_factor = min(max_width / orig_width, max_height / orig_height)

# #     # New size with same aspect ratio
# #     new_size = (int(orig_width * scale_factor), int(orig_height * scale_factor))

# #     # Resize image using high-quality resampling
# #     upscaled_img = img.resize(new_size, Image.LANCZOS)

# #     # Save the result
# #     upscaled_img.save(output_path)
# #     print(f"Image upscaled to {new_size} and saved as {output_path}")

# # # Example usage
# # upscale_preserve_aspect("input.jpg", "upscaled_preserved_1080p.jpg")


# from PIL import Image

# def upscale_to_8k(input_path, output_path):
#     # Target resolution (8K)
#     max_width, max_height = 7680, 4320

#     # Open the original image
#     img = Image.open(input_path)
#     orig_width, orig_height = img.size

#     # Calculate scale factor to fit within 8K while keeping aspect ratio
#     scale_factor = min(max_width / orig_width, max_height / orig_height)

#     # Compute new size
#     new_size = (int(orig_width * scale_factor), int(orig_height * scale_factor))

#     # Resize image with high-quality LANCZOS filter
#     upscaled_img = img.resize(new_size, Image.LANCZOS)

#     # Save the result
#     upscaled_img.save(output_path)
#     print(f"Image upscaled to {new_size} and saved as {output_path}")

# # Example usage
# upscale_to_8k("input.jpg", "upscaled_to_8k.jpg")



import cv2
import numpy as np

# === Load the image ===
img = cv2.imread("input.jpg")

# === Resize if too small ===
h, w = img.shape[:2]
scale = 6  # upscale factor to simulate 4K-like clarity
img = cv2.resize(img, (w*scale, h*scale), interpolation=cv2.INTER_CUBIC)

# === Denoise to smooth skin ===
denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# === Sharpen to enhance details ===
sharpen_kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])
sharpened = cv2.filter2D(denoised, -1, sharpen_kernel)

# === Increase contrast and saturation ===
hsv = cv2.cvtColor(sharpened, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
s = cv2.multiply(s, 1.3)  # Boost saturation
v = cv2.multiply(v, 1.1)  # Slightly boost brightness
final_hsv = cv2.merge([h, s, v])
vibrant = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

# === Optional: Add soft glow (simulate beautification effect) ===
blurred = cv2.GaussianBlur(vibrant, (0, 0), 10)
glow = cv2.addWeighted(vibrant, 1.5, blurred, -0.5, 0)

# === Save result ===
cv2.imwrite("portrait_styled_output.jpg", glow)
