# import yt_dlp

# def download_x_video(url, output_path="1.mp4"):
#     headers = {
#         'Cookie': 'auth_token=fcd9913b8b41850747a30e8c4d4cb92622330fc9; ct0=61030a9d65771dae2048829a0169309ff1a70d2b27c1fc5fe242c833c16e341dc4f46ca5a455c3143e015aa0a3b397b1a3111d34ff3660808bfb22a4d0a276768d4dbb73c43b0f1ba1b2007b7c56a8eb'
#     }
    
#     ydl_opts = {
#         'format': 'best',
#         'outtmpl': output_path,
#         'http_headers': headers,
#     }
    
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
    
#     print(f"Download complete: {output_path}")

# # Example usage
# video_url = "https://x.com/T4tusy/status/1925227983113204079"
# download_x_video(video_url)


import yt_dlp

# List of video URLs from X
video_urls = [
"https://x.com/hohnseena9/status/1931902327994335541",
"https://x.com/ManiacActress/status/1931568228213403976",
"https://x.com/reloadead69/status/1932041308727812343",
"https://x.com/Pettite_Beauty/status/1850185943048733156",
"https://x.com/Pettite_Beauty/status/1923408589785284959",
"https://x.com/GlamspotA/status/1932024077436518502",
"https://x.com/GlamspotA/status/1932129326549647543",
"https://x.com/mouniroystan/status/1931595932401045974",
"https://x.com/ordinarygaadni/status/1931660934126440863",
"https://x.com/CrushSlot/status/1931942297312309508",
"https://x.com/Starleth3re2/status/1931714845189235187",
"https://x.com/KAISER_111/status/1931756055106597334",
""
]

# Insert your own valid cookies here (⚠️ use with caution!)
headers = {
    'Cookie': 'auth_token=fcd9913b8b41850747a30e8c4d4cb92622330fc9; ct0=61030a9d65771dae2048829a0169309ff1a70d2b27c1fc5fe242c833c16e341dc4f46ca5a455c3143e015aa0a3b397b1a3111d34ff3660808bfb22a4d0a276768d4dbb73c43b0f1ba1b2007b7c56a8eb'
}

def download_x_video(url, index):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'video_{index}.mp4',
        'http_headers': headers,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"✅ Downloaded: video_{index}.mp4")
        except Exception as e:
            print(f"❌ Failed to download {url}: {e}")

# Loop through all URLs
for i, url in enumerate(video_urls, start=1):
    download_x_video(url, i)
