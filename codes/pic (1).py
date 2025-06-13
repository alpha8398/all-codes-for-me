import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Enter the Instagram post URL
post_url = "https://www.instagram.com/p/DIDmAdByvje/?utm_source=ig_web_copy_link"  # Replace with the actual URL

# Extract the post ID from the URL
post_shortcode = post_url.split("/")[-2]

# Download the post
try:
    # Load the post
    post = instaloader.Post.from_shortcode(L.context, post_shortcode)

    # Download the post's image
    L.download_post(post, target="downloaded_images")

    print("Image downloaded successfully!")

except Exception as e:
    print(f"Error: {e}")
