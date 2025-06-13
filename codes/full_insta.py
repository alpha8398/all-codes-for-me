import instaloader

L = instaloader.Instaloader()

# Use cookies extracted from browser
L.context._session.cookies.update({
    'sessionid': '60643117876%3A5yRSZEMHyW5WlW%3A22%3AAYe9lq4sZsB7kOvdglxmlL_uB4DUuALQ8ma_Mi0KyuI',
    'ds_user_id': '60643117876',
    'csrftoken': 'SVmfN3ts7QECGTgilRQSq8',
    'mid': 'Z9KwvQALAAEzuKE2tXkcVWaXPANx'
})

# Test by loading your own profile
profile = instaloader.Profile.from_username(L.context, "your_username")
print(f"Logged in as: {profile.username}")

# Now access another profile
target = instaloader.Profile.from_username(L.context, "promediaimages")
for post in target.get_posts():
    L.download_post(post, target.username)
