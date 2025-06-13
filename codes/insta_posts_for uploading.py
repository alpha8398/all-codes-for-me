from PIL import Image

def add_padding_to_4_5_aspect(input_path, output_path_full_res, output_path_instagram=None, background_color=(0, 0, 0)):
    target_aspect_ratio = 4 / 5

    # Load original image
    img = Image.open(input_path)
    orig_width, orig_height = img.size
    orig_ratio = orig_width / orig_height

    # Calculate new size with padding
    if orig_ratio > target_aspect_ratio:
        # Image is too wide → pad height
        new_height = int(orig_width / target_aspect_ratio)
        new_width = orig_width
    else:
        # Image is too tall → pad width
        new_width = int(orig_height * target_aspect_ratio)
        new_height = orig_height

    # Create new image with black background
    new_img = Image.new("RGB", (new_width, new_height), background_color)
    offset_x = (new_width - orig_width) // 2
    offset_y = (new_height - orig_height) // 2
    new_img.paste(img, (offset_x, offset_y))

    # Save high-res 4:5 padded image
    new_img.save(output_path_full_res)
    print(f"✅ Saved full-resolution 4:5 image: {output_path_full_res}")

    # Optionally save Instagram-sized version
    if output_path_instagram:
        insta_size = (1080, 1350)
        resized = new_img.resize(insta_size, Image.LANCZOS)
        resized.save(output_path_instagram)
        print(f"✅ Saved resized 1080x1350 version for Instagram: {output_path_instagram}")

# Example usage
add_padding_to_4_5_aspect(
    input_path="Trisha Krishnan.jpg",
    output_path_full_res="your_image_4x5_black_full.jpg",
    output_path_instagram="your_image_1080x1350_black.jpg"
)
