import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',  # Saves the video with the title as the filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
video_url = 'https://xhamster.best/videos/desi-step-sister-hardcore-anal-fuck-with-her-step-brother-when-they-were-alone-at-home-full-movie-xhKfYNC'  # Replace with your video URL
download_video(video_url)
