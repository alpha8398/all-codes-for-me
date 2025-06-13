import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Saves the video with the title as the filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
video_url = 'https://www.instagram.com/reels/DKqjxMtodnX/'  # Replace with your video URL
download_video(video_url)
