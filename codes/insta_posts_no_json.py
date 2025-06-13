# import instaloader

# # Initialize Instaloader with preferred options
# L = instaloader.Instaloader(
#     download_pictures=True,        # Download only pictures
#     download_video_thumbnails=False,
#     download_videos=True,          # Download videos if any
#     download_geotags=False,
#     download_comments=False,
#     save_metadata=False,           # Don't save .json metadata
#     compress_json=False,           # Don't save compressed .json
#     post_metadata_txt_pattern=''   # No metadata text file
# )

# # Set your session cookies
# L.context._session.cookies.update({
#     'sessionid': '60643117876%3A2W7gt7mlFE1Bjh%3A22%3AAYeV1smsBsElq5c8xWDNSMh2UsK9j6Gw-fTlZ3RxGQ',
#     'ds_user_id': '60643117876',
#     'csrftoken': 'SVmfN3ts7QECGTgilRQSq8',
#     'mid': 'Z9KwvQALAAEzuKE2tXkcVWaXPANx'
# })

# # Replace with your actual username to test login
# your_profile = instaloader.Profile.from_username(L.context, "your_username")
# print(f"Logged in as: {your_profile.username}")

# # Target profile
# target = instaloader.Profile.from_username(L.context, "actresseditz.v4_")

# # Print total post count
# print(f"Total posts: {target.mediacount}")

# # Download posts
# for index, post in enumerate(target.get_posts(), start=1):
#     print(f"Downloading post {index} of {target.mediacount}: {post.shortcode}")
#     L.download_post(post, target.username)
# # ana.whiteros


import instaloader

# Initialize Instaloader
L = instaloader.Instaloader(
    download_pictures=True,
    download_video_thumbnails=False,
    download_videos=True,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    post_metadata_txt_pattern=''
)

# Set session cookies (make sure these are up to date)
L.context._session.cookies.update({
    'sessionid': '60643117876%3A1QuXNZtegaMX6z%3A6%3AAYejaHBV-3ksOH37NS9mRjpjSx-X6k9B-iIbILwtdNam',
    'ds_user_id': '60643117876',
    'csrftoken': 'SVmfN3ts7QECGTgilRQSq8',
    'mid': 'Z9KwvQALAAEzuKE2tXkcVWaXPANx'
})

# Confirm login (optional)
your_profile = instaloader.Profile.from_username(L.context, "your_username")
print(f"Logged in as: {your_profile.username}")

# List of Instagram usernames you want to download from
target_usernames = [

"cult_shriyasaran",



]

# Loop through each profile and download posts
for username in target_usernames:
    try:
        target = instaloader.Profile.from_username(L.context, username)
        print(f"\nDownloading posts from {username} ({target.mediacount} posts)")
        
        for index, post in enumerate(target.get_posts(), start=1):
            print(f"Downloading post {index}: {post.shortcode}")
            L.download_post(post, target.username)
    except Exception as e:
        print(f"Failed to download from {username}: {e}")
